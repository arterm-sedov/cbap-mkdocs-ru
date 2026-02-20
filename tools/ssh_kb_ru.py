"""
Enhanced SSH utility module for establishing SSH tunnels and MySQL connections.

Features:
- Cross-platform support (Windows/Linux)
- Multiple server configurations via JSON files
- SSH key authentication with password fallback
- OS keychain integration:
  - Windows: Credential Manager
  - Linux with GUI: GNOME Keyring, KWallet (via D-Bus)
  - Linux headless: File-based encrypted keyring (~/.local/share/python_keyring/)
  - macOS: Keychain Access
- .env file support for credential paths
- Automatic SSH key detection and use
- SSH config file parsing (~/.ssh/config)
- Encrypted SSH key passphrase support
- Enhanced error handling with specific exceptions
"""

import json
import os
import platform
import socket
from getpass import getpass
from pathlib import Path
from typing import Optional, Tuple, Dict

import mysql.connector

# Compatibility shim for Paramiko>=3 where DSSKey (DSA) was removed.
# Some versions of sshtunnel still reference paramiko.DSSKey during key discovery.
try:
    import paramiko  # type: ignore
    if not hasattr(paramiko, "DSSKey"):
        # Alias to RSAKey to satisfy attribute access; password auth will ignore it.
        paramiko.DSSKey = paramiko.RSAKey  # type: ignore[attr-defined]
    PARAMIKO_AVAILABLE = True
except Exception:
    # Best-effort: if paramiko is not installed, sshtunnel import will raise later.
    PARAMIKO_AVAILABLE = False

from sshtunnel import SSHTunnelForwarder  # type: ignore

# Optional dependencies - gracefully handle if not installed
try:
    import keyring  # type: ignore
    KEYRING_AVAILABLE = True
    
    # Try to initialize keyring backend
    # On headless Linux, fall back to file-based backend if D-Bus is not available
    try:
        # Test if default backend works by getting the keyring instance
        _ = keyring.get_keyring()
    except (RuntimeError, Exception):
        # Check if it's a keyring initialization error (no D-Bus, etc.)
        # Default backend failed (likely headless Linux without D-Bus)
        # Try to use file-based backend as fallback
        try:
            # Use file backend which stores passwords encrypted in ~/.local/share/python_keyring/
            # This works without D-Bus or GUI
            import keyring.backends.file
            # Try EncryptedKeyring first (more secure)
            try:
                file_keyring = keyring.backends.file.EncryptedKeyring()
            except Exception:
                # Fall back to PlaintextKeyring if encryption not available
                file_keyring = keyring.backends.file.PlaintextKeyring()
            # Set as default backend
            keyring.set_keyring(file_keyring)
        except Exception:
            # File backend also failed, keyring will be disabled
            KEYRING_AVAILABLE = False
except ImportError:
    KEYRING_AVAILABLE = False

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

# Load .env file if available
if DOTENV_AVAILABLE:
    load_dotenv()

# Keychain service name for storing credentials
KEYCHAIN_SERVICE = "ssh_kb_ru"


def _get_ssh_key_directory() -> Path:
    """Get the SSH key directory path based on the platform.
    
    Returns:
        Path to the SSH key directory (~/.ssh on Linux/Mac, %USERPROFILE%\\.ssh on Windows)
    """
    if platform.system() == "Windows":
        ssh_dir = Path(os.environ.get("USERPROFILE", "")) / ".ssh"
    else:
        ssh_dir = Path.home() / ".ssh"
    return ssh_dir


def _get_ssh_config_path() -> Path:
    """Get the SSH config file path based on the platform.
    
    Returns:
        Path to SSH config file (~/.ssh/config on Linux/Mac, %USERPROFILE%\\.ssh\\config on Windows)
    """
    ssh_dir = _get_ssh_key_directory()
    return ssh_dir / "config"


def _get_keychain_key(server_profile: str, credential_type: str) -> str:
    """Generate a keychain key for storing credentials.
    
    Args:
        server_profile: Server profile identifier (derived from credentials file name)
        credential_type: Type of credential ('ssh_password', 'sql_password', or 'ssh_key_passphrase')
    
    Returns:
        Keychain key string
    """
    return f"{KEYCHAIN_SERVICE}:{server_profile}:{credential_type}"


def _get_keychain_password(server_profile: str, credential_type: str) -> Optional[str]:
    """Retrieve a password from the OS keychain.
    
    Supports both GUI-based keyrings (GNOME Keyring, KWallet, Windows Credential Manager)
    and file-based keyring for headless Linux systems.
    
    Args:
        server_profile: Server profile identifier
        credential_type: Type of credential ('ssh_password', 'sql_password', or 'ssh_key_passphrase')
    
    Returns:
        Password string if found, None otherwise
    """
    if not KEYRING_AVAILABLE:
        return None
    
    # Import keyring at function level to avoid UnboundLocalError
    import keyring as kr  # Use alias to avoid shadowing
    
    try:
        key = _get_keychain_key(server_profile, credential_type)
        password = kr.get_password(KEYCHAIN_SERVICE, key)
        return password
    except (RuntimeError, Exception) as e:
        # Check if it's a keyring backend initialization error
        is_keyring_error = False
        if hasattr(kr, 'errors'):
            if isinstance(e, (kr.errors.NoKeyringError, kr.errors.InitError)):
                is_keyring_error = True
        # RuntimeError is common when D-Bus is not available on headless Linux
        if isinstance(e, RuntimeError) or is_keyring_error:
            # Keyring backend not available (e.g., no D-Bus on headless Linux)
            # Try to initialize file-based backend as fallback
            try:
                import keyring.backends.file as kr_backends_file
                # Try EncryptedKeyring first (more secure)
                try:
                    file_keyring = kr_backends_file.EncryptedKeyring()
                except Exception:
                    # Fall back to PlaintextKeyring if encryption not available
                    file_keyring = kr_backends_file.PlaintextKeyring()
                kr.set_keyring(file_keyring)
                # Retry with file backend
                password = kr.get_password(KEYCHAIN_SERVICE, key)
                return password
            except Exception:
                # File backend also failed
                return None
        # Other keyring errors (e.g., password not found)
        return None


def _get_keychain_key_passphrase(server_profile: str, key_path: str) -> Optional[str]:
    """Retrieve SSH key passphrase from the OS keychain.
    
    Args:
        server_profile: Server profile identifier
        key_path: Path to the SSH key file
    
    Returns:
        Passphrase string if found, None otherwise
    """
    # Use key path as part of the credential type to support multiple keys
    credential_type = f"ssh_key_passphrase:{key_path}"
    return _get_keychain_password(server_profile, credential_type)


def _set_keychain_key_passphrase(server_profile: str, key_path: str, passphrase: str) -> bool:
    """Store SSH key passphrase in the OS keychain.
    
    Args:
        server_profile: Server profile identifier
        key_path: Path to the SSH key file
        passphrase: Passphrase to store
    
    Returns:
        True if successful, False otherwise
    """
    credential_type = f"ssh_key_passphrase:{key_path}"
    stored, _ = _set_keychain_password(server_profile, credential_type, passphrase, verbose=False)
    return stored


def _set_keychain_password(server_profile: str, credential_type: str, password: str, verbose: bool = False) -> Tuple[bool, Optional[str]]:
    """Store a password in the OS keychain.
    
    Supports both GUI-based keyrings (GNOME Keyring, KWallet, Windows Credential Manager)
    and file-based keyring for headless Linux systems.
    
    Args:
        server_profile: Server profile identifier
        credential_type: Type of credential ('ssh_password' or 'sql_password')
        password: Password to store
        verbose: If True, return error message in tuple
    
    Returns:
        Tuple of (success: bool, error_message: Optional[str])
        If verbose=False, returns (bool, None)
    """
    if not KEYRING_AVAILABLE:
        error_msg = "Keyring module is not available"
        return (False, error_msg if verbose else None)
    
    # Import keyring at function level to avoid UnboundLocalError
    import keyring as kr_set  # Use alias to avoid shadowing
    
    try:
        key = _get_keychain_key(server_profile, credential_type)
        kr_set.set_password(KEYCHAIN_SERVICE, key, password)
        # Verify password was stored by trying to retrieve it
        stored_password = kr_set.get_password(KEYCHAIN_SERVICE, key)
        if stored_password == password:
            return (True, None)
        else:
            # Password was stored but doesn't match - might be a keyring issue
            error_msg = f"Password verification failed (stored password doesn't match)"
            return (False, error_msg if verbose else None)
    except (RuntimeError, Exception) as e:
        error_msg = str(e)
        # Check if it's a keyring backend initialization error
        is_keyring_error = False
        if hasattr(kr_set, 'errors'):
            if isinstance(e, (kr_set.errors.NoKeyringError, kr_set.errors.InitError)):
                is_keyring_error = True
        # RuntimeError is common when D-Bus is not available on headless Linux
        if isinstance(e, RuntimeError) or is_keyring_error:
            # Keyring backend not available (e.g., no D-Bus on headless Linux)
            # Try to initialize file-based backend as fallback
            try:
                import keyring.backends.file as kr_backends_file
                # Try EncryptedKeyring first (more secure)
                try:
                    file_keyring = kr_backends_file.EncryptedKeyring()
                except Exception as enc_error:
                    # Fall back to PlaintextKeyring if encryption not available
                    try:
                        file_keyring = kr_backends_file.PlaintextKeyring()
                    except Exception as plain_error:
                        error_msg = f"File backend initialization failed: {plain_error}"
                        return (False, error_msg if verbose else None)
                kr_set.set_keyring(file_keyring)
                # Retry with file backend
                kr_set.set_password(KEYCHAIN_SERVICE, key, password)
                # Verify with file backend
                stored_password = kr_set.get_password(KEYCHAIN_SERVICE, key)
                if stored_password == password:
                    return (True, None)
                else:
                    error_msg = "File backend: Password verification failed"
                    return (False, error_msg if verbose else None)
            except Exception as file_error:
                error_msg = f"File backend failed: {file_error}"
                return (False, error_msg if verbose else None)
        # Other keyring errors
        error_msg = f"Keyring error: {error_msg}"
        return (False, error_msg if verbose else None)


def _get_server_profile_from_path(credentials_path: str) -> str:
    """Extract server profile identifier from credentials file path.
    
    Args:
        credentials_path: Path to credentials JSON file
    
    Returns:
        Server profile identifier (filename without extension)
    """
    profile = Path(credentials_path).stem
    # Remove leading dot if present (e.g., ".serverCredentials" -> "serverCredentials")
    if profile.startswith("."):
        profile = profile[1:]
    return profile


def _load_server_credentials(credentials_path: str = ".serverCredentials.json") -> dict:
    """Load server credentials from JSON file, with .env path override support.
    
    Checks .env file for CREDENTIALS_PATH variable first, then falls back to
    the provided credentials_path parameter.
    
    Args:
        credentials_path: Default path to credentials JSON file
    
    Returns:
        Dictionary with server credentials, empty dict if file is empty or not found
    """
    # Check .env for credentials path override
    env_path = os.getenv("CREDENTIALS_PATH") or os.getenv("SERVER_CREDENTIALS_PATH")
    if env_path:
        credentials_path = env_path
    
    try:
        with open(credentials_path, "r") as server_credentials_file:
            content = server_credentials_file.read()
            return json.loads(content) if content else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def _parse_ssh_config(hostname: str) -> Dict[str, str]:
    """Parse SSH config file and return configuration for the given hostname.
    
    Args:
        hostname: SSH hostname to look up in config
    
    Returns:
        Dictionary with SSH config values (hostname, port, user, identityfile, etc.)
        Empty dict if config file not found or hostname not matched
    """
    if not PARAMIKO_AVAILABLE:
        return {}
    
    config_path = _get_ssh_config_path()
    if not config_path.exists():
        return {}
    
    try:
        ssh_config = paramiko.SSHConfig()
        with open(config_path, "r") as f:
            ssh_config.parse(f)
        
        config = ssh_config.lookup(hostname)
        result = {}
        
        # Extract relevant config values
        if config.get("hostname"):
            result["hostname"] = config["hostname"]
        if config.get("port"):
            result["port"] = config["port"]
        if config.get("user"):
            result["user"] = config["user"]
        if config.get("identityfile"):
            # IdentityFile can be a list, take the first one
            identity_files = config["identityfile"]
            if isinstance(identity_files, list) and len(identity_files) > 0:
                result["identityfile"] = identity_files[0]
            elif isinstance(identity_files, str):
                result["identityfile"] = identity_files
        
        return result
    except Exception:
        # Config parsing failed, return empty dict
        return {}


def _expand_ssh_path(path: str) -> Path:
    """Expand SSH config path tokens like ~, %h, %u, etc.
    
    Args:
        path: Path string that may contain tokens
    
    Returns:
        Expanded Path object
    """
    # Expand ~ to home directory
    if path.startswith("~"):
        path = str(Path.home()) + path[1:]
    
    # Expand %h (hostname) - not applicable here, but handle other common tokens
    # For now, just return as-is after ~ expansion
    return Path(path)


def _detect_ssh_keys(ssh_host: str, ssh_username: str, ssh_config: Optional[Dict[str, str]] = None) -> Optional[str]:
    """Detect and return path to SSH private key if available.
    
    Checks SSH config IdentityFile first, then common SSH key locations.
    SSHTunnelForwarder will automatically use keys from ~/.ssh/ if allow_agent=True,
    but we can also explicitly provide a key path.
    
    Args:
        ssh_host: SSH hostname
        ssh_username: SSH username
        ssh_config: Optional SSH config dictionary (from _parse_ssh_config)
    
    Returns:
        Path to SSH private key if found, None otherwise
    """
    ssh_dir = _get_ssh_key_directory()
    
    # First, check SSH config IdentityFile if available
    if ssh_config and ssh_config.get("identityfile"):
        identity_file = ssh_config["identityfile"]
        expanded_path = _expand_ssh_path(identity_file)
        
        # Try absolute path first
        if expanded_path.is_absolute() and expanded_path.exists() and expanded_path.is_file():
            return str(expanded_path)
        
        # Try relative to ~/.ssh
        if ssh_dir.exists():
            relative_path = ssh_dir / expanded_path.name
            if relative_path.exists() and relative_path.is_file():
                return str(relative_path)
    
    if not ssh_dir.exists():
        return None
    
    # Common SSH key filenames to check
    key_names = [
        "id_rsa",
        "id_ed25519",
        "id_ecdsa",
        "id_dsa",
        f"{ssh_host}_rsa",
        f"{ssh_host}_ed25519",
    ]
    
    for key_name in key_names:
        key_path = ssh_dir / key_name
        if key_path.exists() and key_path.is_file():
            return str(key_path)
    
    return None


def _prompt_with_default(prompt: str, default_value: str) -> str:
    """Prompt the user, falling back to a provided default if available.
    
    Args:
        prompt: Prompt text to display
        default_value: Default value to use if user presses Enter
    
    Returns:
        User input or default value
    """
    if default_value:
        user_input = input(f"{prompt} (default: {default_value}):\n").strip()
        return user_input if user_input else default_value
    else:
        return input(prompt)


def _prompt_for_stored_credential(credential_type: str, server_profile: str) -> Optional[str]:
    """Prompt user to use stored credential or enter a new one.
    
    Args:
        credential_type: Type of credential ('ssh_password' or 'sql_password')
        server_profile: Server profile identifier
    
    Returns:
        Password string to use, or None if user wants to enter new one
    
    Raises:
        KeyboardInterrupt: If user cancels with Ctrl+C
    """
    stored_password = _get_keychain_password(server_profile, credential_type)
    
    if stored_password:
        credential_name = "SSH password" if credential_type == "ssh_password" else "SQL password"
        print(f"\n✓ Found stored {credential_name} in keychain for '{server_profile}'")
        try:
            choice = input(f"Use stored {credential_name}? (Y/n/Enter): ").strip().lower()
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            raise
        
        if choice in ('', 'y', 'yes'):
            print(f"Using stored {credential_name}...")
            return stored_password
        else:
            print(f"Entering new {credential_name}...")
            return None
    else:
        return None


def _load_ssh_key_with_passphrase(key_path: str, server_profile: str) -> Optional[paramiko.PKey]:
    """Load an SSH private key, handling encrypted keys with passphrases.
    
    Args:
        key_path: Path to the SSH private key file
        server_profile: Server profile identifier for keychain lookup
    
    Returns:
        Loaded PKey object if successful, None otherwise
    """
    if not PARAMIKO_AVAILABLE:
        return None
    
    try:
        # Try to load key without passphrase first
        # Try different key types to find the right one
        for key_class in [paramiko.RSAKey, paramiko.Ed25519Key, paramiko.ECDSAKey, paramiko.DSSKey]:
            try:
                key = key_class.from_private_key_file(key_path)
                return key
            except paramiko.ssh_exception.PasswordRequiredException:
                # Key is encrypted, need passphrase
                print(f"SSH key {key_path} is encrypted, requesting passphrase...")
                
                # Try to get passphrase from keychain
                passphrase = _get_keychain_key_passphrase(server_profile, key_path)
                
                if not passphrase:
                    passphrase = getpass(f"Enter passphrase for {key_path}:\n")
                    # Store passphrase in keychain for future use
                    _set_keychain_key_passphrase(server_profile, key_path, passphrase)
                else:
                    print(f"Using passphrase from keychain for {key_path}...")
                
                # Try all key types with passphrase
                for key_class_with_passphrase in [paramiko.RSAKey, paramiko.Ed25519Key, paramiko.ECDSAKey, paramiko.DSSKey]:
                    try:
                        key = key_class_with_passphrase.from_private_key_file(key_path, password=passphrase)
                        return key
                    except (paramiko.ssh_exception.SSHException, ValueError):
                        continue
                
                print(f"Failed to load encrypted key {key_path} with provided passphrase")
                return None
            except (paramiko.ssh_exception.SSHException, ValueError):
                # Wrong key type, try next
                continue
            
    except Exception as e:
        print(f"Error loading SSH key {key_path}: {e}")
        return None


def _try_ssh_connection_with_key(
    ssh_host: str,
    ssh_port: int,
    ssh_username: str,
    remote_bind_address: tuple,
    local_bind_address: tuple,
    server_profile: str,
    ssh_config: Optional[Dict[str, str]] = None,
) -> Optional[SSHTunnelForwarder]:
    """Attempt to establish SSH tunnel using SSH keys only.
    
    Args:
        ssh_host: SSH hostname
        ssh_port: SSH port
        ssh_username: SSH username
        remote_bind_address: Remote bind address tuple (host, port)
        local_bind_address: Local bind address tuple (host, port)
        server_profile: Server profile identifier for keychain lookup
        ssh_config: Optional SSH config dictionary
    
    Returns:
        SSHTunnelForwarder instance if successful, None if key auth fails
    """
    ssh_dir = _get_ssh_key_directory()
    
    # Detect SSH key with config support
    key_path = _detect_ssh_keys(ssh_host, ssh_username, ssh_config)
    
    # Try loading key with passphrase support if specific key found
    ssh_pkey = None
    if key_path and PARAMIKO_AVAILABLE:
        ssh_pkey = _load_ssh_key_with_passphrase(key_path, server_profile)
    
    try:
        print(f"Attempting SSH connection to {ssh_host}:{ssh_port} as {ssh_username}...")
        
        # Build tunnel parameters
        tunnel_params = {
            "ssh_address_or_host": (ssh_host, ssh_port),
            "ssh_username": ssh_username,
            "allow_agent": True,  # Use SSH agent if available
            "remote_bind_address": remote_bind_address,
            "local_bind_address": local_bind_address,
        }
        
        # Add explicit key if we loaded one
        if ssh_pkey:
            tunnel_params["ssh_pkey"] = ssh_pkey
            print(f"Using SSH key: {key_path}")
        elif ssh_dir.exists():
            # Fall back to directory-based key discovery
            tunnel_params["host_pkey_directories"] = [str(ssh_dir)]
            print(f"Using SSH key directory: {ssh_dir}")
        
        server = SSHTunnelForwarder(**tunnel_params)
        server.start()
        
        # Verify tunnel is actually working
        if not server.is_alive:
            print("Warning: SSH tunnel started but is not alive")
            server.stop()
            return None
        
        print(f"SSH tunnel established successfully on local port {server.local_bind_port}")
        return server
        
    except paramiko.AuthenticationException as e:
        print(f"SSH authentication failed: {e}")
        return None
    except paramiko.SSHException as e:
        print(f"SSH error occurred: {e}")
        return None
    except (socket.error, OSError) as e:
        print(f"Connection error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during SSH key authentication: {e}")
        return None


def establish_connection_interactive(credentials_path: str = ".serverCredentials.json") -> Tuple[mysql.connector.MySQLConnection, SSHTunnelForwarder]:
    """Establish an SSH tunnel and MySQL connection using interactive prompts.
    
    This function:
    1. Loads credentials from JSON file (with .env path override support)
    2. Parses SSH config file (~/.ssh/config) for host-specific settings
    3. Prompts for missing values with defaults from JSON and SSH config
    4. Tries SSH key authentication first (with passphrase support)
    5. Falls back to password authentication if keys are not available
    6. Stores passwords and passphrases in OS keychain for future use
    7. Validates tunnel connection before proceeding
    8. Establishes MySQL connection through SSH tunnel
    
    Args:
        credentials_path: Path to credentials JSON file (can be overridden via .env)
    
    Returns:
        Tuple of (mysql_connection, ssh_tunnel_server). Caller is responsible
        for closing both via `close_connection`.
    
    Raises:
        KeyboardInterrupt: If user cancels with Ctrl+C (connections are cleaned up)
        ConnectionError: If SSH tunnel cannot be established
        mysql.connector.Error: If MySQL connection fails
    """
    connection = None
    server = None
    
    try:
        server_credentials = _load_server_credentials(credentials_path)
        server_profile = _get_server_profile_from_path(credentials_path)
        
        # Get SSH host from credentials or prompt
        ssh_host = server_credentials.get("ssh_host", "")
        if not ssh_host:
            try:
                ssh_host = input("PHPKB host:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            print(f"PHPKB host: {ssh_host} (from credentials)")
        
        # Parse SSH config for this host
        ssh_config = _parse_ssh_config(ssh_host)
        if ssh_config:
            print(f"Found SSH config entry for {ssh_host}")
        
        # Use SSH config values as defaults, fall back to JSON credentials
        ssh_hostname = ssh_config.get("hostname", ssh_host)
        if ssh_hostname != ssh_host:
            print(f"SSH hostname: {ssh_hostname} (from SSH config)")
        
        ssh_port_str = ssh_config.get("port") or server_credentials.get("ssh_port", "22")
        ssh_port = int(ssh_port_str)
        if ssh_config.get("port"):
            print(f"SSH port: {ssh_port} (from SSH config)")
        elif server_credentials.get("ssh_port"):
            print(f"SSH port: {ssh_port} (from credentials)")
        
        # Get SSH username from config or credentials, or prompt
        ssh_username = ssh_config.get("user") or server_credentials.get("ssh_username", "")
        if not ssh_username:
            try:
                ssh_username = input("SSH username:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            source = "SSH config" if ssh_config.get("user") else "credentials"
            print(f"SSH username: {ssh_username} (from {source})")
        
        # Get SQL connection parameters from credentials or prompt
        sql_username = server_credentials.get("sql_username", "")
        if not sql_username:
            try:
                sql_username = input("SQL username:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            print(f"SQL username: {sql_username} (from credentials)")
        
        sql_database = server_credentials.get("sql_database", "")
        if not sql_database:
            try:
                sql_database = input("Database name:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            print(f"Database name: {sql_database} (from credentials)")
        
        sql_port = server_credentials.get("sql_port", "")
        if not sql_port:
            try:
                sql_port = input("SQL remote port:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            print(f"SQL remote port: {sql_port} (from credentials)")
        
        sql_port_local = server_credentials.get("sql_port_local", "")
        if not sql_port_local:
            try:
                sql_port_local = input("SQL local port:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            print(f"SQL local port: {sql_port_local} (from credentials)")
        
        sql_ip = server_credentials.get("sql_ip", "")
        if not sql_ip:
            try:
                sql_ip = input("SQL remote IP:\n").strip()
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
        else:
            print(f"SQL remote IP: {sql_ip} (from credentials)")
    
        # Try SSH key authentication first (preferred method)
        print("Attempting SSH key authentication...")
        server = _try_ssh_connection_with_key(
            ssh_hostname,
            ssh_port,
            ssh_username,
            (sql_ip, int(sql_port)),
            (sql_ip, int(sql_port_local)),
            server_profile,
            ssh_config,
        )
        
        # If key auth failed, fall back to password authentication
        if server is None:
            print("SSH key authentication failed, trying password authentication...")
            # Check for stored SSH password and prompt user
            try:
                ssh_password = _prompt_for_stored_credential("ssh_password", server_profile)
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                raise
            
            if not ssh_password:
                try:
                    ssh_password = getpass("SSH password:\n")
                except KeyboardInterrupt:
                    print("\n\nOperation cancelled by user.")
                    raise
                # Store password in keychain for future use
                stored, error_msg = _set_keychain_password(server_profile, "ssh_password", ssh_password, verbose=True)
                if stored:
                    print("✓ SSH password stored in keychain for future use")
                else:
                    print(f"⚠ Warning: Could not store SSH password in keychain: {error_msg}")
                    print("   You will be prompted next time.")
            
            try:
                print(f"Attempting SSH password authentication to {ssh_hostname}:{ssh_port} as {ssh_username}...")
                server = SSHTunnelForwarder(
                    (ssh_hostname, ssh_port),
                    ssh_username=ssh_username,
                    ssh_password=ssh_password,
                    remote_bind_address=(sql_ip, int(sql_port)),
                    local_bind_address=(sql_ip, int(sql_port_local)),
                )
                server.start()
                
                # Verify tunnel is actually working
                if not server.is_alive:
                    server.stop()
                    raise ConnectionError("SSH tunnel started but is not alive")
                
                print(f"SSH tunnel established successfully on local port {server.local_bind_port}")
                
            except paramiko.AuthenticationException as e:
                raise ConnectionError(f"SSH authentication failed: {e}") from e
            except paramiko.SSHException as e:
                raise ConnectionError(f"SSH error occurred: {e}") from e
            except (socket.error, OSError) as e:
                raise ConnectionError(f"Connection error: {e}") from e
            except Exception as e:
                raise ConnectionError(f"Failed to establish SSH tunnel: {e}") from e
        else:
            print("SSH key authentication successful!")
        
        # Get SQL password from keychain or prompt
        try:
            sql_password = _prompt_for_stored_credential("sql_password", server_profile)
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            if server:
                try:
                    close_connection(None, server)
                except Exception:
                    pass
            raise
        
        if not sql_password:
            try:
                sql_password = getpass("SQL password:\n")
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                if server:
                    try:
                        close_connection(None, server)
                    except Exception:
                        pass
                raise
            # Store password in keychain for future use
            stored, error_msg = _set_keychain_password(server_profile, "sql_password", sql_password, verbose=True)
            if stored:
                print("✓ SQL password stored in keychain for future use")
            else:
                print(f"⚠ Warning: Could not store SQL password in keychain: {error_msg}")
                print("   You will be prompted next time.")
        
        try:
            print(f"Connecting to MySQL database {sql_database} on {sql_ip}:{server.local_bind_port}...")
            connection = mysql.connector.MySQLConnection(
                user=sql_username,
                password=sql_password,
                host=sql_ip,
                port=server.local_bind_port,
                database=sql_database,
            )
            print("MySQL connection established successfully")
            return connection, server
        except mysql.connector.Error as e:
            # Close SSH tunnel if MySQL connection fails
            if server:
                try:
                    close_connection(None, server)
                except Exception:
                    pass
            raise mysql.connector.Error(f"Failed to establish MySQL connection: {e}") from e
    except KeyboardInterrupt:
        # Clean up any connections that were established before Ctrl+C
        print("\n\nOperation cancelled by user. Cleaning up connections...")
        if connection:
            try:
                connection.close()
            except Exception:
                pass
        if server:
            try:
                close_connection(None, server)
            except Exception:
                pass
        print("Connections closed.")
        raise


def close_connection(connection: mysql.connector.MySQLConnection, server: SSHTunnelForwarder) -> None:
    """Close MySQL connection and stop SSH tunnel, ignoring errors.
    
    Args:
        connection: MySQL connection to close
        server: SSH tunnel server to stop
    """
    try:
        if connection:
            connection.close()
            print("MySQL connection closed")
    except Exception as e:
        print(f"Error closing MySQL connection: {e}")
    finally:
        try:
            if server:
                if server.is_alive:
                    server.stop()
                server.close()
                print("SSH tunnel closed")
        except Exception as e:
            # Best-effort shutdown
            print(f"Error closing SSH tunnel: {e}")

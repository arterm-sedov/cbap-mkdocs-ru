"""Comprehensive test suite for SSH utility module (tools/ssh_kb_ru.py)."""

import json
import os
import platform
import socket
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch, mock_open

import pytest

# Handle optional paramiko import
try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False
    # Create a mock paramiko module for testing
    class MockParamiko:
        class AuthenticationException(Exception):
            pass
        class SSHException(Exception):
            pass
        class ssh_exception:
            class PasswordRequiredException(Exception):
                pass
        class RSAKey:
            @staticmethod
            def from_private_key_file(path, password=None):
                raise NotImplementedError
        class Ed25519Key:
            @staticmethod
            def from_private_key_file(path, password=None):
                raise NotImplementedError
        class ECDSAKey:
            @staticmethod
            def from_private_key_file(path, password=None):
                raise NotImplementedError
        class DSSKey:
            @staticmethod
            def from_private_key_file(path, password=None):
                raise NotImplementedError
        class SSHConfig:
            def parse(self, f):
                pass
            def lookup(self, hostname):
                return {}
    
    paramiko = MockParamiko()

# Import the module under test
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools import ssh_kb_ru


class TestSSHKeyDirectory:
    """Test SSH key directory path detection."""
    
    def test_get_ssh_key_directory_windows(self):
        """Test SSH key directory on Windows."""
        with patch("platform.system", return_value="Windows"):
            with patch.dict(os.environ, {"USERPROFILE": "C:\\Users\\test"}):
                result = ssh_kb_ru._get_ssh_key_directory()
                assert str(result) == "C:\\Users\\test\\.ssh"
    
    def test_get_ssh_key_directory_linux(self):
        """Test SSH key directory on Linux."""
        with patch("platform.system", return_value="Linux"):
            with patch("pathlib.Path.home", return_value=Path("/home/test")):
                result = ssh_kb_ru._get_ssh_key_directory()
                # Use Path comparison to handle platform differences
                assert result == Path("/home/test/.ssh")
    
    def test_get_ssh_config_path(self):
        """Test SSH config file path."""
        with patch("tools.ssh_kb_ru._get_ssh_key_directory", return_value=Path("/home/test/.ssh")):
            result = ssh_kb_ru._get_ssh_config_path()
            # Use Path comparison to handle platform differences
            assert result == Path("/home/test/.ssh/config")


class TestKeychainFunctions:
    """Test keychain integration functions."""
    
    def test_get_keychain_key(self):
        """Test keychain key generation."""
        result = ssh_kb_ru._get_keychain_key("test_profile", "ssh_password")
        assert result == "ssh_kb_ru:test_profile:ssh_password"
    
    def test_get_keychain_password_available(self):
        """Test retrieving password from keychain when available."""
        with patch("tools.ssh_kb_ru.KEYRING_AVAILABLE", True):
            with patch("tools.ssh_kb_ru.keyring.get_password", return_value="test_password"):
                result = ssh_kb_ru._get_keychain_password("test_profile", "ssh_password")
                assert result == "test_password"
    
    def test_get_keychain_password_unavailable(self):
        """Test retrieving password when keyring is not available."""
        with patch("tools.ssh_kb_ru.KEYRING_AVAILABLE", False):
            result = ssh_kb_ru._get_keychain_password("test_profile", "ssh_password")
            assert result is None
    
    def test_get_keychain_password_not_found(self):
        """Test retrieving password when not found in keychain."""
        with patch("tools.ssh_kb_ru.KEYRING_AVAILABLE", True):
            with patch("tools.ssh_kb_ru.keyring.get_password", return_value=None):
                result = ssh_kb_ru._get_keychain_password("test_profile", "ssh_password")
                assert result is None
    
    def test_get_keychain_password_exception(self):
        """Test handling keychain exceptions."""
        with patch("tools.ssh_kb_ru.KEYRING_AVAILABLE", True):
            with patch("tools.ssh_kb_ru.keyring.get_password", side_effect=Exception("Keyring error")):
                result = ssh_kb_ru._get_keychain_password("test_profile", "ssh_password")
                assert result is None
    
    def test_set_keychain_password_success(self):
        """Test storing password in keychain."""
        with patch("tools.ssh_kb_ru.KEYRING_AVAILABLE", True):
            with patch("tools.ssh_kb_ru.keyring.set_password", return_value=None):
                result = ssh_kb_ru._set_keychain_password("test_profile", "ssh_password", "test_pass")
                assert result is True
    
    def test_set_keychain_password_unavailable(self):
        """Test storing password when keyring is not available."""
        with patch("tools.ssh_kb_ru.KEYRING_AVAILABLE", False):
            result = ssh_kb_ru._set_keychain_password("test_profile", "ssh_password", "test_pass")
            assert result is False
    
    def test_get_keychain_key_passphrase(self):
        """Test retrieving SSH key passphrase from keychain."""
        with patch("tools.ssh_kb_ru._get_keychain_password", return_value="test_passphrase"):
            result = ssh_kb_ru._get_keychain_key_passphrase("test_profile", "/path/to/key")
            assert result == "test_passphrase"
    
    def test_set_keychain_key_passphrase(self):
        """Test storing SSH key passphrase in keychain."""
        with patch("tools.ssh_kb_ru._set_keychain_password", return_value=True):
            result = ssh_kb_ru._set_keychain_key_passphrase("test_profile", "/path/to/key", "test_passphrase")
            assert result is True


class TestServerProfile:
    """Test server profile extraction."""
    
    def test_get_server_profile_from_path_normal(self):
        """Test extracting profile from normal filename."""
        result = ssh_kb_ru._get_server_profile_from_path("serverCredentials.json")
        assert result == "serverCredentials"
    
    def test_get_server_profile_from_path_dot_prefix(self):
        """Test extracting profile from dot-prefixed filename."""
        result = ssh_kb_ru._get_server_profile_from_path(".serverCredentials.json")
        assert result == "serverCredentials"
    
    def test_get_server_profile_from_path_full_path(self):
        """Test extracting profile from full path."""
        result = ssh_kb_ru._get_server_profile_from_path("/path/to/.serverCredentials.json")
        assert result == "serverCredentials"


class TestLoadServerCredentials:
    """Test loading server credentials from JSON."""
    
    def test_load_server_credentials_success(self, temp_dir):
        """Test loading credentials from valid JSON file."""
        creds_file = temp_dir / "test_creds.json"
        creds_data = {"ssh_host": "test.com", "ssh_port": "22"}
        creds_file.write_text(json.dumps(creds_data))
        
        result = ssh_kb_ru._load_server_credentials(str(creds_file))
        assert result == creds_data
    
    def test_load_server_credentials_file_not_found(self):
        """Test loading credentials when file doesn't exist."""
        result = ssh_kb_ru._load_server_credentials("nonexistent.json")
        assert result == {}
    
    def test_load_server_credentials_invalid_json(self, temp_dir):
        """Test loading credentials from invalid JSON file."""
        creds_file = temp_dir / "invalid.json"
        creds_file.write_text("{invalid json}")
        
        result = ssh_kb_ru._load_server_credentials(str(creds_file))
        assert result == {}
    
    def test_load_server_credentials_empty_file(self, temp_dir):
        """Test loading credentials from empty file."""
        creds_file = temp_dir / "empty.json"
        creds_file.write_text("")
        
        result = ssh_kb_ru._load_server_credentials(str(creds_file))
        assert result == {}
    
    def test_load_server_credentials_env_override(self, temp_dir, monkeypatch):
        """Test credentials path override from environment variable."""
        env_creds_file = temp_dir / "env_creds.json"
        env_creds_data = {"ssh_host": "env.com"}
        env_creds_file.write_text(json.dumps(env_creds_data))
        
        default_creds_file = temp_dir / "default.json"
        default_creds_data = {"ssh_host": "default.com"}
        default_creds_file.write_text(json.dumps(default_creds_data))
        
        monkeypatch.setenv("CREDENTIALS_PATH", str(env_creds_file))
        
        result = ssh_kb_ru._load_server_credentials(str(default_creds_file))
        assert result == env_creds_data


class TestSSHConfigParsing:
    """Test SSH config file parsing."""
    
    def test_parse_ssh_config_success(self, temp_dir):
        """Test parsing valid SSH config file."""
        ssh_dir = temp_dir / ".ssh"
        ssh_dir.mkdir()
        config_file = ssh_dir / "config"
        config_file.write_text("""
Host test.example.com
    HostName test.example.com
    Port 2222
    User testuser
    IdentityFile ~/.ssh/id_rsa_test
""")
        
        with patch("tools.ssh_kb_ru._get_ssh_config_path", return_value=config_file):
            with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", True):
                result = ssh_kb_ru._parse_ssh_config("test.example.com")
                assert result["hostname"] == "test.example.com"
                assert result["port"] == "2222"
                assert result["user"] == "testuser"
                assert "id_rsa_test" in result["identityfile"]
    
    def test_parse_ssh_config_file_not_found(self):
        """Test parsing when SSH config file doesn't exist."""
        with patch("tools.ssh_kb_ru._get_ssh_config_path", return_value=Path("/nonexistent/config")):
            result = ssh_kb_ru._parse_ssh_config("test.example.com")
            assert result == {}
    
    def test_parse_ssh_config_paramiko_unavailable(self):
        """Test parsing when Paramiko is not available."""
        with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", False):
            result = ssh_kb_ru._parse_ssh_config("test.example.com")
            assert result == {}
    
    def test_parse_ssh_config_host_not_found(self, temp_dir):
        """Test parsing when host is not in config."""
        ssh_dir = temp_dir / ".ssh"
        ssh_dir.mkdir()
        config_file = ssh_dir / "config"
        config_file.write_text("Host other.example.com\n    HostName other.example.com\n")
        
        with patch("tools.ssh_kb_ru._get_ssh_config_path", return_value=config_file):
            with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", True):
                result = ssh_kb_ru._parse_ssh_config("test.example.com")
                # Should return empty dict or default values
                assert isinstance(result, dict)
    
    def test_expand_ssh_path_home(self):
        """Test expanding ~ in SSH path."""
        result = ssh_kb_ru._expand_ssh_path("~/.ssh/id_rsa")
        assert "~" not in str(result)
        assert ".ssh" in str(result) or "id_rsa" in str(result)
    
    def test_expand_ssh_path_absolute(self):
        """Test expanding absolute path."""
        result = ssh_kb_ru._expand_ssh_path("/absolute/path/to/key")
        # Use Path comparison to handle platform differences
        assert result == Path("/absolute/path/to/key")


class TestDetectSSHKeys:
    """Test SSH key detection."""
    
    def test_detect_ssh_keys_from_config(self, temp_dir):
        """Test detecting SSH key from SSH config IdentityFile."""
        ssh_dir = temp_dir / ".ssh"
        ssh_dir.mkdir()
        key_file = ssh_dir / "id_rsa_test"
        key_file.write_text("mock key")
        
        ssh_config = {"identityfile": str(key_file)}
        
        result = ssh_kb_ru._detect_ssh_keys("test.example.com", "testuser", ssh_config)
        assert result == str(key_file)
    
    def test_detect_ssh_keys_standard_names(self, temp_dir):
        """Test detecting SSH keys with standard names."""
        ssh_dir = temp_dir / ".ssh"
        ssh_dir.mkdir()
        key_file = ssh_dir / "id_rsa"
        key_file.write_text("mock key")
        
        with patch("tools.ssh_kb_ru._get_ssh_key_directory", return_value=ssh_dir):
            result = ssh_kb_ru._detect_ssh_keys("test.example.com", "testuser", None)
            assert result == str(key_file)
    
    def test_detect_ssh_keys_not_found(self, temp_dir):
        """Test when no SSH keys are found."""
        ssh_dir = temp_dir / ".ssh"
        ssh_dir.mkdir()
        # Don't create any key files
        
        with patch("tools.ssh_kb_ru._get_ssh_key_directory", return_value=ssh_dir):
            result = ssh_kb_ru._detect_ssh_keys("test.example.com", "testuser", None)
            assert result is None
    
    def test_detect_ssh_keys_directory_not_exists(self):
        """Test when SSH directory doesn't exist."""
        with patch("tools.ssh_kb_ru._get_ssh_key_directory", return_value=Path("/nonexistent/.ssh")):
            result = ssh_kb_ru._detect_ssh_keys("test.example.com", "testuser", None)
            assert result is None


class TestPromptWithDefault:
    """Test prompt with default value."""
    
    def test_prompt_with_default_provided(self, monkeypatch):
        """Test prompt when default is provided and user enters value."""
        monkeypatch.setattr("builtins.input", lambda x: "user_input")
        result = ssh_kb_ru._prompt_with_default("Enter value:", "default_value")
        assert result == "user_input"
    
    def test_prompt_with_default_empty_input(self, monkeypatch):
        """Test prompt when user presses Enter (empty input)."""
        monkeypatch.setattr("builtins.input", lambda x: "")
        result = ssh_kb_ru._prompt_with_default("Enter value:", "default_value")
        assert result == "default_value"
    
    def test_prompt_with_default_no_default(self, monkeypatch):
        """Test prompt when no default is provided."""
        monkeypatch.setattr("builtins.input", lambda x: "user_input")
        result = ssh_kb_ru._prompt_with_default("Enter value:", "")
        assert result == "user_input"


class TestLoadSSHKeyWithPassphrase:
    """Test loading SSH keys with passphrase support."""
    
    def test_load_ssh_key_unencrypted(self):
        """Test loading unencrypted SSH key."""
        mock_key = MagicMock()
        
        with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", True):
            with patch("paramiko.RSAKey.from_private_key_file", return_value=mock_key):
                result = ssh_kb_ru._load_ssh_key_with_passphrase("/path/to/key", "test_profile")
                assert result == mock_key
    
    def test_load_ssh_key_encrypted_with_passphrase(self, monkeypatch):
        """Test loading encrypted SSH key with passphrase from keychain."""
        mock_key = MagicMock()
        
        def mock_from_private_key_file(path, password=None):
            if password is None:
                raise paramiko.ssh_exception.PasswordRequiredException("Passphrase required")
            return mock_key
        
        with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", True):
            with patch("paramiko.RSAKey.from_private_key_file", side_effect=mock_from_private_key_file):
                with patch("tools.ssh_kb_ru._get_keychain_key_passphrase", return_value="test_passphrase"):
                    result = ssh_kb_ru._load_ssh_key_with_passphrase("/path/to/key", "test_profile")
                    assert result == mock_key
    
    def test_load_ssh_key_encrypted_prompt_passphrase(self, monkeypatch):
        """Test loading encrypted SSH key prompting for passphrase."""
        mock_key = MagicMock()
        
        def mock_from_private_key_file(path, password=None):
            if password is None:
                raise paramiko.ssh_exception.PasswordRequiredException("Passphrase required")
            if password == "prompted_passphrase":
                return mock_key
            raise ValueError("Wrong passphrase")
        
        with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", True):
            with patch("paramiko.RSAKey.from_private_key_file", side_effect=mock_from_private_key_file):
                with patch("tools.ssh_kb_ru._get_keychain_key_passphrase", return_value=None):
                    with patch("tools.ssh_kb_ru._set_keychain_key_passphrase", return_value=True):
                        with patch("tools.ssh_kb_ru.getpass", return_value="prompted_passphrase"):
                            result = ssh_kb_ru._load_ssh_key_with_passphrase("/path/to/key", "test_profile")
                            assert result == mock_key
    
    def test_load_ssh_key_paramiko_unavailable(self):
        """Test loading key when Paramiko is not available."""
        with patch("tools.ssh_kb_ru.PARAMIKO_AVAILABLE", False):
            result = ssh_kb_ru._load_ssh_key_with_passphrase("/path/to/key", "test_profile")
            assert result is None


class TestTrySSHConnectionWithKey:
    """Test SSH connection attempts with key authentication."""
    
    def test_try_ssh_connection_with_key_success(self, mock_ssh_tunnel):
        """Test successful SSH connection with key."""
        with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_ssh_tunnel):
            with patch("tools.ssh_kb_ru._detect_ssh_keys", return_value="/path/to/key"):
                with patch("tools.ssh_kb_ru._load_ssh_key_with_passphrase", return_value=MagicMock()):
                    result = ssh_kb_ru._try_ssh_connection_with_key(
                        "test.example.com", 22, "testuser",
                        ("127.0.0.1", 3306), ("127.0.0.1", 3307),
                        "test_profile", None
                    )
                    assert result == mock_ssh_tunnel
                    mock_ssh_tunnel.start.assert_called_once()
    
    def test_try_ssh_connection_with_key_auth_failure(self):
        """Test SSH connection failure due to authentication."""
        mock_tunnel = MagicMock()
        mock_tunnel.start.side_effect = paramiko.AuthenticationException("Auth failed")
        
        with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_tunnel):
            with patch("tools.ssh_kb_ru._detect_ssh_keys", return_value="/path/to/key"):
                with patch("tools.ssh_kb_ru._load_ssh_key_with_passphrase", return_value=MagicMock()):
                    result = ssh_kb_ru._try_ssh_connection_with_key(
                        "test.example.com", 22, "testuser",
                        ("127.0.0.1", 3306), ("127.0.0.1", 3307),
                        "test_profile", None
                    )
                    assert result is None
    
    def test_try_ssh_connection_with_key_ssh_exception(self):
        """Test SSH connection failure due to SSH exception."""
        mock_tunnel = MagicMock()
        mock_tunnel.start.side_effect = paramiko.SSHException("SSH error")
        
        with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_tunnel):
            with patch("tools.ssh_kb_ru._detect_ssh_keys", return_value="/path/to/key"):
                with patch("tools.ssh_kb_ru._load_ssh_key_with_passphrase", return_value=MagicMock()):
                    result = ssh_kb_ru._try_ssh_connection_with_key(
                        "test.example.com", 22, "testuser",
                        ("127.0.0.1", 3306), ("127.0.0.1", 3307),
                        "test_profile", None
                    )
                    assert result is None
    
    def test_try_ssh_connection_with_key_socket_error(self):
        """Test SSH connection failure due to socket error."""
        mock_tunnel = MagicMock()
        mock_tunnel.start.side_effect = socket.error("Connection refused")
        
        with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_tunnel):
            with patch("tools.ssh_kb_ru._detect_ssh_keys", return_value="/path/to/key"):
                with patch("tools.ssh_kb_ru._load_ssh_key_with_passphrase", return_value=MagicMock()):
                    result = ssh_kb_ru._try_ssh_connection_with_key(
                        "test.example.com", 22, "testuser",
                        ("127.0.0.1", 3306), ("127.0.0.1", 3307),
                        "test_profile", None
                    )
                    assert result is None
    
    def test_try_ssh_connection_with_key_not_alive(self):
        """Test SSH connection when tunnel is not alive."""
        mock_tunnel = MagicMock()
        mock_tunnel.is_alive = False
        
        with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_tunnel):
            with patch("tools.ssh_kb_ru._detect_ssh_keys", return_value="/path/to/key"):
                with patch("tools.ssh_kb_ru._load_ssh_key_with_passphrase", return_value=MagicMock()):
                    result = ssh_kb_ru._try_ssh_connection_with_key(
                        "test.example.com", 22, "testuser",
                        ("127.0.0.1", 3306), ("127.0.0.1", 3307),
                        "test_profile", None
                    )
                    assert result is None
                    mock_tunnel.stop.assert_called_once()


class TestEstablishConnectionInteractive:
    """Test main connection establishment function."""
    
    def test_establish_connection_key_auth_success(self, credentials_file, mock_ssh_tunnel, mock_mysql_connection):
        """Test successful connection establishment with key authentication."""
        def mock_input(prompt):
            if "username" in prompt.lower():
                return "testuser"
            elif "database" in prompt.lower():
                return "testdb"
            elif "remote port" in prompt.lower():
                return "3306"
            elif "local port" in prompt.lower():
                return "3307"
            else:
                return "127.0.0.1"
        
        with patch("tools.ssh_kb_ru._load_server_credentials", return_value={"ssh_host": "test.example.com"}):
            with patch("tools.ssh_kb_ru._parse_ssh_config", return_value={}):
                with patch("tools.ssh_kb_ru._try_ssh_connection_with_key", return_value=mock_ssh_tunnel):
                    with patch("tools.ssh_kb_ru._get_keychain_password", return_value=None):
                        with patch("tools.ssh_kb_ru._set_keychain_password", return_value=True):
                            with patch("builtins.input", side_effect=mock_input):
                                with patch("tools.ssh_kb_ru.getpass", return_value="sql_password"):
                                    with patch("mysql.connector.MySQLConnection", return_value=mock_mysql_connection):
                                        conn, server = ssh_kb_ru.establish_connection_interactive(credentials_file)
                                        assert conn == mock_mysql_connection
                                        assert server == mock_ssh_tunnel
    
    def test_establish_connection_password_auth_success(self, credentials_file, mock_ssh_tunnel, mock_mysql_connection):
        """Test successful connection establishment with password authentication."""
        def mock_input(prompt):
            if "username" in prompt.lower():
                return "testuser"
            elif "database" in prompt.lower():
                return "testdb"
            elif "remote port" in prompt.lower():
                return "3306"
            elif "local port" in prompt.lower():
                return "3307"
            else:
                return "127.0.0.1"
        
        with patch("tools.ssh_kb_ru._load_server_credentials", return_value={"ssh_host": "test.example.com"}):
            with patch("tools.ssh_kb_ru._parse_ssh_config", return_value={}):
                with patch("tools.ssh_kb_ru._try_ssh_connection_with_key", return_value=None):
                    with patch("tools.ssh_kb_ru._get_keychain_password", return_value=None):
                        with patch("tools.ssh_kb_ru._set_keychain_password", return_value=True):
                            with patch("builtins.input", side_effect=mock_input):
                                with patch("tools.ssh_kb_ru.getpass", return_value="password123"):
                                    with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_ssh_tunnel):
                                        with patch("mysql.connector.MySQLConnection", return_value=mock_mysql_connection):
                                            conn, server = ssh_kb_ru.establish_connection_interactive(credentials_file)
                                            assert conn == mock_mysql_connection
                                            assert server == mock_ssh_tunnel
    
    def test_establish_connection_keychain_passwords(self, credentials_file, mock_ssh_tunnel, mock_mysql_connection):
        """Test connection establishment using passwords from keychain."""
        def mock_input(prompt):
            if "username" in prompt.lower():
                return "testuser"
            elif "database" in prompt.lower():
                return "testdb"
            elif "remote port" in prompt.lower():
                return "3306"
            elif "local port" in prompt.lower():
                return "3307"
            else:
                return "127.0.0.1"
        
        with patch("tools.ssh_kb_ru._load_server_credentials", return_value={"ssh_host": "test.example.com"}):
            with patch("tools.ssh_kb_ru._parse_ssh_config", return_value={}):
                with patch("tools.ssh_kb_ru._try_ssh_connection_with_key", return_value=None):
                    with patch("tools.ssh_kb_ru._get_keychain_password", side_effect=lambda p, t: "keychain_password" if t == "ssh_password" else "keychain_sql_password"):
                        with patch("builtins.input", side_effect=mock_input):
                            with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_ssh_tunnel):
                                with patch("mysql.connector.MySQLConnection", return_value=mock_mysql_connection):
                                    conn, server = ssh_kb_ru.establish_connection_interactive(credentials_file)
                                    assert conn == mock_mysql_connection
                                    assert server == mock_ssh_tunnel
    
    def test_establish_connection_ssh_auth_failure(self, credentials_file):
        """Test connection establishment when SSH authentication fails."""
        def mock_input(prompt):
            if "username" in prompt.lower():
                return "testuser"
            elif "database" in prompt.lower():
                return "testdb"
            elif "remote port" in prompt.lower():
                return "3306"
            elif "local port" in prompt.lower():
                return "3307"
            else:
                return "127.0.0.1"
        
        mock_tunnel = MagicMock()
        mock_tunnel.start.side_effect = paramiko.AuthenticationException("Auth failed")
        
        with patch("tools.ssh_kb_ru._load_server_credentials", return_value={"ssh_host": "test.example.com"}):
            with patch("tools.ssh_kb_ru._parse_ssh_config", return_value={}):
                with patch("tools.ssh_kb_ru._try_ssh_connection_with_key", return_value=None):
                    with patch("tools.ssh_kb_ru._get_keychain_password", return_value=None):
                        with patch("builtins.input", side_effect=mock_input):
                            with patch("tools.ssh_kb_ru.getpass", return_value="wrong_password"):
                                with patch("tools.ssh_kb_ru.SSHTunnelForwarder", return_value=mock_tunnel):
                                    with pytest.raises(ConnectionError):
                                        ssh_kb_ru.establish_connection_interactive(credentials_file)
    
    def test_establish_connection_mysql_failure(self, credentials_file, mock_ssh_tunnel):
        """Test connection establishment when MySQL connection fails."""
        def mock_input(prompt):
            if "username" in prompt.lower():
                return "testuser"
            elif "database" in prompt.lower():
                return "testdb"
            elif "remote port" in prompt.lower():
                return "3306"
            elif "local port" in prompt.lower():
                return "3307"
            else:
                return "127.0.0.1"
        
        import mysql.connector
        
        with patch("tools.ssh_kb_ru._load_server_credentials", return_value={"ssh_host": "test.example.com"}):
            with patch("tools.ssh_kb_ru._parse_ssh_config", return_value={}):
                with patch("tools.ssh_kb_ru._try_ssh_connection_with_key", return_value=mock_ssh_tunnel):
                    with patch("tools.ssh_kb_ru._get_keychain_password", return_value=None):
                        with patch("builtins.input", side_effect=mock_input):
                            with patch("tools.ssh_kb_ru.getpass", return_value="sql_password"):
                                with patch("mysql.connector.MySQLConnection", side_effect=mysql.connector.Error("Connection failed")):
                                    with pytest.raises(mysql.connector.Error):
                                        ssh_kb_ru.establish_connection_interactive(credentials_file)
                                    # Verify tunnel is stopped on MySQL failure
                                    mock_ssh_tunnel.stop.assert_called_once()
    
    def test_establish_connection_ssh_config_integration(self, credentials_file, mock_ssh_tunnel, mock_mysql_connection):
        """Test connection establishment using SSH config values."""
        def mock_input(prompt):
            if "database" in prompt.lower():
                return "testdb"
            elif "remote port" in prompt.lower():
                return "3306"
            elif "local port" in prompt.lower():
                return "3307"
            else:
                return "127.0.0.1"
        
        ssh_config = {
            "hostname": "config.example.com",
            "port": "2222",
            "user": "configuser",
            "identityfile": "~/.ssh/id_rsa_config"
        }
        
        with patch("tools.ssh_kb_ru._load_server_credentials", return_value={"ssh_host": "test.example.com"}):
            with patch("tools.ssh_kb_ru._parse_ssh_config", return_value=ssh_config):
                with patch("tools.ssh_kb_ru._try_ssh_connection_with_key", return_value=mock_ssh_tunnel) as mock_try:
                    with patch("tools.ssh_kb_ru._get_keychain_password", return_value=None):
                        with patch("tools.ssh_kb_ru._set_keychain_password", return_value=True):
                            with patch("builtins.input", side_effect=mock_input):
                                with patch("tools.ssh_kb_ru.getpass", return_value="sql_password"):
                                    with patch("mysql.connector.MySQLConnection", return_value=mock_mysql_connection):
                                        conn, server = ssh_kb_ru.establish_connection_interactive(credentials_file)
                                        # Verify SSH config values were used
                                        mock_try.assert_called_once()
                                        call_args = mock_try.call_args
                                        assert call_args[0][0] == "config.example.com"  # hostname from config
                                        assert call_args[0][1] == 2222  # port from config


class TestCloseConnection:
    """Test connection closing function."""
    
    def test_close_connection_success(self, mock_mysql_connection, mock_ssh_tunnel):
        """Test successful connection closure."""
        ssh_kb_ru.close_connection(mock_mysql_connection, mock_ssh_tunnel)
        mock_mysql_connection.close.assert_called_once()
        mock_ssh_tunnel.stop.assert_called_once()
        mock_ssh_tunnel.close.assert_called_once()
    
    def test_close_connection_mysql_error(self, mock_ssh_tunnel):
        """Test connection closure when MySQL close fails."""
        mock_conn = MagicMock()
        mock_conn.close.side_effect = Exception("MySQL close error")
        
        # Should not raise, just log error
        ssh_kb_ru.close_connection(mock_conn, mock_ssh_tunnel)
        mock_ssh_tunnel.stop.assert_called_once()
    
    def test_close_connection_ssh_error(self, mock_mysql_connection):
        """Test connection closure when SSH tunnel close fails."""
        mock_tunnel = MagicMock()
        mock_tunnel.is_alive = True
        mock_tunnel.stop.side_effect = Exception("SSH close error")
        mock_tunnel.close.side_effect = Exception("SSH close error")
        
        # Should not raise, just log error
        ssh_kb_ru.close_connection(mock_mysql_connection, mock_tunnel)
        mock_mysql_connection.close.assert_called_once()
    
    def test_close_connection_tunnel_not_alive(self, mock_mysql_connection):
        """Test connection closure when tunnel is not alive."""
        mock_tunnel = MagicMock()
        mock_tunnel.is_alive = False
        
        ssh_kb_ru.close_connection(mock_mysql_connection, mock_tunnel)
        mock_mysql_connection.close.assert_called_once()
        # Should not call stop if not alive
        mock_tunnel.stop.assert_not_called()
        mock_tunnel.close.assert_called_once()

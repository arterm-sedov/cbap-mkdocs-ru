# Testing Real Connections Guide

This guide explains how to test real SSH and MySQL connections to CMW Lab and Comindware servers.

## Quick Start

### Test Both Servers

```bash
# Activate virtual environment (if using one)
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac

# Run connection tests
python .tests/test_real_connections.py
```

### Test Specific Server

```bash
# Test CMW Lab server
python .tests/test_real_connections.py --server cmw_lab

# Test Comindware server
python .tests/test_real_connections.py --server comindware
```

## What Gets Tested

The `test_real_connections.py` script performs the following checks:

### 1. SSH Tunnel Establishment
- ✅ Attempts SSH key authentication first (from `~/.ssh/` or `%USERPROFILE%\.ssh\`)
- ✅ Falls back to password authentication if keys fail
- ✅ Verifies tunnel is alive and working
- ✅ Shows local bind port for MySQL connection

### 2. MySQL Connection Through Tunnel
- ✅ Connects to MySQL database through SSH tunnel
- ✅ Retrieves database name
- ✅ Checks MySQL version
- ✅ Counts available tables
- ✅ Verifies `phpkb_articles` table exists and is accessible
- ✅ Verifies `phpkb_categories` table exists and is accessible

### 3. Connection Cleanup
- ✅ Properly closes MySQL connection
- ✅ Properly shuts down SSH tunnel

## Credentials Configuration

Credentials are now stored in the `.env` file using environment variables with server profile prefixes.

### Server Profiles

| Server | Profile | Environment Variables Prefix |
|--------|--------|----------------------------|
| CMW Lab | `cmwlab` | `CMWLAB_` |
| Comindware | `cmw` | `CMW_` |

### .env File Format

Set `SERVER_PROFILE` in `.env` to select the default server profile, or pass it as an argument:

```bash
# Default server profile (used when no profile is specified)
SERVER_PROFILE=cmw

# Comindware Server Credentials
CMW_SSH_HOST=31.135.15.59
CMW_SSH_PORT=8223
CMW_SSH_USERNAME=ased
CMW_SSH_PASSWORD=
CMW_SQL_HOSTNAME=localhost
CMW_SQL_IP=127.0.0.1
CMW_SQL_PORT=3306
CMW_SQL_PORT_LOCAL=3307
CMW_SQL_USERNAME=ased
CMW_SQL_PASSWORD=
CMW_SQL_DATABASE=phpkbv9

# CMW Lab Server Credentials
CMWLAB_SSH_HOST=kb.cmwlab.com
CMWLAB_SSH_PORT=22
CMWLAB_SSH_USERNAME=ased
CMWLAB_SSH_PASSWORD=
CMWLAB_SQL_HOSTNAME=localhost
CMWLAB_SQL_IP=127.0.0.1
CMWLAB_SQL_PORT=3306
CMWLAB_SQL_PORT_LOCAL=3307
CMWLAB_SQL_USERNAME=ased
CMWLAB_SQL_PASSWORD=
CMWLAB_SQL_DATABASE=phpkbcmwlab
```

**Note**: 
- Passwords can be left empty (will prompt if needed)
- If credentials are not found in `.env`, the script will prompt you interactively for all connection details
- Legacy JSON files (`.serverCredentials.json`, `.serverCredentialsCmwlab.json`) are still supported for backward compatibility

## Authentication Methods

The SSH utility supports multiple authentication methods (in order of preference):

1. **SSH Key Authentication** (preferred)
   - Uses keys from `~/.ssh/` (Linux/Mac) or `%USERPROFILE%\.ssh\` (Windows)
   - Checks SSH config file (`~/.ssh/config`) for host-specific settings
   - Supports encrypted keys with passphrases (stored in keychain)

2. **Password Authentication** (fallback)
   - Prompts for SSH password if key auth fails
   - Stores password in OS keychain for future use

3. **MySQL Password**
   - Prompts for MySQL password
   - Stores password in OS keychain for future use

## Testing Import Scripts Directly

You can also test the actual import scripts:

### Test CMW Lab Import

```bash
python phpkb_import_cmw_lab.py
```

This will:
1. Prompt for import path (default: `phpkb_content_cmw_lab`)
2. Establish connection using `cmwlab` server profile from `.env`
3. Show root categories
4. Allow you to browse and import categories/articles

### Test Comindware Import

```bash
python phpkb_import.py
```

This will:
1. Prompt for import path (default: `phpkb_content`)
2. Establish connection using `cmw` server profile from `.env` (or SERVER_PROFILE env var)
3. Show root categories
4. Allow you to browse and import categories/articles

## Troubleshooting

### Connection Fails with "Authentication failed"

**Possible causes:**
- SSH keys are not in the expected location
- SSH key passphrase is incorrect
- SSH password is incorrect
- Server credentials are wrong

**Solutions:**
1. Check SSH key location: `~/.ssh/id_rsa` or `~/.ssh/id_ed25519`
2. Verify SSH config: `~/.ssh/config` (if using)
3. Try password authentication (will prompt if key auth fails)
4. Check `.env` file values for the correct server profile prefix (CMW_ or CMWLAB_)

### Connection Fails with "Connection refused"

**Possible causes:**
- Server is not accessible from your network
- SSH port is incorrect
- Firewall blocking connection

**Solutions:**
1. Verify server hostname/IP is correct
2. Check SSH port (default: 22)
3. Test SSH connection manually: `ssh username@hostname -p port`
4. Check network/firewall settings

### MySQL Connection Fails

**Possible causes:**
- SSH tunnel not established properly
- MySQL credentials incorrect
- Database name incorrect
- MySQL port incorrect

**Solutions:**
1. Verify SSH tunnel was established (check output)
2. Check MySQL username/password
3. Verify database name exists
4. Check SQL port settings in credentials file

### "Tunnel is not alive" Error

**Possible causes:**
- SSH connection dropped
- Network interruption
- Server closed connection

**Solutions:**
1. Check network connectivity
2. Verify server is accessible
3. Try reconnecting
4. Check server logs for connection issues

## Keychain Integration

Passwords are automatically stored in your OS keychain:

- **Windows**: Windows Credential Manager
- **Linux**: Secret Service API (GNOME Keyring, KWallet, etc.)
- **macOS**: Keychain Access

To view stored passwords:
- **Windows**: Control Panel → Credential Manager
- **Linux**: Use `secret-tool` or keyring GUI
- **macOS**: Keychain Access app

To remove stored passwords, delete them from the keychain or use keyring CLI tools.

## SSH Config File Support

If you have an SSH config file (`~/.ssh/config`), the utility will automatically use:

- `HostName` - Overrides SSH hostname
- `Port` - Overrides SSH port
- `User` - Overrides SSH username
- `IdentityFile` - Specifies SSH key to use

Example SSH config:

```
Host cmw-lab
    HostName cmw-lab.example.com
    Port 2222
    User myuser
    IdentityFile ~/.ssh/id_rsa_cmw_lab
```

Then use `cmw-lab` as the hostname in your credentials file.

## Example Test Session

```bash
$ python .tests/test_real_connections.py --server cmw_lab

============================================================
Real Connection Test Suite
============================================================

This script will test actual SSH and MySQL connections.
You will be prompted for credentials if not stored in keychain.

⚠️  Note: This requires:
   - Network access to the servers
   - Valid SSH keys or passwords
   - Valid MySQL credentials
============================================================

============================================================
Testing connection to CMW Lab Server
Server profile: cmwlab
============================================================

Step 1: Establishing SSH tunnel and MySQL connection...
Attempting SSH key authentication...
Using SSH key: C:\Users\user\.ssh\id_rsa
SSH tunnel established successfully on local port 3307
✅ SSH tunnel established successfully
   Local bind port: 3307
   Tunnel is alive: True

Step 2: Testing MySQL connection...
✅ Connected to MySQL database: phpkb_cmw_lab
✅ MySQL version: 8.0.35
✅ Found 45 tables in database
✅ phpkb_articles table exists with 1234 articles
✅ phpkb_categories table exists with 56 categories

✅ SUCCESS: All connection tests passed for CMW Lab Server

Step 3: Closing connections...
MySQL connection closed
SSH tunnel closed
✅ Connections closed successfully

============================================================
Test Summary
============================================================
CMW Lab: ✅ PASSED
============================================================

✅ All connection tests passed!
```

## Next Steps

After verifying connections work:

1. **Run import scripts** to import data from servers
2. **Check imported data** in the output directories
3. **Verify article counts** match expectations
4. **Test import scripts** with real data

## See Also

- [README.md](README.md) - Unit test suite documentation
- `tools/ssh_kb_ru.py` - SSH utility module source code
- `phpkb_import_cmw_lab.py` - CMW Lab import script
- `phpkb_import.py` - Comindware import script

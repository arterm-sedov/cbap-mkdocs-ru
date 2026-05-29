# SSH Utility Module Test Suite

Comprehensive test suite for the SSH utility module (`tools/ssh_kb_ru.py`).

## Overview

This test suite provides comprehensive coverage of the SSH utility module, including:

- **SSH Key Directory Detection**: Cross-platform path detection (Windows/Linux)
- **Keychain Integration**: Password and passphrase storage/retrieval
- **Server Credentials Loading**: JSON file parsing with .env override support
- **SSH Config Parsing**: ~/.ssh/config file parsing and integration
- **SSH Key Detection**: Automatic key discovery with config support
- **Key Authentication**: Key-based SSH connection attempts
- **Password Authentication**: Fallback password authentication
- **Encrypted Key Support**: Passphrase handling for encrypted SSH keys
- **Connection Establishment**: Full connection flow with validation
- **Error Handling**: Specific exception handling and error messages
- **Connection Cleanup**: Proper resource cleanup

## Test Structure

```
.tests/
├── __init__.py          # Test package initialization
├── conftest.py          # Pytest fixtures and configuration
├── test_ssh_kb_ru.py    # Main test suite
├── pytest.ini          # Pytest configuration
├── requirements.txt     # Test dependencies
└── README.md            # This file
```

## Test Classes

### TestSSHKeyDirectory
Tests for SSH key directory path detection on different platforms.

### TestKeychainFunctions
Tests for OS keychain integration (password storage/retrieval).

### TestServerProfile
Tests for server profile extraction from file paths.

### TestLoadServerCredentials
Tests for loading credentials from JSON files with .env override.

### TestSSHConfigParsing
Tests for parsing SSH config files (~/.ssh/config).

### TestDetectSSHKeys
Tests for automatic SSH key detection.

### TestPromptWithDefault
Tests for user input prompts with defaults.

### TestLoadSSHKeyWithPassphrase
Tests for loading encrypted SSH keys with passphrase support.

### TestTrySSHConnectionWithKey
Tests for SSH connection attempts with key authentication.

### TestEstablishConnectionInteractive
Tests for the main connection establishment function.

### TestCloseConnection
Tests for proper connection cleanup.

## Running Tests

### Install Test Dependencies

```bash
pip install -r .tests/requirements.txt
```

Or install from the main requirements file (if test dependencies are included):

```bash
pip install -r install/requirements.txt pytest pytest-cov pytest-mock
```

### Run All Tests

```bash
pytest .tests/
```

### Run with Verbose Output

```bash
pytest .tests/ -v
```

### Run Specific Test Class

```bash
pytest .tests/test_ssh_kb_ru.py::TestEstablishConnectionInteractive
```

### Run Specific Test

```bash
pytest .tests/test_ssh_kb_ru.py::TestEstablishConnectionInteractive::test_establish_connection_key_auth_success
```

### Run with Coverage

```bash
pytest .tests/ --cov=tools.ssh_kb_ru --cov-report=html
```

### Run Tests Matching Pattern

```bash
pytest .tests/ -k "keychain"
```

## Test Coverage

The test suite aims for comprehensive coverage including:

- ✅ All public and private functions
- ✅ Success paths and error paths
- ✅ Edge cases (missing files, invalid data, etc.)
- ✅ Cross-platform behavior
- ✅ Integration between components
- ✅ Mocking of external dependencies (SSH, MySQL, keychain)

## Mocking Strategy

Tests use extensive mocking to avoid actual network connections:

- **SSH Connections**: Mocked `SSHTunnelForwarder` instances
- **MySQL Connections**: Mocked `mysql.connector.MySQLConnection`
- **Keychain**: Mocked `keyring` module
- **File System**: Temporary directories via pytest fixtures
- **User Input**: Mocked `input()` and `getpass.getpass()`
- **SSH Config**: Mocked `paramiko.SSHConfig` parsing

## Notes

- All tests are designed to run without actual SSH or MySQL connections
- Tests use temporary directories for file operations
- Mock objects simulate real behavior including exceptions
- Tests verify both success and failure scenarios
- Error handling is tested with specific exception types

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions
- name: Run SSH utility tests
  run: |
    pip install -r .tests/requirements.txt
    pytest .tests/ -v --cov=tools.ssh_kb_ru
```

## Testing Real Connections

To test actual SSH and MySQL connections to the CMW Lab and Comindware servers, use the `test_real_connections.py` script:

### Test Both Servers

```bash
python .tests/test_real_connections.py
```

or

```bash
python .tests/test_real_connections.py --server both
```

### Test Specific Server

```bash
# Test CMW Lab server only
python .tests/test_real_connections.py --server cmw_lab

# Test Comindware server only
python .tests/test_real_connections.py --server comindware
```

### What It Tests

The real connection test script verifies:

1. **SSH Tunnel Establishment**
   - SSH key authentication (if keys are available)
   - Password authentication (if keys fail)
   - Tunnel health check

2. **MySQL Connection**
   - Connection through SSH tunnel
   - Database name retrieval
   - MySQL version check
   - Table count verification
   - phpkb_articles table access
   - phpkb_categories table access

3. **Connection Cleanup**
   - Proper closure of MySQL connection
   - Proper shutdown of SSH tunnel

### Credentials Configuration

Credentials are stored in the `.env` file using server profiles:

- **CMW Lab**: Server profile `cmwlab` (uses `CMWLAB_` prefix in `.env`)
- **Comindware**: Server profile `cmw` (uses `CMW_` prefix in `.env`)

Set `SERVER_PROFILE` in `.env` to select the default server profile, or pass it as an argument to scripts.

If credentials are not found in `.env`, the script will prompt you for all connection details interactively.

**Legacy support**: JSON files (`.serverCredentials.json`, `.serverCredentialsCmwlab.json`) are still supported for backward compatibility.

### Example Output

```
============================================================
Testing connection to CMW Lab Server
Server profile: cmwlab
============================================================

Step 1: Establishing SSH tunnel and MySQL connection...
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
✅ Connections closed successfully
```

### Troubleshooting

If connection tests fail:

1. **SSH Key Issues**: Ensure your SSH keys are in `~/.ssh/` (Linux) or `%USERPROFILE%\.ssh\` (Windows)
2. **Keychain**: Passwords stored in keychain will be used automatically
3. **Network Access**: Ensure you have network access to the servers
4. **Credentials**: Check that credentials files exist or be ready to enter them interactively
5. **SSH Config**: If using SSH config (`~/.ssh/config`), ensure it's properly configured

## Contributing

When adding new features to `tools/ssh_kb_ru.py`:

1. Add corresponding tests in `test_ssh_kb_ru.py`
2. Ensure tests cover both success and failure paths
3. Add appropriate fixtures in `conftest.py` if needed
4. Run tests before committing: `pytest .tests/ -v`
5. Maintain or improve test coverage
6. Test real connections using `test_real_connections.py` before deploying

# Keyring Support on Headless Linux

## Overview

The SSH utility module (`tools/ssh_kb_ru.py`) supports password storage on headless Linux systems (servers without GUI or D-Bus) using a file-based keyring backend.

## How It Works

### Automatic Backend Selection

The module automatically selects the appropriate keyring backend:

1. **First attempt**: Uses the default system keyring backend
   - **Linux with GUI**: GNOME Keyring or KWallet (via D-Bus)
   - **Windows**: Credential Manager
   - **macOS**: Keychain Access

2. **Fallback (headless Linux)**: If the default backend fails (no D-Bus available), it automatically falls back to a file-based backend
   - Stores passwords encrypted in `~/.local/share/python_keyring/`
   - Works without D-Bus or GUI
   - No additional configuration needed

### File-Based Keyring Storage

When running on headless Linux:

- **Location**: `~/.local/share/python_keyring/keyring_pass.cfg`
- **Encryption**: Uses encrypted storage (EncryptedKeyring) when available
- **Fallback**: Uses plaintext storage (PlaintextKeyring) if encryption libraries are not available
- **Permissions**: File is created with user-only read/write permissions (600)

## Usage

No special configuration is needed. The module automatically detects the environment and uses the appropriate backend:

```python
from tools.ssh_kb_ru import establish_connection_interactive

# On headless Linux, this will automatically use file-based keyring
connection, server = establish_connection_interactive(".serverCredentials.json")
```

## Security Considerations

### Encrypted File Backend (Recommended)

If `cryptography` library is available, passwords are stored encrypted:
- Master password is derived from the user's environment
- Passwords are encrypted before storage
- File permissions are restricted to the user

### Plaintext File Backend (Fallback)

If encryption is not available:
- Passwords are stored in plaintext
- File permissions are restricted to the user (600)
- **Warning**: Less secure than encrypted storage

### Recommendations

1. **Install cryptography**: Ensure `cryptography` package is installed for encrypted storage
   ```bash
   pip install cryptography
   ```

2. **File permissions**: The keyring file should have 600 permissions (user-only access)
   - Automatically set by the keyring library
   - Verify with: `ls -l ~/.local/share/python_keyring/`

3. **Backup**: If backing up the keyring file, ensure it's encrypted in transit

## Testing on Headless Linux

To verify keyring works on your headless Linux system:

```bash
# Test connection (will prompt for passwords first time)
python .tests/test_real_connections.py --server cmw_lab

# On subsequent runs, passwords should be retrieved from keyring
# without prompting
```

## Troubleshooting

### Keyring Not Working

**Symptoms**: Passwords are always prompted, never stored

**Possible causes**:
1. Keyring package not installed: `pip install keyring`
2. File permissions issue: Check `~/.local/share/python_keyring/` permissions
3. Disk space: Ensure there's space in home directory

**Solution**:
```bash
# Reinstall keyring
pip install --upgrade keyring

# Check file permissions
ls -la ~/.local/share/python_keyring/
```

### Encryption Not Available

**Symptoms**: Warning about plaintext storage

**Solution**:
```bash
# Install cryptography for encrypted storage
pip install cryptography
```

### Keyring File Location

The keyring file is stored at:
```
~/.local/share/python_keyring/keyring_pass.cfg
```

To view stored credentials (if using plaintext backend):
```bash
cat ~/.local/share/python_keyring/keyring_pass.cfg
```

**Note**: If using encrypted backend, the file will be encrypted and not human-readable.

## Comparison: GUI vs Headless Linux

| Feature | Linux with GUI | Headless Linux |
|---------|---------------|----------------|
| Backend | GNOME Keyring / KWallet | File-based |
| Requires D-Bus | Yes | No |
| Storage Location | System keyring | `~/.local/share/python_keyring/` |
| Encryption | System-managed | EncryptedKeyring (if available) |
| GUI Required | Yes | No |
| Works on Servers | No | Yes |

## Implementation Details

The module handles headless Linux by:

1. **Detection**: Catches `RuntimeError`, `NoKeyringError`, or `InitError` when initializing default backend
2. **Fallback**: Automatically switches to file-based backend
3. **Transparency**: Same API - no code changes needed in scripts using the module

### Code Flow

```python
try:
    # Try default backend (GNOME Keyring, etc.)
    keyring.get_keyring()
except (RuntimeError, NoKeyringError, InitError):
    # Fall back to file backend for headless Linux
    import keyring.backends.file
    file_keyring = keyring.backends.file.EncryptedKeyring()
    keyring.set_keyring(file_keyring)
```

## See Also

- [keyring documentation](https://keyring.readthedocs.io/)
- [keyring file backend](https://keyring.readthedocs.io/en/latest/#file-keyring-backend)
- `tools/ssh_kb_ru.py` - SSH utility module source code

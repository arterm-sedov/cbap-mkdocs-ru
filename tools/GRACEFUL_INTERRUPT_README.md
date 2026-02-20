# Graceful Interrupt Handling Utility

Shared utility module for handling `KeyboardInterrupt` (Ctrl+C) gracefully across all `phpkb*.py` scripts.

## Features

- **Safe input functions**: Handle Ctrl+C gracefully during user input
- **Connection cleanup**: Ensure SSH tunnels and MySQL connections are properly closed on interrupt
- **Consistent error messages**: Standardized user-facing messages when operations are cancelled

## Usage

### Basic Pattern

Replace all `input()` calls with `safe_input()` and wrap your main function in a try-finally block:

```python
from tools.graceful_interrupt import safe_input, ensure_cleanup
from tools.ssh_kb_ru import establish_connection_interactive

def main():
    connection = None
    server = None
    
    try:
        connection, server = establish_connection_interactive()
        
        # Use safe_input instead of input()
        choice = safe_input('Do something? Y/N').lower()
        
        if choice == 'y':
            value = safe_input('Enter a value')
            # ... your code ...
            
    except KeyboardInterrupt:
        # Optional: add any cleanup logic here
        pass
    finally:
        # Always ensure connections are closed
        ensure_cleanup(connection, server)
```

### Available Functions

#### `safe_input(prompt, default=None)`

Safely prompt for user input with graceful Ctrl+C handling.

**Parameters:**
- `prompt` (str): Prompt text to display
- `default` (str, optional): Default value (shown in prompt)

**Returns:**
- User input string

**Raises:**
- `KeyboardInterrupt`: If user presses Ctrl+C (with clean message)

**Example:**
```python
name = safe_input('Enter your name')
age = safe_input('Enter your age', default='18')
```

#### `safe_getpass(prompt)`

Safely prompt for password with graceful Ctrl+C handling.

**Parameters:**
- `prompt` (str): Prompt text to display

**Returns:**
- Password string

**Raises:**
- `KeyboardInterrupt`: If user presses Ctrl+C (with clean message)

**Example:**
```python
password = safe_getpass('Enter password')
```

#### `ensure_cleanup(connection, server)`

Ensure connections are closed on KeyboardInterrupt or normal exit.

**Parameters:**
- `connection` (mysql.connector.MySQLConnection, optional): MySQL connection
- `server` (SSHTunnelForwarder, optional): SSH tunnel server

**Example:**
```python
try:
    connection, server = establish_connection_interactive()
    # ... your code ...
finally:
    ensure_cleanup(connection, server)
```

### Decorator Pattern (Alternative)

For simpler scripts, you can use the decorator:

```python
from tools.graceful_interrupt import graceful_main, ensure_cleanup
from tools.ssh_kb_ru import establish_connection_interactive

CONNECTION = None
server = None

@graceful_main(cleanup_func=lambda: ensure_cleanup(CONNECTION, server))
def main():
    global CONNECTION, server
    CONNECTION, server = establish_connection_interactive()
    
    choice = safe_input('Do something? Y/N').lower()
    # ... your code ...

if __name__ == '__main__':
    main()
```

## Migration Guide

To migrate an existing script:

1. **Add imports:**
   ```python
   from tools.graceful_interrupt import safe_input, ensure_cleanup
   ```

2. **Replace all `input()` calls:**
   ```python
   # Before:
   choice = input('Enter choice: ')
   
   # After:
   choice = safe_input('Enter choice: ')
   ```

3. **Wrap main function in try-finally:**
   ```python
   # Before:
   def main():
       connection, server = establish_connection_interactive()
       # ... code ...
       close_connection(connection, server)
   
   # After:
   def main():
       connection = None
       server = None
       try:
           connection, server = establish_connection_interactive()
           # ... code ...
       except KeyboardInterrupt:
           pass
       finally:
           ensure_cleanup(connection, server)
   ```

## Examples

See `phpkb_update_articles.py` and `phpkb_import_cmw_lab.py` for complete examples.

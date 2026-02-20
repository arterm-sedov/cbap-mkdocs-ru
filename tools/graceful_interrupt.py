"""Shared utility for graceful KeyboardInterrupt (Ctrl+C) handling across phpkb scripts.

Provides:
- Safe input functions that handle Ctrl+C gracefully
- Context manager for connection cleanup
- Decorator for main functions
"""

import sys
from contextlib import contextmanager
from functools import wraps
from typing import Callable, Optional, Tuple, Any

from tools.ssh_kb_ru import close_connection
from sshtunnel import SSHTunnelForwarder
import mysql.connector


def safe_input(prompt: str, default: Optional[str] = None) -> str:
    """Safely prompt for user input with graceful Ctrl+C handling.
    
    Args:
        prompt: Prompt text to display
        default: Optional default value (shown in prompt)
    
    Returns:
        User input string
    
    Raises:
        KeyboardInterrupt: If user presses Ctrl+C (with clean message)
    """
    try:
        if default:
            user_input = input(f"{prompt} (default: {default}):\n").strip()
            return user_input if user_input else default
        else:
            return input(f"{prompt}\n").strip()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        raise


def safe_getpass(prompt: str) -> str:
    """Safely prompt for password with graceful Ctrl+C handling.
    
    Args:
        prompt: Prompt text to display
    
    Returns:
        Password string
    
    Raises:
        KeyboardInterrupt: If user presses Ctrl+C (with clean message)
    """
    from getpass import getpass
    try:
        return getpass(f"{prompt}\n")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        raise


def ensure_cleanup(connection: Optional[mysql.connector.MySQLConnection] = None,
                    server: Optional[SSHTunnelForwarder] = None):
    """Ensure connections are closed on KeyboardInterrupt or normal exit.
    
    This is a helper function to be used in try-finally blocks.
    
    Usage:
        try:
            connection, server = establish_connection_interactive()
            # Your code here
        finally:
            ensure_cleanup(connection, server)
    
    Args:
        connection: MySQL connection (optional)
        server: SSH tunnel server (optional)
    """
    if connection or server:
        try:
            close_connection(connection, server)
        except Exception:
            pass


def graceful_main(cleanup_func: Optional[Callable] = None):
    """Decorator for main functions to handle Ctrl+C gracefully.
    
    Usage:
        @graceful_main(cleanup_func=lambda: close_connection(CONNECTION, server))
        def main():
            # Your main function code
            pass
    
    Or without cleanup:
        @graceful_main()
        def main():
            # Your main function code
            pass
    
    Args:
        cleanup_func: Optional function to call for cleanup (receives no args)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                if cleanup_func:
                    try:
                        cleanup_func()
                    except Exception:
                        pass
                sys.exit(0)
        return wrapper
    return decorator


def handle_keyboard_interrupt(func: Callable) -> Callable:
    """Simple decorator to catch and handle KeyboardInterrupt gracefully.
    
    Usage:
        @handle_keyboard_interrupt
        def my_function():
            # Your code
            pass
    
    Args:
        func: Function to wrap
    
    Returns:
        Wrapped function that handles KeyboardInterrupt
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            raise
    return wrapper

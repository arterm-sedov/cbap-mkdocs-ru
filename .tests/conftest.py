"""Pytest configuration and shared fixtures."""

import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import pytest

# Mock keyring before importing ssh_kb_ru
mock_keyring_module = MagicMock()
mock_keyring_module.get_password = Mock(return_value=None)
mock_keyring_module.set_password = Mock(return_value=None)
sys.modules['keyring'] = mock_keyring_module


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for test files."""
    return tmp_path


@pytest.fixture
def mock_server_credentials():
    """Sample server credentials dictionary."""
    return {
        "ssh_host": "test.example.com",
        "ssh_port": "22",
        "ssh_username": "testuser",
        "sql_hostname": "localhost",
        "sql_username": "dbuser",
        "sql_database": "testdb",
        "sql_port": "3306",
        "sql_port_local": "3307",
        "sql_ip": "127.0.0.1",
    }


@pytest.fixture
def credentials_file(temp_dir, mock_server_credentials):
    """Create a temporary credentials JSON file."""
    creds_file = temp_dir / ".serverCredentials.json"
    with open(creds_file, "w") as f:
        json.dump(mock_server_credentials, f)
    return str(creds_file)


@pytest.fixture
def empty_credentials_file(temp_dir):
    """Create an empty credentials JSON file."""
    creds_file = temp_dir / ".serverCredentials.json"
    creds_file.write_text("{}")
    return str(creds_file)


@pytest.fixture
def mock_ssh_config():
    """Sample SSH config content."""
    return """
Host test.example.com
    HostName test.example.com
    Port 22
    User testuser
    IdentityFile ~/.ssh/id_rsa_test
"""


@pytest.fixture
def ssh_config_file(temp_dir, mock_ssh_config):
    """Create a temporary SSH config file."""
    ssh_dir = temp_dir / ".ssh"
    ssh_dir.mkdir()
    config_file = ssh_dir / "config"
    config_file.write_text(mock_ssh_config)
    return str(config_file)


@pytest.fixture
def mock_ssh_key_file(temp_dir):
    """Create a mock SSH key file."""
    ssh_dir = temp_dir / ".ssh"
    ssh_dir.mkdir()
    key_file = ssh_dir / "id_rsa"
    key_file.write_text("-----BEGIN RSA PRIVATE KEY-----\nMOCK_KEY\n-----END RSA PRIVATE KEY-----")
    return str(key_file)


@pytest.fixture
def mock_ssh_tunnel():
    """Mock SSHTunnelForwarder instance."""
    mock_tunnel = MagicMock()
    mock_tunnel.is_alive = True
    mock_tunnel.local_bind_port = 3307
    mock_tunnel.start = Mock()
    mock_tunnel.stop = Mock()
    mock_tunnel.close = Mock()
    return mock_tunnel


@pytest.fixture
def mock_mysql_connection():
    """Mock MySQL connection."""
    mock_conn = MagicMock()
    mock_conn.close = Mock()
    return mock_conn


@pytest.fixture(autouse=True)
def mock_keyring():
    """Mock keyring module - provides access to the mocked keyring."""
    yield mock_keyring_module


@pytest.fixture(autouse=True)
def mock_dotenv():
    """Mock dotenv module."""
    with patch("tools.ssh_kb_ru.load_dotenv", create=True) as mock_dotenv:
        yield mock_dotenv

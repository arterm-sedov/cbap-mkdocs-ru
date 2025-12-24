import json
from getpass import getpass
from typing import Tuple

import mysql.connector

# Compatibility shim for Paramiko>=3 where DSSKey (DSA) was removed.
# Some versions of sshtunnel still reference paramiko.DSSKey during key discovery.
try:
    import paramiko  # type: ignore
    if not hasattr(paramiko, "DSSKey"):
        # Alias to RSAKey to satisfy attribute access; password auth will ignore it.
        paramiko.DSSKey = paramiko.RSAKey  # type: ignore[attr-defined]
except Exception:
    # Best-effort: if paramiko is not installed, sshtunnel import will raise later.
    pass

from sshtunnel import SSHTunnelForwarder


def _load_server_credentials(credentials_path: str = ".serverCredentials.json") -> dict:
    """Load server credentials JSON. Returns empty dict if file is empty.

    This mirrors the existing behavior in the scripts that read the same file.
    """
    with open(credentials_path, "r") as server_credentials_file:
        content = server_credentials_file.read()
        return json.loads(content) if content else {}


def _prompt_with_default(prompt: str, default_value: str) -> str:
    """Prompt the user, falling back to a provided default if available."""
    return default_value or input(prompt)


def establish_connection_interactive(credentials_path: str = ".serverCredentials.json") -> Tuple[mysql.connector.MySQLConnection, SSHTunnelForwarder]:
    """Establish an SSH tunnel and MySQL connection using interactive prompts.

    Returns a tuple of (mysql_connection, ssh_tunnel_server). Caller is responsible
    for closing both via `close_connection`.
    """

    server_credentials = _load_server_credentials(credentials_path)

    sql_hostname = _prompt_with_default("SQL_hostname:\n", server_credentials.get("sql_hostname", ""))
    ssh_host = _prompt_with_default("PHPKB host:\n", server_credentials.get("ssh_host", ""))
    ssh_username = _prompt_with_default("SSH username:\n", server_credentials.get("ssh_username", ""))
    ssh_password = getpass("SSH password:\n")
    ssh_port = int(server_credentials.get("ssh_port", "22"))
    sql_username = _prompt_with_default("SQL username:\n", server_credentials.get("sql_username", ""))
    sql_password = getpass("SQL password:\n")
    sql_database = _prompt_with_default("Database name:\n", server_credentials.get("sql_database", ""))
    sql_port = server_credentials.get("sql_port", "") or input("SQL remote port:\n")
    sql_port_local = server_credentials.get("sql_port_local", "") or input("SQL local port:\n")
    sql_ip = server_credentials.get("sql_ip", "") or input("SQL remote IP:\n")

    server = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(sql_ip, sql_port),
        local_bind_address=(sql_ip, sql_port_local),
    )

    server.start()

    connection = mysql.connector.MySQLConnection(
        user=sql_username,
        password=sql_password,
        host=sql_ip,
        port=server.local_bind_port,
        database=sql_database,
    )

    return connection, server


def close_connection(connection: mysql.connector.MySQLConnection, server: SSHTunnelForwarder) -> None:
    """Close MySQL connection and stop SSH tunnel, ignoring errors."""
    try:
        if connection:
            connection.close()
    finally:
        try:
            if server:
                server.close()
                server.stop()
        except Exception:
            # Best-effort shutdown
            pass



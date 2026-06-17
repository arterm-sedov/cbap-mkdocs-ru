"""SSH into the production server and git pull the PHPKB assets repo."""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import paramiko

REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(REPO_ROOT / ".env")

SERVER_PROFILE = os.getenv("SERVER_PROFILE", "cmw").lower()
PROFILE_PREFIX = {"cmw": "CMW_", "cmwlab": "CMWLAB_"}.get(SERVER_PROFILE, "CMW_")


def load_credentials() -> dict:
    prefix = PROFILE_PREFIX
    creds = {}
    for var in ["SSH_HOST", "SSH_PORT", "SSH_USERNAME", "SSH_PASSWORD", "SSH_KB_REPO_PATH"]:
        val = os.getenv(f"{prefix}{var}")
        if val:
            creds[var.lower()] = val
    if "ssh_host" not in creds:
        print(f"Error: {prefix}SSH_HOST not set in .env")
        sys.exit(1)
    creds.setdefault("ssh_port", 22)
    creds.setdefault("ssh_kb_repo_path", "/var/www/html")
    return creds


def ssh_pull(creds: dict, no_ask: bool = False) -> bool:
    host = creds["ssh_host"]
    port = int(creds["ssh_port"])
    username = creds["ssh_username"]
    password = creds.get("ssh_password")
    remote_path = creds["ssh_kb_repo_path"]

    if not no_ask:
        answer = input(
            f"SSH into {username}@{host}:{port} and run:\n"
            f"  git -C {remote_path} pull\n"
            "Continue? [Y/n]: "
        ).strip().lower()
        if answer and answer != "y" and answer != "yes":
            print("Cancelled.")
            return False

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=username, password=password,
                       timeout=15, look_for_keys=True, allow_agent=True)
        command = f"cd {remote_path} && git pull"
        stdin, stdout, stderr = client.exec_command(command, timeout=60)
        exit_status = stdout.channel.recv_exit_status()
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        if exit_status != 0:
            print(f"Remote command failed (exit {exit_status})", file=sys.stderr)
            return False
        print(f"Pull on {host} completed.")
        return True
    except Exception as e:
        print(f"SSH connection failed: {e}", file=sys.stderr)
        return False
    finally:
        client.close()


def parse_args():
    parser = argparse.ArgumentParser(
        description="SSH into production and git pull the PHPKB assets repo."
    )
    parser.add_argument(
        "--no-ask",
        action="store_true",
        help="Skip confirmation prompt",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    creds = load_credentials()
    sys.exit(0 if ssh_pull(creds, args.no_ask) else 1)

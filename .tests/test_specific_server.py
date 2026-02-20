"""Test connection to a specific server.

Usage:
    python .tests/test_specific_server.py
"""

import sys
import json
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.ssh_kb_ru import establish_connection_interactive, close_connection


def test_server(ssh_host, ssh_port, ssh_username=None):
    """Test connection to a specific server.
    
    Args:
        ssh_host: SSH hostname or IP address
        ssh_port: SSH port number
        ssh_username: Optional SSH username (will prompt if not provided)
    """
    print("="*60)
    print(f"Testing connection to {ssh_host}:{ssh_port}")
    print("="*60)
    
    # Create a temporary credentials file with minimal info
    # The establish_connection_interactive will prompt for missing values
    temp_creds = {
        "ssh_host": ssh_host,
        "ssh_port": str(ssh_port),
    }
    
    if ssh_username:
        temp_creds["ssh_username"] = ssh_username
    
    # Create temporary credentials file
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    json.dump(temp_creds, temp_file)
    temp_file.close()
    
    connection = None
    server = None
    
    try:
        print(f"\nStep 1: Establishing SSH tunnel...")
        print(f"Host: {ssh_host}")
        print(f"Port: {ssh_port}")
        if ssh_username:
            print(f"Username: {ssh_username}")
        print("\nYou will be prompted for:")
        print("  - SSH username (if not provided)")
        print("  - SSH password (if key auth fails)")
        print("  - SQL connection details")
        print("  - MySQL password")
        print()
        
        connection, server = establish_connection_interactive(temp_file.name)
        
        if not connection:
            print("❌ FAILED: Connection object is None")
            return False
        
        if not server:
            print("❌ FAILED: SSH tunnel server object is None")
            return False
        
        if not server.is_alive:
            print("❌ FAILED: SSH tunnel is not alive")
            return False
        
        print(f"\n✅ SSH tunnel established successfully")
        print(f"   Local bind port: {server.local_bind_port}")
        print(f"   Tunnel is alive: {server.is_alive}")
        
        # Test MySQL connection
        print("\nStep 2: Testing MySQL connection...")
        cursor = connection.cursor()
        
        # Test query: Get database name
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"✅ Connected to MySQL database: {db_name}")
        
        # Test query: Get MySQL version
        cursor.execute("SELECT VERSION()")
        mysql_version = cursor.fetchone()[0]
        print(f"✅ MySQL version: {mysql_version}")
        
        # Test query: Count tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"✅ Found {len(tables)} tables in database")
        
        # Test query: Check phpkb_articles table exists and get count
        try:
            cursor.execute("SELECT COUNT(*) FROM phpkb_articles")
            article_count = cursor.fetchone()[0]
            print(f"✅ phpkb_articles table exists with {article_count} articles")
        except Exception as e:
            print(f"⚠️  Warning: Could not query phpkb_articles table: {e}")
        
        # Test query: Check phpkb_categories table exists and get count
        try:
            cursor.execute("SELECT COUNT(*) FROM phpkb_categories")
            category_count = cursor.fetchone()[0]
            print(f"✅ phpkb_categories table exists with {category_count} categories")
        except Exception as e:
            print(f"⚠️  Warning: Could not query phpkb_categories table: {e}")
        
        cursor.close()
        
        print(f"\n✅ SUCCESS: Connection test passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ FAILED: Connection test failed")
        print(f"   Error: {type(e).__name__}: {e}")
        import traceback
        print(f"\n   Traceback:")
        traceback.print_exc()
        return False
        
    finally:
        # Cleanup
        print(f"\nStep 3: Closing connections...")
        try:
            if connection or server:
                close_connection(connection, server)
                print(f"✅ Connections closed successfully")
        except Exception as e:
            print(f"⚠️  Warning: Error during cleanup: {e}")
        
        # Clean up temp file
        try:
            Path(temp_file.name).unlink()
        except Exception:
            pass


if __name__ == "__main__":
    # Server details
    SSH_HOST = "31.135.15.59"
    SSH_PORT = 8223
    
    print("="*60)
    print("Specific Server Connection Test")
    print("="*60)
    print(f"\nServer: {SSH_HOST}:{SSH_PORT}")
    print("\nThis script will test SSH and MySQL connections.")
    print("You will be prompted for credentials if not stored in keychain.")
    print("="*60)
    
    success = test_server(SSH_HOST, SSH_PORT)
    
    if success:
        print("\n✅ Connection test completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Connection test failed. Check the output above for details.")
        sys.exit(1)

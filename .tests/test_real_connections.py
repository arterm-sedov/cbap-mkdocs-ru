"""Test script for real SSH and MySQL connections to CMW Lab and Comindware servers.

This script tests actual connections (not mocked) to verify:
1. SSH tunnel establishment
2. MySQL connection through SSH tunnel
3. Database queries
4. Connection cleanup

Usage:
    python .tests/test_real_connections.py [--server cmw_lab|comindware|both]
"""

import sys
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.ssh_kb_ru import establish_connection_interactive, close_connection


def test_connection(server_profile, server_name):
    """Test connection to a specific server.
    
    Args:
        server_profile: Server profile identifier ('cmw' or 'cmwlab')
        server_name: Name of the server for display purposes
    
    Returns:
        bool: True if connection test passed, False otherwise
    """
    print(f"\n{'='*60}")
    print(f"Testing connection to {server_name}")
    print(f"Server profile: {server_profile}")
    print(f"{'='*60}\n")
    
    connection = None
    server = None
    
    try:
        # Establish connection
        print("Step 1: Establishing SSH tunnel and MySQL connection...")
        connection, server = establish_connection_interactive(server_profile)
        
        if not connection:
            print("❌ FAILED: Connection object is None")
            return False
        
        if not server:
            print("❌ FAILED: SSH tunnel server object is None")
            return False
        
        if not server.is_alive:
            print("❌ FAILED: SSH tunnel is not alive")
            return False
        
        print(f"✅ SSH tunnel established successfully")
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
        
        print(f"\n✅ SUCCESS: All connection tests passed for {server_name}")
        return True
        
    except Exception as e:
        print(f"\n❌ FAILED: Connection test failed for {server_name}")
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


def main():
    """Main function to run connection tests."""
    parser = argparse.ArgumentParser(
        description="Test real SSH and MySQL connections to CMW Lab and Comindware servers"
    )
    parser.add_argument(
        "--server",
        choices=["cmw_lab", "comindware", "both"],
        default="both",
        help="Which server(s) to test (default: both)"
    )
    
    args = parser.parse_args()
    
    print("="*60)
    print("Real Connection Test Suite")
    print("="*60)
    print("\nThis script will test actual SSH and MySQL connections.")
    print("You will be prompted for credentials if not stored in keychain.")
    print("\n⚠️  Note: This requires:")
    print("   - Network access to the servers")
    print("   - Valid SSH keys or passwords")
    print("   - Valid MySQL credentials")
    print("="*60)
    
    results = {}
    
    if args.server in ["cmw_lab", "both"]:
        server_profile = "cmwlab"
        print(f"\n⚠️  Note: Using server profile '{server_profile}' from .env file.")
        print("   Set SERVER_PROFILE=cmwlab in .env or pass as argument.")
        
        results["CMW Lab"] = test_connection(server_profile, "CMW Lab Server")
    
    if args.server in ["comindware", "both"]:
        server_profile = "cmw"
        print(f"\n⚠️  Note: Using server profile '{server_profile}' from .env file.")
        print("   Set SERVER_PROFILE=cmw in .env or pass as argument.")
        
        results["Comindware"] = test_connection(server_profile, "Comindware Server")
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    all_passed = True
    for server_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{server_name}: {status}")
        if not passed:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n✅ All connection tests passed!")
        return 0
    else:
        print("\n❌ Some connection tests failed. Check the output above for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

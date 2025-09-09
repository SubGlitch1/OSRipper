#!/usr/bin/env python3
"""
OSRipper Logging System
Advanced logging with multiple handlers and formatters
"""

import os
import sys
import logging
import logging.handlers
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
import json

class ColoredFormatter(logging.Formatter):
    """Colored formatter for console output."""
    
    # Color codes
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green  
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[35m',   # Magenta
        'RESET': '\033[0m'        # Reset
    }
    
    def format(self, record):
        # Add color to levelname
        if record.levelname in self.COLORS:
            record.levelname = f"{self.COLORS[record.levelname]}{record.levelname}{self.COLORS['RESET']}"
        
        return super().format(record)

class JSONFormatter(logging.Formatter):
    """JSON formatter for structured logging."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage()
        }
        
        # Add extra fields if present
        if hasattr(record, 'operation'):
            log_entry['operation'] = record.operation
        if hasattr(record, 'payload_type'):
            log_entry['payload_type'] = record.payload_type
        if hasattr(record, 'target'):
            log_entry['target'] = record.target
        
        return json.dumps(log_entry)

class OSRipperLogger:
    """Advanced logging system for OSRipper."""
    
    def __init__(self, name: str = "OSRipper", log_dir: str = "logs"):
        self.name = name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Prevent duplicate handlers
        if self.logger.handlers:
            self.logger.handlers.clear()
        
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup logging handlers."""
        
        # Console handler with colors
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = ColoredFormatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # Main log file handler
        main_log_file = self.log_dir / "osripper.log"
        file_handler = logging.handlers.RotatingFileHandler(
            main_log_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # Error log file handler
        error_log_file = self.log_dir / "error.log"
        error_handler = logging.handlers.RotatingFileHandler(
            error_log_file,
            maxBytes=5*1024*1024,  # 5MB
            backupCount=3
        )
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(file_formatter)
        self.logger.addHandler(error_handler)
        
        # JSON log file handler for structured logging
        json_log_file = self.log_dir / "osripper.json"
        json_handler = logging.handlers.RotatingFileHandler(
            json_log_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=3
        )
        json_handler.setLevel(logging.INFO)
        json_handler.setFormatter(JSONFormatter())
        self.logger.addHandler(json_handler)
    
    def set_level(self, level: str):
        """Set logging level."""
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        
        if level.upper() in level_map:
            self.logger.setLevel(level_map[level.upper()])
            # Update console handler level
            for handler in self.logger.handlers:
                if isinstance(handler, logging.StreamHandler) and handler.stream == sys.stdout:
                    handler.setLevel(level_map[level.upper()])
    
    def debug(self, message: str, **kwargs):
        """Log debug message."""
        self.logger.debug(message, extra=kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message."""
        self.logger.info(message, extra=kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message."""
        self.logger.warning(message, extra=kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message."""
        self.logger.error(message, extra=kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message."""
        self.logger.critical(message, extra=kwargs)
    
    def operation_start(self, operation: str, **kwargs):
        """Log operation start."""
        self.info(f"🚀 Starting operation: {operation}", operation=operation, **kwargs)
    
    def operation_complete(self, operation: str, **kwargs):
        """Log operation completion."""
        self.info(f"✅ Completed operation: {operation}", operation=operation, **kwargs)
    
    def operation_failed(self, operation: str, error: str, **kwargs):
        """Log operation failure."""
        self.error(f"❌ Failed operation: {operation} - {error}", operation=operation, error=error, **kwargs)
    
    def payload_generated(self, payload_type: str, target: str, **kwargs):
        """Log payload generation."""
        self.info(f"🎯 Generated {payload_type} payload: {target}", 
                 operation="payload_generation", payload_type=payload_type, target=target, **kwargs)
    
    def connection_attempt(self, host: str, port: int, **kwargs):
        """Log connection attempt."""
        self.info(f"🔌 Connection attempt: {host}:{port}", 
                 operation="connection", target=f"{host}:{port}", **kwargs)
    
    def connection_established(self, host: str, port: int, **kwargs):
        """Log successful connection."""
        self.info(f"✅ Connection established: {host}:{port}", 
                 operation="connection", target=f"{host}:{port}", **kwargs)
    
    def security_event(self, event_type: str, details: str, **kwargs):
        """Log security-related events."""
        self.warning(f"🛡️  Security event [{event_type}]: {details}", 
                    operation="security", event_type=event_type, **kwargs)
    
    def obfuscation_applied(self, layers: int, techniques: list, **kwargs):
        """Log obfuscation application."""
        self.info(f"🎭 Applied {layers} obfuscation layers: {', '.join(techniques)}", 
                 operation="obfuscation", layers=layers, techniques=techniques, **kwargs)
    
    def compilation_started(self, compiler: str, target: str, **kwargs):
        """Log compilation start."""
        self.info(f"🔨 Starting compilation with {compiler}: {target}", 
                 operation="compilation", compiler=compiler, target=target, **kwargs)
    
    def compilation_finished(self, output_file: str, size_kb: float, **kwargs):
        """Log compilation completion."""
        self.info(f"✅ Compilation finished: {output_file} ({size_kb:.1f} KB)", 
                 operation="compilation", output=output_file, size_kb=size_kb, **kwargs)
    
    def get_log_stats(self) -> Dict[str, Any]:
        """Get logging statistics."""
        stats = {
            'log_files': {},
            'total_size_mb': 0
        }
        
        for log_file in self.log_dir.glob("*.log*"):
            if log_file.is_file():
                size_bytes = log_file.stat().st_size
                size_mb = size_bytes / (1024 * 1024)
                stats['log_files'][log_file.name] = {
                    'size_mb': round(size_mb, 2),
                    'modified': datetime.fromtimestamp(log_file.stat().st_mtime).isoformat()
                }
                stats['total_size_mb'] += size_mb
        
        stats['total_size_mb'] = round(stats['total_size_mb'], 2)
        return stats
    
    def cleanup_old_logs(self, days: int = 30):
        """Clean up old log files."""
        cutoff_time = datetime.now().timestamp() - (days * 24 * 3600)
        cleaned_files = []
        
        for log_file in self.log_dir.glob("*.log*"):
            if log_file.is_file() and log_file.stat().st_mtime < cutoff_time:
                try:
                    log_file.unlink()
                    cleaned_files.append(log_file.name)
                except Exception as e:
                    self.error(f"Failed to delete old log file {log_file}: {e}")
        
        if cleaned_files:
            self.info(f"🧹 Cleaned up {len(cleaned_files)} old log files")
        
        return cleaned_files

class OperationLogger:
    """Context manager for logging operations."""
    
    def __init__(self, logger: OSRipperLogger, operation: str, **kwargs):
        self.logger = logger
        self.operation = operation
        self.kwargs = kwargs
        self.start_time = None
    
    def __enter__(self):
        self.start_time = datetime.now()
        self.logger.operation_start(self.operation, **self.kwargs)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = (datetime.now() - self.start_time).total_seconds()
        
        if exc_type is None:
            self.logger.operation_complete(
                self.operation, 
                duration_seconds=duration, 
                **self.kwargs
            )
        else:
            self.logger.operation_failed(
                self.operation, 
                str(exc_val), 
                duration_seconds=duration,
                **self.kwargs
            )
        
        return False  # Don't suppress exceptions

# Global logger instance
_global_logger: Optional[OSRipperLogger] = None

def get_logger(name: str = "OSRipper") -> OSRipperLogger:
    """Get or create global logger instance."""
    global _global_logger
    if _global_logger is None:
        _global_logger = OSRipperLogger(name)
    return _global_logger

def init_logger(name: str = "OSRipper", log_dir: str = "logs", level: str = "INFO") -> OSRipperLogger:
    """Initialize global logger."""
    global _global_logger
    _global_logger = OSRipperLogger(name, log_dir)
    _global_logger.set_level(level)
    return _global_logger

def log_operation(operation: str, **kwargs):
    """Decorator for logging operations."""
    def decorator(func):
        def wrapper(*args, **func_kwargs):
            logger = get_logger()
            with OperationLogger(logger, operation, **kwargs):
                return func(*args, **func_kwargs)
        return wrapper
    return decorator

if __name__ == "__main__":
    # Test the logging system
    logger = OSRipperLogger()
    
    logger.info("OSRipper logging system initialized")
    logger.debug("This is a debug message")
    logger.warning("This is a warning")
    logger.error("This is an error")
    
    logger.payload_generated("reverse_tcp", "192.168.1.100:4444")
    logger.connection_attempt("192.168.1.100", 4444)
    logger.security_event("vm_detection", "VirtualBox detected")
    logger.obfuscation_applied(5, ["base64", "zlib", "marshal"])
    logger.compilation_started("nuitka", "payload.py")
    logger.compilation_finished("payload.exe", 2048.5)
    
    # Test operation context manager
    with OperationLogger(logger, "test_operation", test_param="value"):
        import time
        time.sleep(0.1)
    
    # Show log statistics
    stats = logger.get_log_stats()
    print(f"\nLog Statistics:")
    print(f"Total size: {stats['total_size_mb']} MB")
    for filename, info in stats['log_files'].items():
        print(f"  {filename}: {info['size_mb']} MB")

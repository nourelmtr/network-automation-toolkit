"""
Application configuration
"""

# ==========================
# Device Commands
# ==========================

SHOW_VERSION = "show version"

SHOW_INTERFACES = "show ip interface brief"

SHOW_RUNNING_CONFIG = "show running-config"

SHOW_HOSTNAME = "show running-config | include hostname"


# ==========================
# File Paths
# ==========================

INVENTORY_FILE = "inventory/devices.yaml"

BACKUP_DIRECTORY = "backup"

REPORT_DIRECTORY = "reports"

LOG_DIRECTORY = "logs"


# ==========================
# Network Settings
# ==========================

SSH_PORT = 22

SSH_TIMEOUT = 10

PING_TIMEOUT = 2
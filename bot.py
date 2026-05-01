#!/usr/bin/env python3
# ╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                               ║
# ║  ███╗   ██╗███████╗██╗  ██╗    ██╗   ██╗███╗   ███╗    ██╗   ██╗   ██╔                        ║
# ║  ████╗  ██║██╔════╝╚██╗██╔╝    ██║   ██║████╗ ████║    ██║   ██║╚══██╔                        ║
# ║  ██╔██╗ ██║█████╗   ╚███╔╝     ██║   ██║██╔████╔██║    ██║   ██║   ██║                        ║
# ║  ██║╚██╗██║██╔══╝   ██╔██╗     ╚██╗ ██╔╝██║╚██╔╝██║    ╚██╗ ██╔╝   ██║                        ║
# ║  ██║ ╚████║███████╗██╔╝ ██╗     ╚████╔╝ ██║ ╚═╝ ██║     ╚████╔╝    ██║                        ║
# ║  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚═╝     ╚═╝      ╚═══╝     ╚═╝                        ║
# ║                                                                                               ║
# ║                     ⚡ NEX VM V1 TOOL - VPS MANAGEMENT SYSTEM ⚡                             ║
# ║                                                                                               ║
# ║                         ████████╗ ██████╗  ██████╗ ██╗                                        ║
# ║                         ╚══██╔══╝██╔═══██╗██╔═══██╗██║                                        ║
# ║                            ██║   ██║   ██║██║   ██║██║                                        ║
# ║                            ██║   ██║   ██║██║   ██║██║                                        ║
# ║                            ██║   ╚██████╔╝╚██████╔╝███████╗                                   ║
# ║                            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                   ║
# ║                                                                                               ║
# ║                         Made by DeVv-prime ⚡ Version 1.0.0                                  ║
# ║                     CORE READY • SYSTEM STABLE • ALL MODULES ACTIVE                           ║
# ║                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════╝

import discord
from discord.ext import commands, tasks
from discord.ui import Modal, TextInput, View, Button, Select, InputText
import asyncio
import json
import os
import random
import string
import subprocess
import sys
import re
import sqlite3
import logging
import shlex
import shutil
import time
import aiohttp
import psutil
import netifaces
import socket
import requests
import hashlib
import uuid
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import io
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any, Tuple

# ==================================================================================================
#  🎨  COLOR CONSTANTS
# ==================================================================================================

COLORS = {
    'primary': 0x5865F2,
    'success': 0x57F287,
    'error': 0xED4245,
    'warning': 0xFEE75C,
    'info': 0x5865F2,
    'node': 0x9B59B6,
    'terminal': 0x2C2F33,
    'gold': 0xFFD700,
    'cyan': 0x00CCFF,
    'pink': 0xFF69B4,
    'os': 0x00FF88,
}

# ==================================================================================================
#  📝  LOGGING SETUP
# ==================================================================================================

# Create directories
os.makedirs('/opt/nex-vm-v1/logs', exist_ok=True)
os.makedirs('/opt/nex-vm-v1/data', exist_ok=True)
os.makedirs('/opt/nex-vm-v1/backups', exist_ok=True)
os.makedirs('/opt/nex-vm-v1/qr_codes', exist_ok=True)
os.makedirs('/opt/nex-vm-v1/nodes', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('/opt/nex-vm-v1/logs/nexvm.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("NEXVM-V1-BOT")

# ==================================================================================================
#  ⚙️  CONFIGURATION - IMPORTANT: CHANGE THESE VALUES!
# ==================================================================================================

# Discord Bot Configuration
BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"  # CHANGE THIS!
BOT_PREFIX = "."
BOT_NAME = "NEXVM-V1"
BOT_AUTHOR = "DeVv-Prime"
MAIN_ADMIN_IDS = [1405866008127864852]  # CHANGE THIS TO YOUR DISCORD ID!

# Storage Configuration
DEFAULT_STORAGE_POOL = "default"

# License Keys - Valid keys for the bot
VALID_LICENSE_KEYS = ["prime2026", "preimdragon", "gamerhindu"]

# Auto-detect server information
try:
    SERVER_IP = requests.get('https://api.ipify.org', timeout=5).text.strip()
except:
    try:
        SERVER_IP = subprocess.getoutput("curl -s ifconfig.me")
    except:
        SERVER_IP = "127.0.0.1"

HOSTNAME = socket.gethostname()

def get_mac_address():
    try:
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            if iface != 'lo':
                addr = netifaces.ifaddresses(iface)
                if netifaces.AF_LINK in addr:
                    return addr[netifaces.AF_LINK][0]['addr']
    except:
        pass
    return "00:00:00:00:00:00"

MAC_ADDRESS = get_mac_address()
THUMBNAIL_URL = "https://images-ext-1.discordapp.net/external/6lAZL5FnvLRPc2KydFlV2yuW8CPj_P7LE0MdcNLhki0/%3Fsize%3D2048/https/cdn.discordapp.com/icons/1478373286684393604/6317df64b495cfcbaf38f12db6bb22c0.webp?format=webp"

# ==================================================================================================
#  🐧  OS OPTIONS - 70+ OPERATING SYSTEMS
# ==================================================================================================

OS_OPTIONS = [
    # Ubuntu Series
    {"label": "🐧 Ubuntu 24.04 LTS", "value": "ubuntu:24.04", "desc": "Noble Numbat - Latest LTS", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 22.04 LTS", "value": "ubuntu:22.04", "desc": "Jammy Jellyfish - Current LTS", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 20.04 LTS", "value": "ubuntu:20.04", "desc": "Focal Fossa - Stable LTS", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 18.04 LTS", "value": "ubuntu:18.04", "desc": "Bionic Beaver - Legacy LTS", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    
    # Debian Series
    {"label": "🌀 Debian 12", "value": "debian:12", "desc": "Bookworm - Current Stable", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Debian 11", "value": "debian:11", "desc": "Bullseye - Old Stable", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Debian 10", "value": "debian:10", "desc": "Buster - Older Stable", "category": "Debian", "icon": "🌀", "ram_min": 512},
    
    # Fedora Series
    {"label": "🎩 Fedora 40", "value": "fedora:40", "desc": "Fedora 40 - Latest", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    {"label": "🎩 Fedora 39", "value": "fedora:39", "desc": "Fedora 39 - Stable", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    
    # CentOS/Rocky/Alma
    {"label": "📦 CentOS 9 Stream", "value": "centos:9", "desc": "CentOS 9 Stream", "category": "CentOS", "icon": "📦", "ram_min": 1024},
    {"label": "📦 CentOS 7", "value": "centos:7", "desc": "CentOS 7 - Legacy", "category": "CentOS", "icon": "📦", "ram_min": 1024},
    {"label": "🦊 Rocky Linux 9", "value": "rockylinux:9", "desc": "Rocky 9 - Latest", "category": "Rocky", "icon": "🦊", "ram_min": 1024},
    {"label": "🦊 AlmaLinux 9", "value": "almalinux:9", "desc": "Alma 9 - Latest", "category": "AlmaLinux", "icon": "🦊", "ram_min": 1024},
    
    # Lightweight
    {"label": "🐧 Alpine 3.19", "value": "alpine:3.19", "desc": "Alpine 3.19 - Lightweight", "category": "Alpine", "icon": "🐧", "ram_min": 256},
    {"label": "🐧 Alpine 3.18", "value": "alpine:3.18", "desc": "Alpine 3.18 - Stable", "category": "Alpine", "icon": "🐧", "ram_min": 256},
    
    # Arch Linux
    {"label": "📀 Arch Linux", "value": "archlinux:latest", "desc": "Arch - Rolling Release", "category": "Arch", "icon": "📀", "ram_min": 1024},
    
    # Kali Linux
    {"label": "🐉 Kali Linux", "value": "kali:latest", "desc": "Kali - Security Testing", "category": "Kali", "icon": "🐉", "ram_min": 2048},
]

# ==================================================================================================
#  🎮  GAMES LIST
# ==================================================================================================

GAMES_LIST = [
    {'name': 'Minecraft Java', 'docker': 'itzg/minecraft-server', 'port': 25565, 'ram': 2048, 'icon': '🎮'},
    {'name': 'Minecraft Bedrock', 'docker': 'itzg/minecraft-bedrock-server', 'port': 19132, 'ram': 1024, 'icon': '📱'},
    {'name': 'Terraria', 'docker': 'beardedio/terraria', 'port': 7777, 'ram': 1024, 'icon': '🌳'},
    {'name': 'Valheim', 'docker': 'lloesche/valheim-server', 'port': 2456, 'ram': 2048, 'icon': '⚔️'},
]

# ==================================================================================================
#  🛠️  TOOLS LIST
# ==================================================================================================

TOOLS_LIST = [
    {'name': 'Nginx', 'cmd': 'apt install nginx -y', 'port': 80, 'icon': '🌐'},
    {'name': 'Apache', 'cmd': 'apt install apache2 -y', 'port': 80, 'icon': '🕸️'},
    {'name': 'MySQL', 'cmd': 'apt install mysql-server -y', 'port': 3306, 'icon': '🗄️'},
    {'name': 'PostgreSQL', 'cmd': 'apt install postgresql -y', 'port': 5432, 'icon': '🐘'},
    {'name': 'Docker', 'cmd': 'curl -fsSL https://get.docker.com | bash', 'icon': '🐳'},
    {'name': 'Node.js', 'cmd': 'curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt install nodejs -y', 'icon': '🟢'},
]

# ==================================================================================================
#  💰  FREE VPS PLANS
# ==================================================================================================

FREE_VPS_PLANS = {
    'invites': [
        {'name': '🥉 Bronze', 'invites': 5, 'ram': 2, 'cpu': 1, 'disk': 20, 'emoji': '🥉'},
        {'name': '🥈 Silver', 'invites': 10, 'ram': 4, 'cpu': 2, 'disk': 40, 'emoji': '🥈'},
        {'name': '🥇 Gold', 'invites': 15, 'ram': 8, 'cpu': 4, 'disk': 80, 'emoji': '🥇'},
        {'name': '🏆 Platinum', 'invites': 20, 'ram': 16, 'cpu': 8, 'disk': 160, 'emoji': '🏆'},
        {'name': '💎 Diamond', 'invites': 25, 'ram': 32, 'cpu': 16, 'disk': 320, 'emoji': '💎'},
    ]
}

# ==================================================================================================
#  🗄️  DATABASE SETUP
# ==================================================================================================

DATABASE_PATH = '/opt/nex-vm-v1/data/nexvm.db'
NODES_FILE = '/opt/nex-vm-v1/nodes/nodes.json'

def get_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        return None

def init_db():
    conn = get_db()
    if not conn:
        logger.error("Failed to initialize database")
        return False
    
    cur = conn.cursor()
    
    # Users table
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        username TEXT,
        created_at TEXT,
        last_seen TEXT
    )''')
    
    # VPS table
    cur.execute('''CREATE TABLE IF NOT EXISTS vps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        container_name TEXT UNIQUE NOT NULL,
        plan_name TEXT DEFAULT 'Custom',
        ram INTEGER NOT NULL,
        cpu INTEGER NOT NULL,
        disk INTEGER NOT NULL,
        os_version TEXT DEFAULT 'ubuntu:22.04',
        status TEXT DEFAULT 'stopped',
        suspended INTEGER DEFAULT 0,
        purge_protected INTEGER DEFAULT 0,
        node_name TEXT DEFAULT 'local',
        created_at TEXT NOT NULL,
        ip_address TEXT,
        mac_address TEXT,
        ssh_key TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )''')
    
    # User stats table
    cur.execute('''CREATE TABLE IF NOT EXISTS user_stats (
        user_id TEXT PRIMARY KEY,
        invites INTEGER DEFAULT 0,
        claimed_vps_count INTEGER DEFAULT 0,
        api_key TEXT UNIQUE,
        last_updated TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )''')
    
    # Settings table
    cur.execute('''CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )''')
    
    # Installed games table
    cur.execute('''CREATE TABLE IF NOT EXISTS installed_games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        container_name TEXT,
        game_name TEXT,
        game_port INTEGER,
        installed_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (container_name) REFERENCES vps(container_name)
    )''')
    
    # Installed tools table
    cur.execute('''CREATE TABLE IF NOT EXISTS installed_tools (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        container_name TEXT,
        tool_name TEXT,
        tool_port INTEGER,
        installed_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (container_name) REFERENCES vps(container_name)
    )''')
    
    # Port forwards table
    cur.execute('''CREATE TABLE IF NOT EXISTS port_forwards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        container_name TEXT,
        container_port INTEGER,
        host_port INTEGER UNIQUE,
        protocol TEXT DEFAULT 'tcp',
        created_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (container_name) REFERENCES vps(container_name)
    )''')
    
    # Port allocations table
    cur.execute('''CREATE TABLE IF NOT EXISTS port_allocations (
        user_id TEXT PRIMARY KEY,
        allocated_ports INTEGER DEFAULT 5,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )''')
    
    # Transactions table
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        txn_ref TEXT UNIQUE,
        amount INTEGER,
        status TEXT DEFAULT 'pending',
        created_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )''')
    
    # Snapshots table
    cur.execute('''CREATE TABLE IF NOT EXISTS snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        container_name TEXT,
        snapshot_name TEXT,
        created_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (container_name) REFERENCES vps(container_name)
    )''')
    
    # Insert default settings
    settings = [
        ('license_verified', 'false'),
        ('server_ip', SERVER_IP),
        ('mac_address', MAC_ADDRESS),
        ('hostname', HOSTNAME),
        ('default_port_quota', '5'),
        ('upi_id', 'vedant1437@fam'),
        ('discord_invite', 'https://discord.gg/zS2ynbF6jK'),
    ]
    
    for key, value in settings:
        cur.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)', (key, value))
    
    conn.commit()
    conn.close()
    logger.info("✅ Database initialized successfully")
    return True

# Initialize database
init_db()

# ==================================================================================================
#  📊  DATABASE HELPER FUNCTIONS
# ==================================================================================================

def get_setting(key: str, default: Any = None) -> Any:
    conn = get_db()
    if not conn:
        return default
    cur = conn.cursor()
    cur.execute('SELECT value FROM settings WHERE key = ?', (key,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else default

def set_setting(key: str, value: str):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', (key, value))
    conn.commit()
    conn.close()

def get_user_vps(user_id: str) -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM vps WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_all_vps() -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM vps ORDER BY created_at DESC')
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_vps(user_id: str, container_name: str, ram: int, cpu: int, disk: int, os_version: str, plan: str = "Custom") -> Optional[Dict]:
    conn = get_db()
    if not conn:
        return None
    cur = conn.cursor()
    now = datetime.now().isoformat()
    
    cur.execute('''INSERT INTO vps 
        (user_id, container_name, plan_name, ram, cpu, disk, os_version, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (user_id, container_name, plan, ram, cpu, disk, os_version, 'running', now))
    
    conn.commit()
    conn.close()
    return {'container_name': container_name}

def update_vps_status(container_name: str, status: str):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('UPDATE vps SET status = ? WHERE container_name = ?', (status, container_name))
    conn.commit()
    conn.close()

def delete_vps(container_name: str) -> bool:
    conn = get_db()
    if not conn:
        return False
    cur = conn.cursor()
    cur.execute('DELETE FROM vps WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM installed_games WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM installed_tools WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM port_forwards WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM snapshots WHERE container_name = ?', (container_name,))
    conn.commit()
    conn.close()
    return True

def is_admin(user_id: str) -> bool:
    return str(user_id) in [str(aid) for aid in MAIN_ADMIN_IDS]

def get_user_stats(user_id: str) -> Dict:
    conn = get_db()
    if not conn:
        return {'invites': 0, 'claimed_vps_count': 0}
    cur = conn.cursor()
    cur.execute('SELECT * FROM user_stats WHERE user_id = ?', (user_id,))
    row = cur.fetchone()
    conn.close()
    
    if row:
        return dict(row)
    
    # Create new user stats
    api_key = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()[:16]
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO user_stats (user_id, invites, claimed_vps_count, api_key, last_updated) VALUES (?, 0, 0, ?, ?)',
               (user_id, api_key, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    
    return {'user_id': user_id, 'invites': 0, 'claimed_vps_count': 0, 'api_key': api_key}

def update_user_stats(user_id: str, invites: int = 0, claimed: int = 0):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    
    # Get current stats
    current = get_user_stats(user_id)
    new_invites = current.get('invites', 0) + invites
    new_claimed = current.get('claimed_vps_count', 0) + claimed
    
    cur.execute('''INSERT OR REPLACE INTO user_stats 
        (user_id, invites, claimed_vps_count, api_key, last_updated)
        VALUES (?, ?, ?, ?, ?)''',
        (user_id, new_invites, new_claimed, current.get('api_key', ''), datetime.now().isoformat()))
    
    conn.commit()
    conn.close()

def add_game_install(user_id: str, container: str, game: str, port: int):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('INSERT INTO installed_games (user_id, container_name, game_name, game_port, installed_at) VALUES (?, ?, ?, ?, ?)',
               (user_id, container, game, port, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def add_tool_install(user_id: str, container: str, tool: str, port: int = None):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('INSERT INTO installed_tools (user_id, container_name, tool_name, tool_port, installed_at) VALUES (?, ?, ?, ?, ?)',
               (user_id, container, tool, port, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def add_port_forward(user_id: str, container: str, cport: int, hport: int, proto: str = "tcp") -> bool:
    conn = get_db()
    if not conn:
        return False
    cur = conn.cursor()
    cur.execute('INSERT INTO port_forwards (user_id, container_name, container_port, host_port, protocol, created_at) VALUES (?, ?, ?, ?, ?, ?)',
               (user_id, container, cport, hport, proto, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return True

def get_user_port_forwards(user_id: str) -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM port_forwards WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_port_allocation(user_id: str) -> int:
    conn = get_db()
    if not conn:
        return int(get_setting('default_port_quota', '5'))
    cur = conn.cursor()
    cur.execute('SELECT allocated_ports FROM port_allocations WHERE user_id = ?', (user_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else int(get_setting('default_port_quota', '5'))

def add_port_allocation(user_id: str, amount: int):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    current = get_port_allocation(user_id)
    cur.execute('INSERT OR REPLACE INTO port_allocations (user_id, allocated_ports) VALUES (?, ?)',
               (user_id, current + amount))
    conn.commit()
    conn.close()

def add_transaction(user_id: str, txn_ref: str, amount: int) -> int:
    conn = get_db()
    if not conn:
        return 0
    cur = conn.cursor()
    cur.execute('INSERT INTO transactions (user_id, txn_ref, amount, created_at) VALUES (?, ?, ?, ?)',
               (user_id, txn_ref, amount, datetime.now().isoformat()))
    tid = cur.lastrowid
    conn.commit()
    conn.close()
    return tid

def add_snapshot(user_id: str, container: str, snapshot_name: str):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('INSERT INTO snapshots (user_id, container_name, snapshot_name, created_at) VALUES (?, ?, ?, ?)',
               (user_id, container, snapshot_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_snapshots(container: str) -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM snapshots WHERE container_name = ? ORDER BY created_at DESC', (container,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# ==================================================================================================
#  🌐  NODE MANAGEMENT
# ==================================================================================================

def load_nodes():
    default = {
        "version": "1.0.0",
        "last_updated": datetime.now().isoformat(),
        "main_node": "local",
        "nodes": {},
        "node_groups": {"all": [], "us": [], "eu": [], "asia": []}
    }
    
    if os.path.exists(NODES_FILE):
        try:
            with open(NODES_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    
    # Auto-create local node
    try:
        lxc_count = len(subprocess.getoutput("lxc list -c n --format csv").splitlines())
    except:
        lxc_count = 0
    
    local_node = {
        "name": "local",
        "host": "localhost",
        "port": 0,
        "type": "local",
        "status": "online",
        "is_main": True,
        "region": "us",
        "stats": {
            "total_ram": psutil.virtual_memory().total // 1024 // 1024,
            "used_ram": psutil.virtual_memory().used // 1024 // 1024,
            "total_cpu": psutil.cpu_count(),
            "used_cpu": psutil.cpu_percent(),
            "total_disk": psutil.disk_usage('/').total // 1024 // 1024 // 1024,
            "used_disk": psutil.disk_usage('/').used // 1024 // 1024 // 1024,
            "lxc_count": lxc_count,
            "last_checked": datetime.now().isoformat()
        }
    }
    
    default["nodes"]["local"] = local_node
    default["node_groups"]["all"].append("local")
    
    with open(NODES_FILE, 'w') as f:
        json.dump(default, f, indent=2)
    
    return default

def update_local_node_stats():
    nodes = load_nodes()
    if 'local' in nodes['nodes']:
        try:
            lxc_count = len(subprocess.getoutput("lxc list -c n --format csv").splitlines())
        except:
            lxc_count = 0
        nodes['nodes']['local']['stats'] = {
            "total_ram": psutil.virtual_memory().total // 1024 // 1024,
            "used_ram": psutil.virtual_memory().used // 1024 // 1024,
            "total_cpu": psutil.cpu_count(),
            "used_cpu": psutil.cpu_percent(),
            "total_disk": psutil.disk_usage('/').total // 1024 // 1024 // 1024,
            "used_disk": psutil.disk_usage('/').used // 1024 // 1024 // 1024,
            "lxc_count": lxc_count,
            "last_checked": datetime.now().isoformat()
        }
        nodes['nodes']['local']['status'] = "online"
        with open(NODES_FILE, 'w') as f:
            json.dump(nodes, f, indent=2)

# ==================================================================================================
#  🛠️  LXC HELPER FUNCTIONS
# ==================================================================================================

async def run_lxc(cmd: str, timeout: int = 60) -> Tuple[str, str, int]:
    try:
        proc = await asyncio.create_subprocess_exec(
            *shlex.split(cmd),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        try:
            out, err = await asyncio.wait_for(proc.communicate(), timeout)
            return out.decode().strip(), err.decode().strip(), proc.returncode
        except asyncio.TimeoutError:
            proc.kill()
            await proc.wait()
            return "", f"Timeout after {timeout}s", -1
    except Exception as e:
        return "", str(e), -1

async def exec_in_container(container: str, cmd: str, timeout: int = 30) -> Tuple[str, str, int]:
    return await run_lxc(f"lxc exec {container} -- bash -c {shlex.quote(cmd)}", timeout)

async def get_container_status(container: str) -> str:
    try:
        out = subprocess.getoutput(f"lxc info {container} 2>/dev/null | grep Status | awk '{{print $2}}'")
        return out.lower() if out else "unknown"
    except:
        return "unknown"

async def get_container_stats(container: str) -> Dict:
    stats = {
        'status': 'unknown', 
        'cpu': '0%', 
        'memory': '0/0MB', 
        'disk': '0/0GB', 
        'ipv4': [], 
        'mac': 'N/A', 
        'uptime': '0m'
    }
    
    stats['status'] = await get_container_status(container)
    
    if stats['status'] == 'running':
        # Get CPU usage
        out, _, _ = await exec_in_container(container, "top -bn1 | grep 'Cpu(s)' | awk '{print $2}' | cut -d'%' -f1")
        stats['cpu'] = f"{out}%" if out else "0%"
        
        # Get memory usage
        out, _, _ = await exec_in_container(container, "free -m | awk '/^Mem:/{print $3\"/\"$2}'")
        stats['memory'] = f"{out}MB" if out else "0/0MB"
        
        # Get disk usage
        out, _, _ = await exec_in_container(container, "df -h / | awk 'NR==2{print $3\"/\"$2}'")
        stats['disk'] = out if out else "0/0GB"
        
        # Get IP addresses
        out, _, _ = await exec_in_container(container, "ip -4 addr show | grep -oP '(?<=inet\\s)[0-9.]+' | grep -v 127")
        stats['ipv4'] = out.splitlines() if out else []
        
        # Get MAC address
        out, _, _ = await exec_in_container(container, "ip link | grep ether | awk '{print $2}' | head -1")
        stats['mac'] = out if out else "N/A"
        
        # Get uptime
        out, _, _ = await exec_in_container(container, "uptime -p | sed 's/up //'")
        stats['uptime'] = out if out else "0m"
    
    return stats

async def get_available_port() -> Optional[int]:
    used = set()
    conn = get_db()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT host_port FROM port_forwards')
        used = {row[0] for row in cur.fetchall()}
        conn.close()
    
    for _ in range(100):
        port = random.randint(20000, 50000)
        if port not in used:
            return port
    return None

async def create_port_forward(user_id: str, container: str, cport: int, proto: str = "tcp") -> Optional[int]:
    hport = await get_available_port()
    if not hport:
        return None
    
    try:
        await run_lxc(f"lxc config device add {container} proxy-{hport} proxy listen=tcp:0.0.0.0:{hport} connect=tcp:127.0.0.1:{cport}")
        add_port_forward(user_id, container, cport, hport, proto)
        return hport
    except:
        return None

async def apply_lxc_config(container_name: str):
    """Apply basic LXC configuration"""
    try:
        await run_lxc(f"lxc config set {container_name} security.privileged true")
        await run_lxc(f"lxc config set {container_name} security.nesting true")
    except:
        pass

async def apply_internal_permissions(container_name: str):
    """Setup internal user permissions"""
    try:
        await exec_in_container(container_name, "useradd -m -s /bin/bash -G sudo svm5 2>/dev/null || true")
        await exec_in_container(container_name, "echo 'svm5:svm5' | chpasswd 2>/dev/null || true")
        await exec_in_container(container_name, "echo 'svm5 ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers 2>/dev/null || true")
    except:
        pass

# ==================================================================================================
#  🎨  UI HELPER FUNCTIONS
# ==================================================================================================

def create_embed(title: str, description: str = "", color: int = COLORS['primary']) -> discord.Embed:
    embed = discord.Embed(
        title=f"```glow\n✦ {BOT_NAME} - {title} ✦\n```",
        description=description,
        color=color
    )
    embed.set_thumbnail(url=THUMBNAIL_URL)
    embed.set_footer(
        text=f"⚡ {BOT_NAME} • {BOT_AUTHOR} • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ⚡",
        icon_url=THUMBNAIL_URL
    )
    return embed

def success_embed(title: str, description: str = "") -> discord.Embed:
    return create_embed(f"✅ {title}", description, COLORS['success'])

def error_embed(title: str, description: str = "") -> discord.Embed:
    return create_embed(f"❌ {title}", description, COLORS['error'])

def info_embed(title: str, description: str = "") -> discord.Embed:
    return create_embed(f"ℹ️ {title}", description, COLORS['info'])

def warning_embed(title: str, description: str = "") -> discord.Embed:
    return create_embed(f"⚠️ {title}", description, COLORS['warning'])

def terminal_embed(title: str, content: str) -> discord.Embed:
    embed = discord.Embed(
        title=f"```fix\n[ {title} ]\n```",
        description=f"```bash\n{content[:1900]}\n```",
        color=COLORS['terminal']
    )
    embed.set_footer(text=f"⚡ Terminal • {datetime.now().strftime('%H:%M:%S')} ⚡")
    return embed

def no_vps_embed() -> discord.Embed:
    return info_embed("No VPS Found", "You don't have any VPS yet.\n\nUse `.plans` to see available plans.")

# ==================================================================================================
#  🌈  CONSTANTS
# ==================================================================================================

RAINBOW_COLORS = [
    0xFF0000, 0xFF7700, 0xFFFF00, 0x00FF00, 0x00CCFF, 0x3366FF, 0x8B00FF, 0xFF00CC
]

# ==================================================================================================
#  🤖  BOT SETUP
# ==================================================================================================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents, help_command=None)
bot.start_time = datetime.utcnow()
LICENSE_VERIFIED = get_setting('license_verified', 'false') == 'true'

# ==================================================================================================
#  🖥️  VPS MANAGE VIEW
# ==================================================================================================

class VPSManageView(View):
    def __init__(self, ctx, container_name, container_data):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.container = container_name
        self.data = container_data
        self.user = ctx.author
        self.message = None
        self.live_mode = False
        self.live_task = None
        
        # Buttons Row 1
        self.start_btn = Button(label="▶️ Start", style=discord.ButtonStyle.success, row=0)
        self.stop_btn = Button(label="⏹️ Stop", style=discord.ButtonStyle.danger, row=0)
        self.restart_btn = Button(label="🔄 Restart", style=discord.ButtonStyle.primary, row=0)
        
        # Buttons Row 2
        self.stats_btn = Button(label="📊 Stats", style=discord.ButtonStyle.secondary, row=1)
        self.console_btn = Button(label="📟 Console", style=discord.ButtonStyle.secondary, row=1)
        self.ssh_btn = Button(label="🔑 SSH", style=discord.ButtonStyle.primary, row=1)
        
        # Buttons Row 3
        self.backup_btn = Button(label="💾 Backup", style=discord.ButtonStyle.success, row=2)
        self.restore_btn = Button(label="🔄 Restore", style=discord.ButtonStyle.warning, row=2)
        self.delete_btn = Button(label="🗑️ Delete", style=discord.ButtonStyle.danger, row=2)
        
        # Buttons Row 4
        self.refresh_btn = Button(label="🔄 Refresh", style=discord.ButtonStyle.secondary, row=3)
        self.close_btn = Button(label="❌ Close", style=discord.ButtonStyle.danger, row=3)
        
        # Set callbacks
        self.start_btn.callback = self.start_callback
        self.stop_btn.callback = self.stop_callback
        self.restart_btn.callback = self.restart_callback
        self.stats_btn.callback = self.stats_callback
        self.console_btn.callback = self.console_callback
        self.ssh_btn.callback = self.ssh_callback
        self.backup_btn.callback = self.backup_callback
        self.restore_btn.callback = self.restore_callback
        self.delete_btn.callback = self.delete_callback
        self.refresh_btn.callback = self.refresh_callback
        self.close_btn.callback = self.close_callback
        
        self.add_item(self.start_btn)
        self.add_item(self.stop_btn)
        self.add_item(self.restart_btn)
        self.add_item(self.stats_btn)
        self.add_item(self.console_btn)
        self.add_item(self.ssh_btn)
        self.add_item(self.backup_btn)
        self.add_item(self.restore_btn)
        self.add_item(self.delete_btn)
        self.add_item(self.refresh_btn)
        self.add_item(self.close_btn)
    
    async def get_stats_embed(self):
        stats = await get_container_stats(self.container)
        
        embed = discord.Embed(
            title=f"```glow\n🖥️ VPS MANAGEMENT - {self.container.upper()}\n```",
            description=f"👤 **Owner:** {self.user.mention}\n📦 **Container:** `{self.container}`",
            color=0x5865F2
        )
        embed.set_thumbnail(url=self.user.avatar.url if self.user.avatar else THUMBNAIL_URL)
        
        status_emoji = "🟢" if stats['status'] == 'running' else "🔴"
        embed.add_field(name="📊 STATUS", value=f"{status_emoji} `{stats['status'].upper()}`", inline=True)
        embed.add_field(name="💾 CPU", value=f"```fix\n{stats['cpu']}\n```", inline=True)
        embed.add_field(name="📀 MEMORY", value=f"```fix\n{stats['memory']}\n```", inline=True)
        embed.add_field(name="💽 DISK", value=f"```fix\n{stats['disk']}\n```", inline=True)
        embed.add_field(name="🌐 IP", value=f"```fix\n{stats['ipv4'][0] if stats['ipv4'] else 'N/A'}\n```", inline=True)
        embed.add_field(name="🔌 MAC", value=f"```fix\n{stats['mac']}\n```", inline=True)
        embed.add_field(name="⏱️ UPTIME", value=f"```fix\n{stats['uptime']}\n```", inline=True)
        
        return embed
    
    async def start_callback(self, interaction):
        await interaction.response.defer()
        await run_lxc(f"lxc start {self.container}")
        update_vps_status(self.container, 'running')
        await interaction.followup.send(embed=success_embed("Started", f"```fix\n{self.container} started!\n```"), ephemeral=True)
        await self.refresh_callback(interaction)
    
    async def stop_callback(self, interaction):
        await interaction.response.defer()
        await run_lxc(f"lxc stop {self.container}")
        update_vps_status(self.container, 'stopped')
        await interaction.followup.send(embed=success_embed("Stopped", f"```fix\n{self.container} stopped.\n```"), ephemeral=True)
        await self.refresh_callback(interaction)
    
    async def restart_callback(self, interaction):
        await interaction.response.defer()
        await run_lxc(f"lxc restart {self.container}")
        update_vps_status(self.container, 'running')
        await interaction.followup.send(embed=success_embed("Restarted", f"```fix\n{self.container} restarted.\n```"), ephemeral=True)
        await self.refresh_callback(interaction)
    
    async def stats_callback(self, interaction):
        stats = await get_container_stats(self.container)
        embed = info_embed(f"Live Stats: {self.container}")
        embed.add_field(name="📊 Status", value=f"```fix\n{stats['status'].upper()}\n```", inline=True)
        embed.add_field(name="💾 CPU", value=f"```fix\n{stats['cpu']}\n```", inline=True)
        embed.add_field(name="📀 Memory", value=f"```fix\n{stats['memory']}\n```", inline=True)
        embed.add_field(name="💽 Disk", value=f"```fix\n{stats['disk']}\n```", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    async def console_callback(self, interaction):
        modal = CommandModal(self.container)
        await interaction.response.send_modal(modal)
    
    async def ssh_callback(self, interaction):
        await interaction.response.defer()
        await exec_in_container(self.container, "apt-get update -qq && apt-get install -y -qq tmate")
        sess = f"nex-{random.randint(1000,9999)}"
        await exec_in_container(self.container, f"tmate -S /tmp/{sess}.sock new-session -d")
        await asyncio.sleep(5)
        out, _, _ = await exec_in_container(self.container, f"tmate -S /tmp/{sess}.sock display -p '#{{tmate_ssh}}'")
        url = out.strip()
        if url:
            try:
                dm = success_embed("🔑 SSH Access")
                dm.add_field(name="Container", value=f"```fix\n{self.container}\n```")
                dm.add_field(name="Command", value=f"```bash\n{url}\n```")
                await interaction.user.send(embed=dm)
                await interaction.followup.send(embed=success_embed("SSH Generated", "Check DMs!"), ephemeral=True)
            except:
                await interaction.followup.send(embed=error_embed("DM Failed", f"```fix\n{url}\n```"), ephemeral=True)
        else:
            await interaction.followup.send(embed=error_embed("Failed", "Could not generate SSH"), ephemeral=True)
    
    async def backup_callback(self, interaction):
        await interaction.response.defer()
        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        out, err, code = await run_lxc(f"lxc snapshot {self.container} {backup_name}")
        if code == 0:
            add_snapshot(str(self.ctx.author.id), self.container, backup_name)
            embed = success_embed("Backup Created")
            embed.add_field(name="📦 Container", value=f"```fix\n{self.container}\n```", inline=True)
            embed.add_field(name="💾 Backup", value=f"```fix\n{backup_name}\n```", inline=True)
            await interaction.followup.send(embed=embed, ephemeral=True)
        else:
            await interaction.followup.send(embed=error_embed("Backup Failed", f"```diff\n- {err}\n```"), ephemeral=True)
    
    async def restore_callback(self, interaction):
        snapshots = get_snapshots(self.container)
        if not snapshots:
            return await interaction.response.send_message(embed=error_embed("No Backups"), ephemeral=True)
        
        options = []
        for s in snapshots[:10]:
            options.append(discord.SelectOption(label=s['snapshot_name'], value=s['snapshot_name']))
        
        view = View()
        select = Select(placeholder="Select backup...", options=options)
        
        async def select_cb(sel_interaction):
            snap_name = select.values[0]
            await sel_interaction.response.defer()
            msg = await sel_interaction.followup.send(embed=info_embed("Restoring", f"```fix\n{self.container} from {snap_name}...\n```"), ephemeral=True)
            
            status = await get_container_status(self.container)
            if status == 'running':
                await run_lxc(f"lxc stop {self.container} --force")
            out, err, code = await run_lxc(f"lxc restore {self.container} {snap_name}")
            if code == 0:
                await run_lxc(f"lxc start {self.container}")
                await msg.edit(embed=success_embed("Restored", f"```fix\n{self.container} restored from {snap_name}\n```"))
            else:
                await msg.edit(embed=error_embed("Restore Failed", f"```diff\n- {err}\n```"))
        
        select.callback = select_cb
        view.add_item(select)
        await interaction.response.send_message(embed=info_embed("Select Backup"), view=view, ephemeral=True)
    
    async def delete_callback(self, interaction):
        view = ConfirmationView(self.ctx, self.container, self)
        embed = warning_embed("⚠️ Confirm Delete", f"```fix\nContainer: {self.container}\n\n⚠️ This will permanently delete your VPS and all data!\n```")
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    
    async def refresh_callback(self, interaction):
        embed = await self.get_stats_embed()
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def close_callback(self, interaction):
        await interaction.message.delete()


class ConfirmationView(View):
    def __init__(self, ctx, container, parent_view):
        super().__init__(timeout=60)
        self.ctx = ctx
        self.container = container
        self.parent_view = parent_view
        
        confirm_btn = Button(label="✅ Confirm Delete", style=discord.ButtonStyle.danger)
        cancel_btn = Button(label="❌ Cancel", style=discord.ButtonStyle.secondary)
        
        confirm_btn.callback = self.confirm_callback
        cancel_btn.callback = self.cancel_callback
        
        self.add_item(confirm_btn)
        self.add_item(cancel_btn)
    
    async def confirm_callback(self, interaction):
        await interaction.response.defer()
        
        status = await get_container_status(self.container)
        if status == 'running':
            await run_lxc(f"lxc stop {self.container} --force")
        
        await run_lxc(f"lxc delete {self.container}")
        delete_vps(self.container)
        
        await interaction.followup.send(embed=success_embed("Deleted", f"```fix\n{self.container} has been deleted.\n```"), ephemeral=True)
        
        if self.parent_view.message:
            await self.parent_view.message.delete()
    
    async def cancel_callback(self, interaction):
        await interaction.response.edit_message(embed=info_embed("Cancelled"), view=None)


class CommandModal(Modal):
    def __init__(self, container):
        super().__init__(title="Run Command")
        self.container = container
        self.add_item(InputText(label="Command", placeholder="e.g., apt update", style=discord.InputTextStyle.paragraph))
        self.add_item(InputText(label="Timeout (seconds)", placeholder="30", required=False, value="30"))
    
    async def callback(self, interaction):
        cmd = self.children[0].value
        timeout = int(self.children[1].value or "30")
        await interaction.response.defer()
        msg = await interaction.followup.send(embed=info_embed("Executing", f"```fix\n$ {cmd}\n```"), ephemeral=True)
        out, err, code = await exec_in_container(self.container, cmd, timeout)
        embed = terminal_embed("Output", f"$ {cmd}\n\n{(out or err)[:1900]}")
        embed.add_field(name="Exit Code", value=f"```fix\n{code}\n```")
        await msg.edit(embed=embed)


# ==================================================================================================
#  📦  CLAIM FREE VPS VIEW
# ==================================================================================================

class ClaimFreeView(View):
    def __init__(self, ctx, plan):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.plan = plan
        
        options = []
        for os in OS_OPTIONS[:25]:
            options.append(discord.SelectOption(
                label=os['label'][:100],
                value=os['value'],
                description=os['desc'][:100] if os.get('desc') else None
            ))
        
        self.select = Select(placeholder="Select an operating system...", options=options)
        self.select.callback = self.select_callback
        self.add_item(self.select)
        
        cancel_btn = Button(label="❌ Cancel", style=discord.ButtonStyle.secondary)
        cancel_btn.callback = self.cancel_callback
        self.add_item(cancel_btn)
    
    async def select_callback(self, interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("Not for you!", ephemeral=True)
            return
        
        selected_os = self.select.values[0]
        os_name = next((o['label'] for o in OS_OPTIONS if o['value'] == selected_os), selected_os)
        
        view = ConfirmClaimView(self.ctx, self.plan, selected_os, os_name)
        embed = warning_embed(
            "Confirm VPS Claim",
            f"```fix\nPlan: {self.plan['emoji']} {self.plan['name']}\nOS: {os_name}\nRAM: {self.plan['ram']}GB\nCPU: {self.plan['cpu']} Core(s)\nDisk: {self.plan['disk']}GB\nCost: {self.plan['invites']} invites\n```\n\nThis will use {self.plan['invites']} invites from your account!"
        )
        await interaction.response.edit_message(embed=embed, view=view)
    
    async def cancel_callback(self, interaction):
        await interaction.response.edit_message(embed=info_embed("Cancelled"), view=None)


class ConfirmClaimView(View):
    def __init__(self, ctx, plan, os_version, os_name):
        super().__init__(timeout=120)
        self.ctx = ctx
        self.plan = plan
        self.os_version = os_version
        self.os_name = os_name
        
        confirm_btn = Button(label="✅ Confirm Claim", style=discord.ButtonStyle.success)
        cancel_btn = Button(label="❌ Cancel", style=discord.ButtonStyle.secondary)
        
        confirm_btn.callback = self.confirm_callback
        cancel_btn.callback = self.cancel_callback
        
        self.add_item(confirm_btn)
        self.add_item(cancel_btn)
    
    async def confirm_callback(self, interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("Not for you!", ephemeral=True)
            return
        await self.create_vps(interaction)
    
    async def cancel_callback(self, interaction):
        await interaction.response.edit_message(embed=info_embed("Cancelled"), view=None)
    
    async def create_vps(self, interaction):
        await interaction.response.defer()
        
        user_id = str(self.ctx.author.id)
        container_name = f"nex-{user_id[:6]}-{random.randint(1000, 9999)}"
        
        progress_msg = await interaction.followup.send(
            embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description="```fix\n[░░░░░░░░░░░░░░░░░░░░] 0% | Initializing...\n```",
                color=RAINBOW_COLORS[0]
            ),
            ephemeral=True
        )
        
        def get_progress_bar(percent):
            filled = int(percent / 5)
            return "█" * filled + "░" * (20 - filled)
        
        try:
            ram_mb = self.plan['ram'] * 1024
            
            # Step 1: Initialize
            await progress_msg.edit(embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description=f"```fix\n[{get_progress_bar(20)}] 20% | 🔧 Initializing container...\n```",
                color=RAINBOW_COLORS[1]
            ))
            await run_lxc(f"lxc init {self.os_version} {container_name} -s {DEFAULT_STORAGE_POOL}")
            await asyncio.sleep(1)
            
            # Step 2: Set RAM
            await progress_msg.edit(embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description=f"```fix\n[{get_progress_bar(40)}] 40% | 💾 Setting RAM ({self.plan['ram']}GB)...\n```",
                color=RAINBOW_COLORS[2]
            ))
            await run_lxc(f"lxc config set {container_name} limits.memory {ram_mb}MB")
            await asyncio.sleep(1)
            
            # Step 3: Set CPU
            await progress_msg.edit(embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description=f"```fix\n[{get_progress_bar(60)}] 60% | ⚡ Setting CPU ({self.plan['cpu']} cores)...\n```",
                color=RAINBOW_COLORS[3]
            ))
            await run_lxc(f"lxc config set {container_name} limits.cpu {self.plan['cpu']}")
            await asyncio.sleep(1)
            
            # Step 4: Set Disk
            await progress_msg.edit(embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description=f"```fix\n[{get_progress_bar(80)}] 80% | 💽 Setting Disk ({self.plan['disk']}GB)...\n```",
                color=RAINBOW_COLORS[4]
            ))
            await run_lxc(f"lxc config device set {container_name} root size={self.plan['disk']}GB")
            await asyncio.sleep(1)
            
            # Step 5: Apply config
            await progress_msg.edit(embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description=f"```fix\n[{get_progress_bar(90)}] 90% | 🔨 Applying configuration...\n```",
                color=RAINBOW_COLORS[5]
            ))
            await apply_lxc_config(container_name)
            await asyncio.sleep(1)
            
            # Step 6: Start container
            await progress_msg.edit(embed=discord.Embed(
                title="```glow\n🌈 NEX VM V1 - CREATING VPS 🌈\n```",
                description=f"```fix\n[{get_progress_bar(100)}] 100% | ▶️ Starting container...\n```",
                color=RAINBOW_COLORS[6]
            ))
            await run_lxc(f"lxc start {container_name}")
            await asyncio.sleep(3)
            
            # Apply internal permissions
            await apply_internal_permissions(container_name)
            
            # Get IP and MAC
            ip = "N/A"
            mac = "N/A"
            try:
                out, _, _ = await exec_in_container(container_name, "ip -4 addr show eth0 | grep -oP '(?<=inet\\s)[0-9.]+' | head -1")
                ip = out.strip() if out else "N/A"
                out, _, _ = await exec_in_container(container_name, "ip link | grep ether | awk '{print $2}' | head -1")
                mac = out.strip() if out else "N/A"
            except:
                pass
            
            # Save to database
            add_vps(user_id, container_name, self.plan['ram'], self.plan['cpu'], self.plan['disk'], self.os_version, self.plan['name'])
            
            # Update VPS with IP and MAC
            conn = get_db()
            cur = conn.cursor()
            cur.execute('UPDATE vps SET ip_address = ?, mac_address = ? WHERE container_name = ?', (ip, mac, container_name))
            conn.commit()
            conn.close()
            
            # Update user stats
            stats = get_user_stats(user_id)
            update_user_stats(user_id, invites=-self.plan['invites'], claimed=1)
            
            # Success Embed
            success_embed = discord.Embed(
                title="```glow\n🌟 VPS CREATED SUCCESSFULLY! 🌟\n```",
                description=f"🎉 Congratulations {self.ctx.author.mention}! Your VPS is ready!\n\n"
                            f"```glow\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n```",
                color=0x00FF88
            )
            success_embed.set_thumbnail(url=THUMBNAIL_URL)
            
            success_embed.add_field(
                name="📦 CONTAINER",
                value=f"```fix\nName: {container_name}\nIP: {ip}\nMAC: {mac}\nOS: {self.os_name}\nPlan: {self.plan['emoji']} {self.plan['name']}\n```",
                inline=False
            )
            
            success_embed.add_field(
                name="⚙️ RESOURCES",
                value=f"```fix\nRAM: {self.plan['ram']}GB\nCPU: {self.plan['cpu']} Core(s)\nDisk: {self.plan['disk']}GB\n```",
                inline=True
            )
            
            success_embed.add_field(
                name="🖥️ COMMANDS",
                value=f"```fix\n.manage {container_name}\n.stats {container_name}\n.ssh-gen {container_name}\n```",
                inline=False
            )
            
            await progress_msg.edit(embed=success_embed)
            
            # DM user
            try:
                dm = success_embed("Your VPS is Ready!")
                dm.add_field(name="Container", value=f"```fix\n{container_name}\n```", inline=True)
                dm.add_field(name="IP", value=f"```fix\n{ip}\n```", inline=True)
                dm.add_field(name="Resources", value=f"```fix\nRAM: {self.plan['ram']}GB | CPU: {self.plan['cpu']}\n```", inline=False)
                await self.ctx.author.send(embed=dm)
            except:
                pass
            
            logger.info(f"User {self.ctx.author} claimed VPS {container_name}")
            
        except Exception as e:
            await progress_msg.edit(embed=error_embed("Creation Failed", f"```diff\n- {str(e)}\n```"))


# ==================================================================================================
#  📚  HELP COMMAND
# ==================================================================================================

class HelpView(View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.current_category = "home"
        
        options = [
            discord.SelectOption(label="🏠 Home", value="home", description="Main menu"),
            discord.SelectOption(label="👤 User Commands", value="user", description="User commands"),
            discord.SelectOption(label="🖥️ VPS Commands", value="vps", description="VPS management"),
            discord.SelectOption(label="🎮 Games Commands", value="games", description="Game servers"),
            discord.SelectOption(label="🛠️ Tools Commands", value="tools", description="Development tools"),
            discord.SelectOption(label="💰 Plans", value="plans", description="VPS plans"),
        ]
        
        self.select = Select(placeholder="Select a category...", options=options)
        self.select.callback = self.select_callback
        self.add_item(self.select)
        
        close_btn = Button(label="❌ Close", style=discord.ButtonStyle.danger)
        close_btn.callback = self.close_callback
        self.add_item(close_btn)
        
        self.update_embed()
    
    def update_embed(self):
        categories = {
            'home': {
                'title': "🏠 NEX VM V1 - Help Center",
                'desc': f"```glow\nWelcome to {BOT_NAME} - Complete VPS Management Solution\n```\nSelect a category from the dropdown menu.",
                'fields': [
                    ("📌 Getting Started", "Use `.plans` to view available plans\nUse `.claim-free` to get a free VPS", False),
                    ("🔑 License", f"Use `.license-verify <key>` to activate\nValid keys: prime2026, preimdragon, gamerhindu", False),
                ]
            },
            'user': {
                'title': "👤 User Commands",
                'desc': "```fix\nBasic commands for all users\n```",
                'fields': [
                    (".help", "Show this help menu", False),
                    (".ping", "Check bot latency", False),
                    (".plans", "View available VPS plans", False),
                    (".claim-free", "Claim a free VPS", False),
                    (".myvps", "List your VPS containers", False),
                    (".stats", "View your statistics", False),
                    (".inv", "Check your invites", False),
                    (".userinfo", "View user information", False),
                ]
            },
            'vps': {
                'title': "🖥️ VPS Commands",
                'desc': "```fix\nManage your VPS containers\n```",
                'fields': [
                    (".manage <container>", "Interactive VPS manager", False),
                    (".start <container>", "Start a VPS", False),
                    (".stop <container>", "Stop a VPS", False),
                    (".restart <container>", "Restart a VPS", False),
                    (".stats <container>", "View VPS statistics", False),
                    (".logs <container>", "View VPS logs", False),
                    (".ssh-gen <container>", "Generate SSH access", False),
                ]
            },
            'games': {
                'title': "🎮 Games Commands",
                'desc': "```fix\nInstall and manage game servers\n```",
                'fields': [
                    (".games", "List available games", False),
                    (".game-info <game>", "Game information", False),
                    (".install-game <container> <game>", "Install game", False),
                    (".my-games", "Your installed games", False),
                ]
            },
            'tools': {
                'title': "🛠️ Tools Commands",
                'desc': "```fix\nInstall development tools\n```",
                'fields': [
                    (".tools", "List available tools", False),
                    (".tool-info <tool>", "Tool information", False),
                    (".install-tool <container> <tool>", "Install tool", False),
                    (".my-tools", "Your installed tools", False),
                ]
            },
            'plans': {
                'title': "💰 VPS Plans",
                'desc': "```fix\nFree VPS plans based on invites\n```",
                'fields': [
                    ("🥉 Bronze (5 invites)", "2GB RAM, 1 CPU, 20GB Disk", False),
                    ("🥈 Silver (10 invites)", "4GB RAM, 2 CPU, 40GB Disk", False),
                    ("🥇 Gold (15 invites)", "8GB RAM, 4 CPU, 80GB Disk", False),
                    ("🏆 Platinum (20 invites)", "16GB RAM, 8 CPU, 160GB Disk", False),
                    ("💎 Diamond (25 invites)", "32GB RAM, 16 CPU, 320GB Disk", False),
                ]
            }
        }
        
        cat_data = categories.get(self.current_category, categories['home'])
        
        embed = discord.Embed(
            title=f"```glow\n{cat_data['title']}\n```",
            description=cat_data['desc'],
            color=COLORS['primary']
        )
        embed.set_thumbnail(url=THUMBNAIL_URL)
        
        for name, value, inline in cat_data['fields']:
            embed.add_field(name=name, value=value, inline=inline)
        
        embed.set_footer(text=f"⚡ {BOT_NAME} • Use dropdown to navigate ⚡", icon_url=THUMBNAIL_URL)
        self.embed = embed
    
    async def select_callback(self, interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("Not for you!", ephemeral=True)
            return
        self.current_category = self.select.values[0]
        self.update_embed()
        await interaction.response.edit_message(embed=self.embed, view=self)
    
    async def close_callback(self, interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("Not for you!", ephemeral=True)
            return
        await interaction.message.delete()


# ==================================================================================================
#  👤  USER COMMANDS
# ==================================================================================================

@bot.command(name="help")
async def help_cmd(ctx):
    if not LICENSE_VERIFIED and not is_admin(str(ctx.author.id)):
        return await ctx.send(embed=error_embed("License Required", "Please verify license first."))
    view = HelpView(ctx)
    await ctx.send(embed=view.embed, view=view)


@bot.command(name="ping")
async def ping(ctx):
    start = time.time()
    msg = await ctx.send(embed=info_embed("Pinging..."))
    end = time.time()
    embed = success_embed("Pong! 🏓")
    embed.add_field(name="📡 API", value=f"```fix\n{round(bot.latency*1000)}ms\n```", inline=True)
    embed.add_field(name="⏱️ Response", value=f"```fix\n{round((end-start)*1000)}ms\n```", inline=True)
    await msg.edit(embed=embed)


@bot.command(name="plans")
async def plans(ctx):
    embed = info_embed("Free VPS Plans")
    for p in FREE_VPS_PLANS['invites']:
        embed.add_field(
            name=f"{p['emoji']} {p['name']}",
            value=f"```fix\nRAM: {p['ram']}GB | CPU: {p['cpu']} | Disk: {p['disk']}GB\nInvites: {p['invites']}\n```",
            inline=True
        )
    await ctx.send(embed=embed)


@bot.command(name="stats")
async def user_stats(ctx):
    stats = get_user_stats(str(ctx.author.id))
    vps_count = len(get_user_vps(str(ctx.author.id)))
    
    embed = info_embed("Your Statistics")
    embed.add_field(name="📨 Invites", value=f"```fix\n{stats.get('invites', 0)}\n```", inline=True)
    embed.add_field(name="🖥️ VPS Count", value=f"```fix\n{vps_count}\n```", inline=True)
    embed.add_field(name="🔑 API Key", value=f"```fix\n{stats.get('api_key', 'None')}\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="inv")
async def inv(ctx):
    stats = get_user_stats(str(ctx.author.id))
    await ctx.send(embed=info_embed("Your Invites", f"```fix\n{stats.get('invites', 0)}\n```"))


@bot.command(name="userinfo")
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    elif not is_admin(str(ctx.author.id)) and user.id != ctx.author.id:
        return await ctx.send(embed=error_embed("Access Denied", "You can only view yourself."))
    
    uid = str(user.id)
    vps = get_user_vps(uid)
    stats = get_user_stats(uid)
    
    embed = info_embed(f"User: {user.display_name}")
    embed.set_thumbnail(url=user.avatar.url if user.avatar else THUMBNAIL_URL)
    embed.add_field(name="🆔 ID", value=f"```fix\n{user.id}\n```", inline=True)
    embed.add_field(name="📨 Invites", value=f"```fix\n{stats.get('invites', 0)}\n```", inline=True)
    embed.add_field(name="🖥️ VPS", value=f"```fix\n{len(vps)}\n```", inline=True)
    
    if vps:
        text = "\n".join([f"{'🟢' if v['status']=='running' else '🔴'} `{v['container_name']}`" for v in vps[:3]])
        embed.add_field(name="📋 VPS List", value=text, inline=False)
    
    await ctx.send(embed=embed)


@bot.command(name="claim-free")
async def claim_free(ctx):
    user_id = str(ctx.author.id)
    
    user_vps = get_user_vps(user_id)
    if user_vps:
        return await ctx.send(embed=error_embed("VPS Already Exists", "You already have a VPS. Each user can only claim one free VPS."))
    
    stats = get_user_stats(user_id)
    invites = stats.get('invites', 0)
    
    eligible_plan = None
    for plan in reversed(FREE_VPS_PLANS['invites']):
        if invites >= plan['invites']:
            eligible_plan = plan
            break
    
    if not eligible_plan:
        return await ctx.send(embed=error_embed("No Eligible Plans", f"You have {invites} invites. Need at least 5 invites to claim a VPS."))
    
    embed = info_embed(f"Claim {eligible_plan['emoji']} {eligible_plan['name']} Plan")
    embed.add_field(name="📋 Plan Details", value=f"```fix\nRAM: {eligible_plan['ram']}GB\nCPU: {eligible_plan['cpu']} Core(s)\nDisk: {eligible_plan['disk']}GB\nCost: {eligible_plan['invites']} invites\n```", inline=False)
    embed.add_field(name="📊 Your Stats", value=f"```fix\nYour Invites: {invites}\nAfter Claim: {invites - eligible_plan['invites']}\n```", inline=False)
    
    view = ClaimFreeView(ctx, eligible_plan)
    await ctx.send(embed=embed, view=view)


# ==================================================================================================
#  🖥️  VPS COMMANDS
# ==================================================================================================

@bot.command(name="myvps")
async def myvps(ctx):
    vps = get_user_vps(str(ctx.author.id))
    if not vps:
        return await ctx.send(embed=no_vps_embed())
    
    embed = info_embed(f"Your VPS ({len(vps)})")
    for i, v in enumerate(vps, 1):
        status = "🟢" if v['status'] == 'running' else "🔴"
        text = f"{status} **`{v['container_name']}`**\n```fix\nRAM: {v['ram']}GB | CPU: {v['cpu']} | Disk: {v['disk']}GB\nIP: {v.get('ip_address', 'N/A')}\nOS: {v.get('os_version', 'N/A')}\n```"
        embed.add_field(name=f"VPS #{i}", value=text, inline=False)
    await ctx.send(embed=embed)


@bot.command(name="manage")
async def manage(ctx, container_name: str = None):
    user_id = str(ctx.author.id)
    
    if not container_name:
        vps_list = get_user_vps(user_id)
        if not vps_list:
            return await ctx.send(embed=no_vps_embed())
        container_name = vps_list[0]['container_name']
        container_data = vps_list[0]
    else:
        vps_list = get_user_vps(user_id)
        container_data = next((v for v in vps_list if v['container_name'] == container_name), None)
        if not container_data:
            return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    view = VPSManageView(ctx, container_name, container_data)
    embed = await view.get_stats_embed()
    await ctx.send(embed=embed, view=view)


@bot.command(name="start")
async def start_vps(ctx, container_name: str):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    await run_lxc(f"lxc start {container_name}")
    update_vps_status(container_name, 'running')
    await ctx.send(embed=success_embed("Started", f"```fix\n{container_name} started!\n```"))


@bot.command(name="stop")
async def stop_vps(ctx, container_name: str):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    await run_lxc(f"lxc stop {container_name}")
    update_vps_status(container_name, 'stopped')
    await ctx.send(embed=success_embed("Stopped", f"```fix\n{container_name} stopped.\n```"))


@bot.command(name="restart")
async def restart_vps(ctx, container_name: str):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    await run_lxc(f"lxc restart {container_name}")
    update_vps_status(container_name, 'running')
    await ctx.send(embed=success_embed("Restarted", f"```fix\n{container_name} restarted.\n```"))


@bot.command(name="logs")
async def vps_logs(ctx, container_name: str, lines: int = 50):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    lines = min(lines, 200)
    out, _, _ = await exec_in_container(container_name, f"journalctl -n {lines} --no-pager 2>/dev/null || dmesg | tail -{lines}")
    embed = terminal_embed(f"Logs: {container_name}", out[:1900])
    await ctx.send(embed=embed)


@bot.command(name="ssh-gen")
async def ssh_gen(ctx, container_name: str):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    status = await get_container_status(container_name)
    if status != 'running':
        return await ctx.send(embed=error_embed("Not Running", f"```diff\n- {container_name} is not running.\n```"))
    
    msg = await ctx.send(embed=info_embed("Generating SSH", f"```fix\n{container_name}\n```"))
    
    try:
        await exec_in_container(container_name, "apt-get update -qq && apt-get install -y -qq tmate")
        session = f"nex-{random.randint(1000, 9999)}"
        await exec_in_container(container_name, f"tmate -S /tmp/{session}.sock new-session -d")
        await asyncio.sleep(5)
        out, _, _ = await exec_in_container(container_name, f"tmate -S /tmp/{session}.sock display -p '#{{tmate_ssh}}'")
        url = out.strip()
        
        if url:
            embed = success_embed("🔑 SSH Access Generated")
            embed.add_field(name="Container", value=f"```fix\n{container_name}\n```", inline=True)
            embed.add_field(name="Command", value=f"```bash\n{url}\n```", inline=False)
            embed.add_field(name="⚠️ Note", value="This link expires in 15 minutes. Do not share!", inline=False)
            await msg.edit(embed=embed)
            
            try:
                await ctx.author.send(embed=embed)
            except:
                pass
        else:
            await msg.edit(embed=error_embed("Failed", "Could not generate SSH access."))
    except Exception as e:
        await msg.edit(embed=error_embed("Failed", f"```diff\n- {str(e)}\n```"))


# ==================================================================================================
#  🎮  GAMES COMMANDS
# ==================================================================================================

@bot.command(name="games")
async def list_games(ctx):
    embed = info_embed("Available Games", f"```fix\nTotal: {len(GAMES_LIST)}\n```")
    for g in GAMES_LIST:
        embed.add_field(
            name=f"{g['icon']} {g['name']}",
            value=f"```fix\nPort: {g['port']} | RAM: {g['ram']}MB\n```",
            inline=True
        )
    await ctx.send(embed=embed)


@bot.command(name="install-game")
async def install_game(ctx, container_name: str, *, game_name: str):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    game = next((g for g in GAMES_LIST if g['name'].lower() == game_name.lower()), None)
    if not game:
        return await ctx.send(embed=error_embed("Game Not Found", f"```diff\n- {game_name}\n```"))
    
    msg = await ctx.send(embed=info_embed("Installing Game", f"```fix\n{game['name']} on {container_name}\n```"))
    
    await exec_in_container(container_name, "which docker || curl -fsSL https://get.docker.com | bash")
    cmd = f"docker run -d --name {game['name'].lower().replace(' ', '-')} -p {game['port']}:{game['port']} {game['docker']}"
    out, err, code = await exec_in_container(container_name, cmd)
    
    if code == 0:
        add_game_install(user_id, container_name, game['name'], game['port'])
        embed = success_embed("Game Installed")
        embed.add_field(name="🎮 Game", value=f"```fix\n{game['name']}\n```", inline=True)
        embed.add_field(name="🔌 Port", value=f"```fix\n{game['port']}\n```", inline=True)
        await msg.edit(embed=embed)
    else:
        await msg.edit(embed=error_embed("Failed", f"```diff\n- {err}\n```"))


@bot.command(name="my-games")
async def my_games(ctx, container_name: str = None):
    user_id = str(ctx.author.id)
    conn = get_db()
    cur = conn.cursor()
    
    if container_name:
        cur.execute('SELECT * FROM installed_games WHERE user_id = ? AND container_name = ?', (user_id, container_name))
    else:
        cur.execute('SELECT * FROM installed_games WHERE user_id = ?', (user_id,))
    
    rows = cur.fetchall()
    conn.close()
    
    if not rows:
        return await ctx.send(embed=info_embed("No Games", "No games installed."))
    
    embed = info_embed("Your Installed Games")
    for row in rows:
        embed.add_field(
            name=f"🎮 {row['game_name']}",
            value=f"```fix\nContainer: {row['container_name']}\nPort: {row['game_port']}\n```",
            inline=False
        )
    await ctx.send(embed=embed)


# ==================================================================================================
#  🛠️  TOOLS COMMANDS
# ==================================================================================================

@bot.command(name="tools")
async def list_tools(ctx):
    embed = info_embed("Available Tools", f"```fix\nTotal: {len(TOOLS_LIST)}\n```")
    for t in TOOLS_LIST:
        embed.add_field(
            name=f"{t['icon']} {t['name']}",
            value=f"```fix\nPort: {t.get('port', 'None')}\n```",
            inline=True
        )
    await ctx.send(embed=embed)


@bot.command(name="install-tool")
async def install_tool(ctx, container_name: str, *, tool_name: str):
    user_id = str(ctx.author.id)
    if not any(v['container_name'] == container_name for v in get_user_vps(user_id)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    tool = next((t for t in TOOLS_LIST if t['name'].lower() == tool_name.lower()), None)
    if not tool:
        return await ctx.send(embed=error_embed("Tool Not Found", f"```diff\n- {tool_name}\n```"))
    
    msg = await ctx.send(embed=info_embed("Installing Tool", f"```fix\n{tool['name']} on {container_name}\n```"))
    out, err, code = await exec_in_container(container_name, tool['cmd'])
    
    if code == 0 or "already" in err.lower():
        add_tool_install(user_id, container_name, tool['name'], tool.get('port'))
        embed = success_embed("Tool Installed")
        embed.add_field(name="🛠️ Tool", value=f"```fix\n{tool['name']}\n```", inline=True)
        embed.add_field(name="📦 Container", value=f"```fix\n{container_name}\n```", inline=True)
        await msg.edit(embed=embed)
    else:
        await msg.edit(embed=error_embed("Failed", f"```diff\n- {err}\n```"))


@bot.command(name="my-tools")
async def my_tools(ctx, container_name: str = None):
    user_id = str(ctx.author.id)
    conn = get_db()
    cur = conn.cursor()
    
    if container_name:
        cur.execute('SELECT * FROM installed_tools WHERE user_id = ? AND container_name = ?', (user_id, container_name))
    else:
        cur.execute('SELECT * FROM installed_tools WHERE user_id = ?', (user_id,))
    
    rows = cur.fetchall()
    conn.close()
    
    if not rows:
        return await ctx.send(embed=info_embed("No Tools", "No tools installed."))
    
    embed = info_embed("Your Installed Tools")
    for row in rows:
        embed.add_field(
            name=f"🛠️ {row['tool_name']}",
            value=f"```fix\nContainer: {row['container_name']}\nPort: {row['tool_port'] or 'None'}\n```",
            inline=False
        )
    await ctx.send(embed=embed)


# ==================================================================================================
#  🔐  LICENSE COMMANDS
# ==================================================================================================

@bot.command(name="license-verify")
async def license_verify(ctx, key: str = None):
    global LICENSE_VERIFIED
    
    if key is None:
        if LICENSE_VERIFIED:
            embed = success_embed("License Verified", "```fix\nYour license is active.\n```")
        else:
            embed = warning_embed("License Required", "```fix\nNo valid license found.\n```")
            embed.add_field(
                name="📌 Valid License Keys",
                value="```fix\nprime2026\npreimdragon\ngamerhindu\n```",
                inline=False
            )
        return await ctx.send(embed=embed)
    
    if key in VALID_LICENSE_KEYS:
        set_setting('license_verified', 'true')
        LICENSE_VERIFIED = True
        
        embed = success_embed("✅ License Verified!")
        embed.add_field(name="🔑 Key", value=f"```fix\n{key}\n```", inline=True)
        embed.add_field(name="👤 Activated By", value=ctx.author.mention, inline=True)
        await ctx.send(embed=embed)
        logger.info(f"License verified by {ctx.author} with key: {key}")
    else:
        await ctx.send(embed=error_embed("Invalid License", f"```diff\n- '{key}' is not valid.\n```"))


@bot.command(name="license-status")
async def license_status(ctx):
    if LICENSE_VERIFIED:
        embed = success_embed("License Status", "```fix\nLicense is active.\n```")
    else:
        embed = warning_embed("License Status", "```fix\nNo active license.\n```")
        embed.add_field(name="📌 Activate", value=f"Use `{BOT_PREFIX}license-verify <key>`", inline=False)
    await ctx.send(embed=embed)


# ==================================================================================================
#  👑  ADMIN COMMANDS
# ==================================================================================================

@bot.command(name="add-inv")
@commands.check(lambda ctx: is_admin(str(ctx.author.id)))
async def add_invites(ctx, user: discord.Member, amount: int):
    if amount <= 0:
        return await ctx.send(embed=error_embed("Invalid", "Amount must be positive."))
    
    update_user_stats(str(user.id), invites=amount)
    await ctx.send(embed=success_embed("Invites Added", f"```fix\n+{amount} invites to {user.name}\n```"))


@bot.command(name="list-all")
@commands.check(lambda ctx: is_admin(str(ctx.author.id)))
async def list_all_vps(ctx):
    all_vps = get_all_vps()
    if not all_vps:
        return await ctx.send(embed=info_embed("No VPS", "No VPS in system."))
    
    by_user = {}
    for v in all_vps:
        if v['user_id'] not in by_user:
            by_user[v['user_id']] = []
        by_user[v['user_id']].append(v)
    
    embed = info_embed(f"All VPS ({len(all_vps)})")
    for uid, vlist in list(by_user.items())[:10]:
        try:
            user = await bot.fetch_user(int(uid))
            name = user.name
        except:
            name = f"Unknown ({uid[:8]})"
        
        text = "\n".join([f"{'🟢' if v['status']=='running' else '🔴'} `{v['container_name']}` ({v['ram']}GB)" for v in vlist[:3]])
        embed.add_field(name=f"{name} ({len(vlist)})", value=text, inline=False)
    
    await ctx.send(embed=embed)


@bot.command(name="server-stats")
@commands.check(lambda ctx: is_admin(str(ctx.author.id)))
async def server_stats(ctx):
    all_vps = get_all_vps()
    total_ram = sum(v['ram'] for v in all_vps)
    total_cpu = sum(v['cpu'] for v in all_vps)
    total_disk = sum(v['disk'] for v in all_vps)
    active_vps = len([v for v in all_vps if v['status'] == 'running'])
    
    embed = info_embed("Server Statistics")
    embed.add_field(name="🖥️ Total VPS", value=f"```fix\n{len(all_vps)}\n```", inline=True)
    embed.add_field(name="🟢 Active VPS", value=f"```fix\n{active_vps}\n```", inline=True)
    embed.add_field(name="💾 Total RAM", value=f"```fix\n{total_ram}GB\n```", inline=True)
    embed.add_field(name="⚡ Total CPU", value=f"```fix\n{total_cpu} cores\n```", inline=True)
    embed.add_field(name="💽 Total Disk", value=f"```fix\n{total_disk}GB\n```", inline=True)
    await ctx.send(embed=embed)


# ==================================================================================================
#  ✅  ON READY EVENT
# ==================================================================================================

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{BOT_PREFIX}help | {BOT_NAME}"
        )
    )
    logger.info(f"✅ Bot is ready: {bot.user}")
    update_local_node_stats()
    
    total_vps = len(get_all_vps())
    
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                      ███████╗██╗   ██╗███╗   ███╗                            ║
║                      ██╔════╝██║   ██║████╗ ████║                            ║
║                      ███████╗██║   ██║██╔████╔██║                            ║
║                      ╚════██║╚██╗ ██╔╝██║╚██╔╝██║                            ║
║                      ███████║ ╚████╔╝ ██║ ╚═╝ ██║                            ║
║                      ╚══════╝  ╚═══╝  ╚═╝     ╚═╝                            ║
║                                                                               ║
║                         Made by DeVv-prime with ❤️                            ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  📍 Bot Status:    🟢 ONLINE                                                 ║
║  🤖 Bot Name:      {bot.user}                                                ║
║  🔧 Prefix:        {BOT_PREFIX}                                              ║
║  🔐 License:       {'✅ VERIFIED' if LICENSE_VERIFIED else '❌ NOT VERIFIED'} ║
║  🌐 Server IP:     {SERVER_IP}                                               ║
║                                                                               ║
║  🖥️ Total VPS:     {total_vps}                                               ║
║  🐧 Total OS:      {len(OS_OPTIONS)}                                          ║
║  🎮 Total Games:   {len(GAMES_LIST)}                                          ║
║  🛠️ Total Tools:   {len(TOOLS_LIST)}                                          ║
║                                                                               ║
║  📊 UPI: vedant1437@fam | Discord: https://discord.gg/zS2ynbF6jK             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)


# ==================================================================================================
#  ❌  ERROR HANDLER
# ==================================================================================================

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=error_embed("Missing Argument", f"Usage: `{BOT_PREFIX}{ctx.command.name} {ctx.command.signature}`"))
    elif isinstance(error, commands.BadArgument):
        await ctx.send(embed=error_embed("Invalid Argument", "Please check your input."))
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(embed=error_embed("Access Denied", "You don't have permission."))
    else:
        logger.error(f"Command error: {error}")
        await ctx.send(embed=error_embed("Error", f"```diff\n- {str(error)[:1900]}\n```"))


# ==================================================================================================
#  🚀  RUN THE BOT
# ==================================================================================================

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_DISCORD_BOT_TOKEN_HERE":
        print("\n❌ ERROR: Please set your BOT_TOKEN in the script!")
        print("📍 Edit the BOT_TOKEN variable at the top of the script.")
        sys.exit(1)
    
    update_local_node_stats()
    
    try:
        bot.run(BOT_TOKEN)
    except discord.LoginFailure:
        print("\n❌ ERROR: Invalid Discord bot token!")
        print("📍 Please check your BOT_TOKEN and try again.")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

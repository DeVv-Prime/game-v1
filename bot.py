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
import base64
import uuid
import qrcode
import base64
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

os.makedirs('/opt/nex-bot/logs', exist_ok=True)
os.makedirs('/opt/nex-bot/data', exist_ok=True)
os.makedirs('/opt/nex-bot/backups', exist_ok=True)
os.makedirs('/opt/nex-bot/qr_codes', exist_ok=True)
os.makedirs('/opt/nex-bot/nodes', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('/opt/nex-bot/logs/svm5.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("NEXVMV1-BOT")

# ==================================================================================================
#  ⚙️  CONFIGURATION
# ==================================================================================================

BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"
BOT_PREFIX = "."
BOT_NAME = "NEXVMV1-BOT"
BOT_AUTHOR = "DeVv-Prime"
MAIN_ADMIN_IDS = [1405866008127864852]
DEFAULT_STORAGE_POOL = "default"

# Auto-detect server
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

# License Keys - UPDATED
VALID_LICENSE_KEYS = ["prime2026", "preimdragon", "gamerhindu"]

# ==================================================================================================
#  🐧  OS OPTIONS - 70+ OPERATING SYSTEMS
# ==================================================================================================

OS_OPTIONS = [
    # ==============================================================================================
    # 🐧 UBUNTU SERIES (15 versions)
    # ==============================================================================================
    {"label": "🐧 Ubuntu 24.04 LTS", "value": "ubuntu:24.04", "desc": "Noble Numbat - Latest LTS (April 2024)", "category": "Ubuntu", "icon": "🐧", "popular": True, "ram_min": 1024},
    {"label": "🐧 Ubuntu 23.10", "value": "ubuntu:23.10", "desc": "Mantic Minotaur - Latest (EOL Oct 2024)", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 23.04", "value": "ubuntu:23.04", "desc": "Lunar Lobster - EOL Jan 2024", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 22.04 LTS", "value": "ubuntu:22.04", "desc": "Jammy Jellyfish - Current LTS (April 2022)", "category": "Ubuntu", "icon": "🐧", "popular": True, "ram_min": 1024},
    {"label": "🐧 Ubuntu 22.10", "value": "ubuntu:22.10", "desc": "Kinetic Kudu - EOL July 2023", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 21.10", "value": "ubuntu:21.10", "desc": "Impish Indri - EOL July 2022", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 21.04", "value": "ubuntu:21.04", "desc": "Hirsute Hippo - EOL Jan 2022", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 20.04 LTS", "value": "ubuntu:20.04", "desc": "Focal Fossa - Stable LTS (April 2020)", "category": "Ubuntu", "icon": "🐧", "popular": True, "ram_min": 1024},
    {"label": "🐧 Ubuntu 20.10", "value": "ubuntu:20.10", "desc": "Groovy Gorilla - EOL July 2021", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 19.10", "value": "ubuntu:19.10", "desc": "Eoan Ermine - EOL July 2020", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 19.04", "value": "ubuntu:19.04", "desc": "Disco Dingo - EOL Jan 2020", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 18.04 LTS", "value": "ubuntu:18.04", "desc": "Bionic Beaver - Legacy LTS (April 2018)", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 18.10", "value": "ubuntu:18.10", "desc": "Cosmic Cuttlefish - EOL July 2019", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 17.10", "value": "ubuntu:17.10", "desc": "Artful Aardvark - EOL July 2018", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 17.04", "value": "ubuntu:17.04", "desc": "Zesty Zapus - EOL Jan 2018", "category": "Ubuntu", "icon": "🐧", "ram_min": 1024},
    {"label": "🐧 Ubuntu 16.04 LTS", "value": "ubuntu:16.04", "desc": "Xenial Xerus - Old LTS (April 2016)", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    {"label": "🐧 Ubuntu 16.10", "value": "ubuntu:16.10", "desc": "Yakkety Yak - EOL July 2017", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    {"label": "🐧 Ubuntu 15.10", "value": "ubuntu:15.10", "desc": "Wily Werewolf - EOL July 2016", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    {"label": "🐧 Ubuntu 15.04", "value": "ubuntu:15.04", "desc": "Vivid Vervet - EOL Jan 2016", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    {"label": "🐧 Ubuntu 14.04 LTS", "value": "ubuntu:14.04", "desc": "Trusty Tahr - Ancient LTS (April 2014)", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    {"label": "🐧 Ubuntu 12.04 LTS", "value": "ubuntu:12.04", "desc": "Precise Pangolin - Very Old LTS", "category": "Ubuntu", "icon": "🐧", "ram_min": 512},
    {"label": "🐧 Ubuntu 10.04 LTS", "value": "ubuntu:10.04", "desc": "Lucid Lynx - Retro LTS", "category": "Ubuntu", "icon": "🐧", "ram_min": 256},
    {"label": "🌀 Debian 13", "value": "images:debian/13", "desc": "Trixie - Testing (Upcoming Stable)", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Debian 12", "value": "images:debian/12", "desc": "Bookworm - Current Stable (June 2023)", "category": "Debian", "icon": "🌀", "popular": True, "ram_min": 512},
    {"label": "🌀 Debian 11", "value": "images:debian/11", "desc": "Bullseye - Old Stable (Aug 2021)", "category": "Debian", "icon": "🌀", "popular": True, "ram_min": 512},
    {"label": "🌀 Debian 10", "value": "images:debian/10", "desc": "Buster - Older Stable (July 2019)", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Debian 9", "value": "images:debian/9", "desc": "Stretch - Legacy (June 2017)", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Debian 8", "value": "images:debian/8", "desc": "Jessie - Ancient (April 2015)", "category": "Debian", "icon": "🌀", "ram_min": 256},
    {"label": "🌀 Debian 7", "value": "images:debian/7", "desc": "Wheezy - Retro (May 2013)", "category": "Debian", "icon": "🌀", "ram_min": 256},
    {"label": "🌀 Debian 6", "value": "images:debian/6", "desc": "Squeeze - Very Old (Feb 2011)", "category": "Debian", "icon": "🌀", "ram_min": 256},
    {"label": "🌀 Debian 5", "value": "images:debian/5", "desc": "Lenny - Museum (Feb 2009)", "category": "Debian", "icon": "🌀", "ram_min": 128},
    {"label": "🌀 Debian Sid", "value": "images:debian/sid", "desc": "Unstable - Rolling Development", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Debian Testing", "value": "images:debian/testing", "desc": "Testing - Next Stable", "category": "Debian", "icon": "🌀", "ram_min": 512},
    {"label": "🎩 Fedora 41", "value": "images:fedora/41", "desc": "Fedora 41 - Latest Development", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    {"label": "🎩 Fedora 40", "value": "images:fedora/40", "desc": "Fedora 40 - Latest (April 2024)", "category": "Fedora", "icon": "🎩", "popular": True, "ram_min": 1024},
    {"label": "🎩 Fedora 39", "value": "images:fedora/39", "desc": "Fedora 39 - Stable (Nov 2023)", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    {"label": "🎩 Fedora 38", "value": "images:fedora/38", "desc": "Fedora 38 - Older (April 2023)", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    {"label": "🎩 Fedora 37", "value": "images:fedora/37", "desc": "Fedora 37 - EOL Dec 2023", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    {"label": "🎩 Fedora Rawhide", "value": "images:fedora/rawhide", "desc": "Rawhide - Rolling Development", "category": "Fedora", "icon": "🎩", "ram_min": 1024},
    {"label": "🦊 Rocky Linux 9", "value": "images:rockylinux/9", "desc": "Rocky 9 - Latest (July 2022)", "category": "Rocky", "icon": "🦊", "popular": True, "ram_min": 1024},
    {"label": "🦊 Rocky Linux 8", "value": "images:rockylinux/8", "desc": "Rocky 8 - Stable (June 2021)", "category": "Rocky", "icon": "🦊", "ram_min": 1024},
    {"label": "🦊 AlmaLinux 9", "value": "images:almalinux/9", "desc": "Alma 9 - Latest (July 2022)", "category": "AlmaLinux", "icon": "🦊", "popular": True, "ram_min": 1024},
    {"label": "🦊 AlmaLinux 8", "value": "images:almalinux/8", "desc": "Alma 8 - Stable (March 2021)", "category": "AlmaLinux", "icon": "🦊", "ram_min": 1024},
    {"label": "📦 CentOS 9 Stream", "value": "images:centos/9-Stream", "desc": "CentOS 9 Stream - Rolling", "category": "CentOS", "icon": "📦", "ram_min": 1024},
    {"label": "📦 CentOS 8 Stream", "value": "images:centos/8-Stream", "desc": "CentOS 8 Stream - EOL May 2024", "category": "CentOS", "icon": "📦", "ram_min": 1024},
    {"label": "📦 CentOS 7", "value": "images:centos/7", "desc": "CentOS 7 - Legacy (June 2024 EOL)", "category": "CentOS", "icon": "📦", "ram_min": 1024},
    {"label": "🐧 Alpine 3.20", "value": "images:alpine/3.20", "desc": "Alpine 3.20 - Latest (May 2024)", "category": "Alpine", "icon": "🐧", "ram_min": 256},
    {"label": "🐧 Alpine 3.19", "value": "images:alpine/3.19", "desc": "Alpine 3.19 - Stable (Dec 2023)", "category": "Alpine", "icon": "🐧", "popular": True, "ram_min": 256},
    {"label": "🐧 Alpine 3.18", "value": "images:alpine/3.18", "desc": "Alpine 3.18 - Older (May 2023)", "category": "Alpine", "icon": "🐧", "ram_min": 256},
    {"label": "🐧 Alpine Edge", "value": "images:alpine/edge", "desc": "Alpine Edge - Rolling Development", "category": "Alpine", "icon": "🐧", "ram_min": 256},
    {"label": "📀 Arch Linux", "value": "images:archlinux", "desc": "Arch - Rolling Release", "category": "Arch", "icon": "📀", "popular": True, "ram_min": 1024},
    {"label": "📀 Arch Linux (Current)", "value": "images:archlinux/current", "desc": "Arch Current - Rolling", "category": "Arch", "icon": "📀", "ram_min": 1024},
    {"label": "📀 Manjaro", "value": "images:manjaro", "desc": "Manjaro - Arch Based", "category": "Arch", "icon": "📀", "ram_min": 1024},
    {"label": "🟢 OpenSUSE Tumbleweed", "value": "images:opensuse/tumbleweed", "desc": "Rolling Release", "category": "OpenSUSE", "icon": "🟢", "ram_min": 1024},
    {"label": "🟢 OpenSUSE Leap 15.6", "value": "images:opensuse/15.6", "desc": "Leap 15.6 - Latest (June 2024)", "category": "OpenSUSE", "icon": "🟢", "ram_min": 1024},
    {"label": "🟢 OpenSUSE Leap 15.5", "value": "images:opensuse/15.5", "desc": "Leap 15.5 - Stable (June 2023)", "category": "OpenSUSE", "icon": "🟢", "ram_min": 1024},
    {"label": "🔵 FreeBSD 14", "value": "images:freebsd/14", "desc": "FreeBSD 14 - Latest (Nov 2023)", "category": "FreeBSD", "icon": "🔵", "popular": True, "ram_min": 1024},
    {"label": "🔵 FreeBSD 13", "value": "images:freebsd/13", "desc": "FreeBSD 13 - Stable (April 2021)", "category": "FreeBSD", "icon": "🔵", "ram_min": 1024},
    {"label": "🐡 OpenBSD 7.5", "value": "images:openbsd/7.5", "desc": "OpenBSD 7.5 - Latest (April 2024)", "category": "OpenBSD", "icon": "🐡", "ram_min": 512},
    {"label": "🐡 OpenBSD 7.4", "value": "images:openbsd/7.4", "desc": "OpenBSD 7.4 - Stable (Oct 2023)", "category": "OpenBSD", "icon": "🐡", "ram_min": 512},
    {"label": "🐉 Kali Linux", "value": "images:kali", "desc": "Kali - Security Testing (Rolling)", "category": "Kali", "icon": "🐉", "popular": True, "ram_min": 2048},
    {"label": "🐉 Kali Linux Weekly", "value": "images:kali/weekly", "desc": "Kali Weekly - Bleeding Edge", "category": "Kali", "icon": "🐉", "ram_min": 2048},
    {"label": "🦜 Parrot OS", "value": "images:parrotos", "desc": "Parrot Security OS", "category": "Parrot", "icon": "🦜", "ram_min": 2048},
    {"label": "💻 Gentoo", "value": "images:gentoo", "desc": "Gentoo - Source Based", "category": "Gentoo", "icon": "💻", "ram_min": 4096},
    {"label": "💻 Gentoo Current", "value": "images:gentoo/current", "desc": "Gentoo Current - Rolling", "category": "Gentoo", "icon": "💻", "ram_min": 4096},
    {"label": "☁️ Amazon Linux 2", "value": "images:amazonlinux/2", "desc": "Amazon Linux 2 - AWS Optimized", "category": "Amazon", "icon": "☁️", "ram_min": 1024},
    {"label": "☁️ Amazon Linux 2023", "value": "images:amazonlinux/2023", "desc": "Amazon Linux 2023 - Latest", "category": "Amazon", "icon": "☁️", "ram_min": 1024},
    {"label": "🔴 Red Hat 9", "value": "images:rhel/9", "desc": "RHEL 9 - Enterprise (May 2022)", "category": "RHEL", "icon": "🔴", "ram_min": 2048},
    {"label": "🔴 Red Hat 8", "value": "images:rhel/8", "desc": "RHEL 8 - Stable (May 2019)", "category": "RHEL", "icon": "🔴", "ram_min": 2048},
    {"label": "🌀 Devuan 5", "value": "images:devuan/5", "desc": "Devuan Daedalus - Without Systemd", "category": "Devuan", "icon": "🌀", "ram_min": 512},
    {"label": "🌀 Devuan 4", "value": "images:devuan/4", "desc": "Devuan Chimaera - Stable", "category": "Devuan", "icon": "🌀", "ram_min": 512},
    {"label": "💾 Slackware 15", "value": "images:slackware/15", "desc": "Slackware 15 - Latest (Feb 2022)", "category": "Slackware", "icon": "💾", "ram_min": 1024},
    {"label": "💾 Slackware 14.2", "value": "images:slackware/14.2", "desc": "Slackware 14.2 - Stable", "category": "Slackware", "icon": "💾", "ram_min": 1024},
    {"label": "🔷 Clear Linux", "value": "images:clearlinux", "desc": "Clear Linux - Intel Optimized", "category": "Clear", "icon": "🔷", "ram_min": 1024},
]

# ==================================================================================================
#  🎮  GAMES LIST
# ==================================================================================================

GAMES_LIST = [
    {'name': 'Minecraft Java', 'docker': 'itzg/minecraft-server', 'port': 25565, 'ram': 2048, 'icon': '🎮'},
    {'name': 'Minecraft Bedrock', 'docker': 'itzg/minecraft-bedrock-server', 'port': 19132, 'ram': 1024, 'icon': '📱'},
    {'name': 'Terraria', 'docker': 'beardedio/terraria', 'port': 7777, 'ram': 1024, 'icon': '🌳'},
    {'name': 'CS:GO', 'docker': 'cm2network/csgo', 'port': 27015, 'ram': 2048, 'icon': '🔫'},
    {'name': 'Valheim', 'docker': 'lloesche/valheim-server', 'port': 2456, 'ram': 2048, 'icon': '⚔️'},
    {'name': 'ARK', 'docker': 'hermsi/ark-server-tools', 'port': 7777, 'ram': 4096, 'icon': '🦖'},
    {'name': 'Rust', 'docker': 'didstopia/rust-server', 'port': 28015, 'ram': 4096, 'icon': '🦀'},
]

# ==================================================================================================
#  🛠️  TOOLS LIST
# ==================================================================================================

TOOLS_LIST = [
    {'name': 'Nginx', 'cmd': 'apt install nginx -y', 'port': 80, 'icon': '🌐'},
    {'name': 'Apache', 'cmd': 'apt install apache2 -y', 'port': 80, 'icon': '🕸️'},
    {'name': 'MySQL', 'cmd': 'apt install mysql-server -y', 'port': 3306, 'icon': '🗄️'},
    {'name': 'PostgreSQL', 'cmd': 'apt install postgresql -y', 'port': 5432, 'icon': '🐘'},
    {'name': 'Redis', 'cmd': 'apt install redis-server -y', 'port': 6379, 'icon': '🔴'},
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
        {'name': '👑 Royal', 'invites': 30, 'ram': 64, 'cpu': 32, 'disk': 640, 'emoji': '👑'},
    ]
}

# ==================================================================================================
#  🗄️  DATABASE SETUP
# ==================================================================================================

DATABASE_PATH = '/opt/svm5-bot/data/svm5.db'
NODES_FILE = '/opt/svm5-bot/nodes/nodes.json'

def get_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except:
        return None

def init_db():
    conn = get_db()
    if not conn:
        return False
    cur = conn.cursor()
    
    # Admins
    cur.execute('''CREATE TABLE IF NOT EXISTS admins (user_id TEXT PRIMARY KEY, added_at TEXT)''')
    for aid in MAIN_ADMIN_IDS:
        cur.execute('INSERT OR IGNORE INTO admins (user_id, added_at) VALUES (?, ?)', (str(aid), datetime.now().isoformat()))
    
    # VPS
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
        games_installed TEXT DEFAULT '[]',
        tools_installed TEXT DEFAULT '[]',
        shared_with TEXT DEFAULT '[]'
    )''')
    
    # User stats
    cur.execute('''CREATE TABLE IF NOT EXISTS user_stats (
        user_id TEXT PRIMARY KEY,
        invites INTEGER DEFAULT 0,
        boosts INTEGER DEFAULT 0,
        claimed_vps_count INTEGER DEFAULT 0,
        api_key TEXT UNIQUE,
        last_updated TEXT
    )''')
    
    # Settings
    cur.execute('''CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)''')
    
    # Shared VPS
    cur.execute('''CREATE TABLE IF NOT EXISTS shared_vps (
        owner_id TEXT, shared_with_id TEXT, container_name TEXT, permissions TEXT, shared_at TEXT,
        UNIQUE(owner_id, shared_with_id, container_name)
    )''')
    
    # Games
    cur.execute('''CREATE TABLE IF NOT EXISTS installed_games (
        user_id TEXT, container_name TEXT, game_name TEXT, game_port INT, installed_at TEXT
    )''')
    
    # Tools
    cur.execute('''CREATE TABLE IF NOT EXISTS installed_tools (
        user_id TEXT, container_name TEXT, tool_name TEXT, tool_port INT, installed_at TEXT
    )''')
    
    # IPv4
    cur.execute('''CREATE TABLE IF NOT EXISTS ipv4 (
        user_id TEXT, container_name TEXT, public_ip TEXT, private_ip TEXT, mac_address TEXT, assigned_at TEXT
    )''')
    
    # Port forwards
    cur.execute('''CREATE TABLE IF NOT EXISTS port_forwards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT, container_name TEXT, container_port INT, host_port INT UNIQUE, protocol TEXT, created_at TEXT
    )''')
    
    # Port allocations
    cur.execute('''CREATE TABLE IF NOT EXISTS port_allocations (
        user_id TEXT PRIMARY KEY, allocated_ports INTEGER DEFAULT 5
    )''')
    
    # Panels
    cur.execute('''CREATE TABLE IF NOT EXISTS panels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT, panel_type TEXT, panel_url TEXT, admin_user TEXT, admin_pass TEXT, admin_email TEXT,
        container_name TEXT, tunnel_url TEXT, installed_at TEXT
    )''')
    
    # Transactions
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT, txn_ref TEXT UNIQUE, txn_id TEXT, amount INT, status TEXT DEFAULT 'pending', created_at TEXT
    )''')
    
    # AI History
    cur.execute('''CREATE TABLE IF NOT EXISTS ai_history (user_id TEXT PRIMARY KEY, messages TEXT, updated_at TEXT)''')
    
    # Snapshots
    cur.execute('''CREATE TABLE IF NOT EXISTS snapshots (user_id TEXT, container_name TEXT, snapshot_name TEXT, created_at TEXT)''')
    
    # Settings defaults
    settings = [
        ('license_verified', 'false'),
        ('server_ip', SERVER_IP),
        ('mac_address', MAC_ADDRESS),
        ('hostname', HOSTNAME),
        ('default_port_quota', '5'),
        ('ipv4_price', '50'),
        ('upi_id', '9892642904@ybl'),
    ]
    for k, v in settings:
        cur.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)', (k, v))
    
    conn.commit()
    conn.close()
    logger.info("✅ Database initialized")
    return True

init_db()

# ==================================================================================================
#  📊  DATABASE HELPERS
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
    cur.execute('SELECT * FROM vps WHERE user_id = ? ORDER BY id', (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_all_vps() -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM vps ORDER BY user_id, id')
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_vps(user_id: str, container_name: str, ram: int, cpu: int, disk: int, os_version: str, plan: str = "Custom") -> Optional[Dict]:
    conn = get_db()
    if not conn:
        return None
    cur = conn.cursor()
    now = datetime.now().isoformat()
    
    ip = "N/A"
    mac = "N/A"
    try:
        ip = subprocess.getoutput(f"lxc exec {container_name} -- ip -4 addr show eth0 | grep -oP '(?<=inet\\s)[0-9.]+' | head -1")
        mac = subprocess.getoutput(f"lxc exec {container_name} -- ip link | grep ether | awk '{{print $2}}' | head -1")
    except:
        pass
    
    cur.execute('''INSERT INTO vps 
        (user_id, container_name, plan_name, ram, cpu, disk, os_version, status, created_at, ip_address, mac_address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (user_id, container_name, plan, ram, cpu, disk, os_version, 'running', now, ip, mac))
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
    cur.execute('DELETE FROM shared_vps WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM installed_games WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM installed_tools WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM ipv4 WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM port_forwards WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM panels WHERE container_name = ?', (container_name,))
    cur.execute('DELETE FROM snapshots WHERE container_name = ?', (container_name,))
    conn.commit()
    conn.close()
    return True

def is_admin(user_id: str) -> bool:
    return user_id in [str(a) for a in MAIN_ADMIN_IDS]

def get_user_stats(user_id: str) -> Dict:
    conn = get_db()
    if not conn:
        return {'invites': 0}
    cur = conn.cursor()
    cur.execute('SELECT * FROM user_stats WHERE user_id = ?', (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    api_key = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()[:16]
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO user_stats (user_id, invites, boosts, claimed_vps_count, api_key, last_updated) VALUES (?, 0, 0, 0, ?, ?)',
               (user_id, api_key, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return {'user_id': user_id, 'invites': 0, 'api_key': api_key}

def update_user_stats(user_id: str, invites: int = 0, claimed: int = 0):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO user_stats 
        (user_id, invites, boosts, claimed_vps_count, api_key, last_updated)
        VALUES (?, 
                COALESCE((SELECT invites FROM user_stats WHERE user_id = ?), 0) + ?,
                0,
                COALESCE((SELECT claimed_vps_count FROM user_stats WHERE user_id = ?), 0) + ?,
                COALESCE((SELECT api_key FROM user_stats WHERE user_id = ?), ?),
                ?)''',
        (user_id, user_id, invites, user_id, claimed, user_id, hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()[:16], datetime.now().isoformat()))
    conn.commit()
    conn.close()

def share_vps(owner: str, shared: str, container: str) -> bool:
    conn = get_db()
    if not conn:
        return False
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('INSERT OR REPLACE INTO shared_vps VALUES (?, ?, ?, ?, ?)', (owner, shared, container, 'view', now))
    conn.commit()
    conn.close()
    return True

def unshare_vps(owner: str, shared: str, container: str) -> bool:
    conn = get_db()
    if not conn:
        return False
    cur = conn.cursor()
    cur.execute('DELETE FROM shared_vps WHERE owner_id = ? AND shared_with_id = ? AND container_name = ?',
               (owner, shared, container))
    conn.commit()
    conn.close()
    return True

def get_shared_vps(user_id: str) -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('''SELECT v.*, sv.permissions, sv.owner_id 
                   FROM vps v JOIN shared_vps sv ON v.container_name = sv.container_name 
                   WHERE sv.shared_with_id = ?''', (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_port_forward(user_id: str, container: str, cport: int, hport: int, proto: str = "tcp+udp") -> bool:
    conn = get_db()
    if not conn:
        return False
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('INSERT INTO port_forwards (user_id, container_name, container_port, host_port, protocol, created_at) VALUES (?, ?, ?, ?, ?, ?)',
               (user_id, container, cport, hport, proto, now))
    conn.commit()
    conn.close()
    return True

def remove_port_forward(pid: int) -> Tuple[bool, str, int]:
    conn = get_db()
    if not conn:
        return False, "", 0
    cur = conn.cursor()
    cur.execute('SELECT container_name, host_port FROM port_forwards WHERE id = ?', (pid,))
    row = cur.fetchone()
    if not row:
        conn.close()
        return False, "", 0
    container, hport = row['container_name'], row['host_port']
    cur.execute('DELETE FROM port_forwards WHERE id = ?', (pid,))
    conn.commit()
    conn.close()
    return True, container, hport

def get_user_port_forwards(user_id: str) -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM port_forwards WHERE user_id = ? ORDER BY created_at', (user_id,))
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

def add_ipv4(user_id: str, container: str, public: str, private: str, mac: str = ""):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('INSERT OR REPLACE INTO ipv4 VALUES (?, ?, ?, ?, ?, ?)',
               (user_id, container, public, private, mac, now))
    conn.commit()
    conn.close()

def get_user_ipv4(user_id: str) -> List[Dict]:
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM ipv4 WHERE user_id = ?', (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_transaction(user_id: str, txn_ref: str, amount: int) -> int:
    conn = get_db()
    if not conn:
        return 0
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('INSERT INTO transactions (user_id, txn_ref, amount, created_at) VALUES (?, ?, ?, ?)',
               (user_id, txn_ref, amount, now))
    tid = cur.lastrowid
    conn.commit()
    conn.close()
    return tid

def add_game_install(user_id: str, container: str, game: str, port: int):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('INSERT INTO installed_games VALUES (?, ?, ?, ?, ?)',
               (user_id, container, game, port, now))
    conn.commit()
    conn.close()

def add_tool_install(user_id: str, container: str, tool: str, port: int = None):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('INSERT INTO installed_tools VALUES (?, ?, ?, ?, ?)',
               (user_id, container, tool, port, now))
    conn.commit()
    conn.close()

def add_panel(user_id: str, ptype: str, url: str, user: str, pwd: str, email: str, container: str, tunnel: str = ""):
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute('''INSERT INTO panels 
        (user_id, panel_type, panel_url, admin_user, admin_pass, admin_email, container_name, tunnel_url, installed_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (user_id, ptype, url, user, pwd, email, container, tunnel, now))
    conn.commit()
    conn.close()

def add_snapshot(user_id: str, container_name: str, snapshot_name: str):
    """Add snapshot to database"""
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('INSERT INTO snapshots VALUES (?, ?, ?, ?)',
               (user_id, container_name, snapshot_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_snapshots(container_name: str) -> List[Dict]:
    """Get snapshots for container"""
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM snapshots WHERE container_name = ? ORDER BY created_at DESC', (container_name,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_user_panels(user_id: str) -> List[Dict]:
    """Get panels for user"""
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT * FROM panels WHERE user_id = ? ORDER BY installed_at DESC', (user_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def clear_ai_history(user_id: str):
    """Clear AI chat history"""
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('DELETE FROM ai_history WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

def load_ai_history(user_id: str) -> List[Dict]:
    """Load AI chat history"""
    conn = get_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute('SELECT messages FROM ai_history WHERE user_id = ?', (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return json.loads(row['messages'])
    return []

def save_ai_history(user_id: str, messages: List[Dict]):
    """Save AI chat history"""
    conn = get_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute('INSERT OR REPLACE INTO ai_history (user_id, messages, updated_at) VALUES (?, ?, ?)',
               (user_id, json.dumps(messages), datetime.now().isoformat()))
    conn.commit()
    conn.close()

# ==================================================================================================
#  🌐  NODE MANAGEMENT WITH NODES.JSON
# ==================================================================================================

def load_nodes():
    """Load nodes from JSON file with auto-detect"""
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
        "username": "local",
        "type": "local",
        "status": "online",
        "is_main": True,
        "region": "us",
        "description": "Auto-detected local node",
        "api_key": hashlib.sha256(f"local{time.time()}".encode()).hexdigest()[:32],
        "stats": {
            "total_ram": psutil.virtual_memory().total // 1024 // 1024,
            "used_ram": psutil.virtual_memory().used // 1024 // 1024,
            "total_cpu": psutil.cpu_count(),
            "used_cpu": psutil.cpu_percent(),
            "total_disk": psutil.disk_usage('/').total // 1024 // 1024 // 1024,
            "used_disk": psutil.disk_usage('/').used // 1024 // 1024 // 1024,
            "lxc_count": lxc_count,
            "last_checked": datetime.now().isoformat()
        },
        "settings": {
            "max_containers": 100,
            "default_storage_pool": DEFAULT_STORAGE_POOL,
            "allow_overcommit": True
        }
    }
    
    default["nodes"]["local"] = local_node
    default["node_groups"]["all"].append("local")
    default["node_groups"]["us"].append("local")
    
    with open(NODES_FILE, 'w') as f:
        json.dump(default, f, indent=2)
    
    return default

def save_nodes(data):
    with open(NODES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_node(name):
    nodes = load_nodes()
    return nodes['nodes'].get(name)

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
        save_nodes(nodes)
    return nodes

# ==================================================================================================
#  🛠️  LXC HELPERS
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
        out = subprocess.getoutput(f"lxc info {container} | grep Status | awk '{{print $2}}'")
        return out.lower()
    except:
        return "unknown"

async def get_container_stats(container: str) -> Dict:
    stats = {'status': 'unknown', 'cpu': '0%', 'memory': '0/0MB', 'disk': '0/0GB', 'ipv4': [], 'mac': 'N/A', 'uptime': '0m'}
    stats['status'] = await get_container_status(container)
    if stats['status'] == 'running':
        out, _, _ = await exec_in_container(container, "top -bn1 | grep Cpu | awk '{print $2}'")
        stats['cpu'] = f"{out}%" if out else "0%"
        out, _, _ = await exec_in_container(container, "free -m | awk '/^Mem:/{print $3\"/\"$2}'")
        stats['memory'] = f"{out}MB" if out else "0/0MB"
        out, _, _ = await exec_in_container(container, "df -h / | awk 'NR==2{print $3\"/\"$2}'")
        stats['disk'] = out if out else "0/0GB"
        out, _, _ = await exec_in_container(container, "ip -4 addr show | grep -oP '(?<=inet\\s)[0-9.]+' | grep -v 127")
        stats['ipv4'] = out.splitlines() if out else []
        out, _, _ = await exec_in_container(container, "ip link | grep ether | awk '{print $2}'")
        stats['mac'] = out.splitlines()[0] if out else "N/A"
        out, _, _ = await exec_in_container(container, "uptime -p | sed 's/up //'")
        stats['uptime'] = out if out else "0m"
    return stats

async def get_available_port() -> Optional[int]:
    used = set()
    conn = get_db()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT host_port FROM port_forwards')
        used = {r[0] for r in cur.fetchall()}
        conn.close()
    for _ in range(100):
        port = random.randint(20000, 50000)
        if port not in used:
            return port
    return None

async def create_port_forward(user_id: str, container: str, cport: int, proto: str = "tcp+udp") -> Optional[int]:
    hport = await get_available_port()
    if not hport:
        return None
    try:
        if proto in ["tcp", "tcp+udp"]:
            await run_lxc(f"lxc config device add {container} proxy-tcp-{hport} proxy listen=tcp:0.0.0.0:{hport} connect=tcp:127.0.0.1:{cport}")
        if proto in ["udp", "tcp+udp"]:
            await run_lxc(f"lxc config device add {container} proxy-udp-{hport} proxy listen=udp:0.0.0.0:{hport} connect=udp:127.0.0.1:{cport}")
        add_port_forward(user_id, container, cport, hport, proto)
        return hport
    except:
        return None

async def remove_port_device(container: str, hport: int):
    try:
        await run_lxc(f"lxc config device remove {container} proxy-tcp-{hport}")
    except:
        pass
    try:
        await run_lxc(f"lxc config device remove {container} proxy-udp-{hport}")
    except:
        pass

async def apply_lxc_config(container_name: str):
    """Apply LXC configuration to container"""
    try:
        await run_lxc(f"lxc config device add {container_name} eth0 nic name=eth0 network=lxdbr0")
        await run_lxc(f"lxc config set {container_name} security.privileged true")
        await run_lxc(f"lxc config set {container_name} security.nesting true")
    except:
        pass

async def apply_internal_permissions(container_name: str):
    """Apply internal permissions to container"""
    try:
        await exec_in_container(container_name, "useradd -m -s /bin/bash -G sudo svm5 2>/dev/null || true")
        await exec_in_container(container_name, "echo 'svm5:svm5' | chpasswd 2>/dev/null || true")
        await exec_in_container(container_name, "echo 'svm5 ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers 2>/dev/null || true")
        await exec_in_container(container_name, "apt-get update -qq 2>/dev/null || true")
        await exec_in_container(container_name, "apt-get install -y -qq curl wget sudo 2>/dev/null || true")
    except:
        pass

# ==================================================================================================
#  🎨  UI HELPER FUNCTIONS
# ==================================================================================================

def glow_text(text: str) -> str:
    return f"```glow\n{text}\n```"

def terminal_text(text: str) -> str:
    return f"```fix\n{text}\n```"

def error_text(text: str) -> str:
    return f"```diff\n- {text}\n```"

def os_embed(title: str, desc: str = "") -> discord.Embed:
    embed = discord.Embed(title=f"```glow\n{title}\n```", description=desc, color=COLORS['os'])
    embed.set_thumbnail(url=THUMBNAIL_URL)
    return embed

def create_embed(title: str, desc: str = "", color: int = COLORS['primary']) -> discord.Embed:
    embed = discord.Embed(title=glow_text(f"✦ {BOT_NAME} - {title} ✦"), description=desc, color=color)
    embed.set_thumbnail(url=THUMBNAIL_URL)
    embed.set_footer(text=f"⚡ {BOT_NAME} • {BOT_AUTHOR} • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ⚡", icon_url=THUMBNAIL_URL)
    return embed

def success_embed(title: str, desc: str = "") -> discord.Embed:
    return create_embed(f"✅ {title}", desc, COLORS['success'])

def error_embed(title: str, desc: str = "") -> discord.Embed:
    return create_embed(f"❌ {title}", desc, COLORS['error'])

def info_embed(title: str, desc: str = "") -> discord.Embed:
    return create_embed(f"ℹ️ {title}", desc, COLORS['info'])

def warning_embed(title: str, desc: str = "") -> discord.Embed:
    return create_embed(f"⚠️ {title}", desc, COLORS['warning'])

def node_embed(title: str, desc: str = "") -> discord.Embed:
    return create_embed(f"🌐 {title}", desc, COLORS['node'])

def terminal_embed(title: str, content: str) -> discord.Embed:
    embed = discord.Embed(title=terminal_text(f"[ {title} ]"), description=f"```bash\n{content[:1900]}\n```", color=COLORS['terminal'])
    embed.set_footer(text=f"⚡ Terminal • {datetime.now().strftime('%H:%M:%S')} ⚡")
    return embed

def no_vps_embed() -> discord.Embed:
    return info_embed("No VPS Found", error_text("You don't have any VPS yet.") + f"\n\nUse `{BOT_PREFIX}plans` to see plans")

# ==================================================================================================
#  🌈  RAINBOW COLORS FOR PROGRESS
# ==================================================================================================

RAINBOW_COLORS = [
    0xFF0000,  # Red
    0xFF7700,  # Orange
    0xFFFF00,  # Yellow
    0x00FF00,  # Green
    0x00CCFF,  # Cyan
    0x3366FF,  # Blue
    0x8B00FF,  # Violet
    0xFF00CC,  # Pink
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

# Check if cloudflared is installed
CLOUDFLARED_AVAILABLE = shutil.which("cloudflared") is not None

async def create_cloudflared_tunnel(container_name: str, port: int = 80) -> Optional[str]:
    """Create cloudflared tunnel for container and return URL"""
    if not CLOUDFLARED_AVAILABLE:
        return None
    
    try:
        await exec_in_container(container_name, "which cloudflared || (wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O /usr/local/bin/cloudflared && chmod +x /usr/local/bin/cloudflared)")
        tunnel_id = str(uuid.uuid4())[:8]
        await exec_in_container(container_name, f"nohup cloudflared tunnel --url http://localhost:{port} --no-autoupdate > /tmp/cloudflared_{tunnel_id}.log 2>&1 & echo $!")
        await asyncio.sleep(8)
        out, _, _ = await exec_in_container(container_name, f"cat /tmp/cloudflared_{tunnel_id}.log | grep -oP 'https://[a-z0-9-]+\\.trycloudflare\\.com' | head -1")
        url = out.strip()
        if url:
            return url
    except Exception as e:
        logger.error(f"Failed to create cloudflared tunnel: {e}")
    return None

# ==================================================================================================
#  🖥️  VPS MANAGE VIEW WITH ALL BUTTONS
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
        
        # Row 1 - Basic Controls
        self.start_btn = Button(label="▶️ Start", style=discord.ButtonStyle.success, emoji="▶️", row=0)
        self.stop_btn = Button(label="⏹️ Stop", style=discord.ButtonStyle.danger, emoji="⏹️", row=0)
        self.restart_btn = Button(label="🔄 Restart", style=discord.ButtonStyle.primary, emoji="🔄", row=0)
        self.reboot_btn = Button(label="⚡ Reboot", style=discord.ButtonStyle.warning, emoji="⚡", row=0)
        self.shutdown_btn = Button(label="⛔ Shutdown", style=discord.ButtonStyle.danger, emoji="⛔", row=0)
        
        # Row 2 - Info & Access
        self.stats_btn = Button(label="📊 Stats", style=discord.ButtonStyle.secondary, emoji="📊", row=1)
        self.process_btn = Button(label="🔝 Processes", style=discord.ButtonStyle.secondary, emoji="🔝", row=1)
        self.console_btn = Button(label="📟 Console", style=discord.ButtonStyle.secondary, emoji="📟", row=1)
        self.ssh_btn = Button(label="🔑 SSH-GEN", style=discord.ButtonStyle.primary, emoji="🔑", row=1)
        self.logs_btn = Button(label="📋 Logs", style=discord.ButtonStyle.secondary, emoji="📋", row=1)
        
        # Row 3 - Advanced
        self.ipv4_btn = Button(label="🌍 IPv4 Check", style=discord.ButtonStyle.secondary, emoji="🌍", row=2)
        self.tunnel_btn = Button(label="🌐 Tunnel URL", style=discord.ButtonStyle.primary, emoji="🌐", row=2)
        self.ports_btn = Button(label="🔌 Ports", style=discord.ButtonStyle.secondary, emoji="🔌", row=2)
        self.backup_btn = Button(label="💾 Backup", style=discord.ButtonStyle.success, emoji="💾", row=2)
        self.restore_btn = Button(label="🔄 Restore", style=discord.ButtonStyle.warning, emoji="🔄", row=2)
        
        # Row 4 - Management
        self.reinstall_btn = Button(label="🔄 Reinstall OS", style=discord.ButtonStyle.danger, emoji="🔄", row=3)
        self.upgrade_btn = Button(label="⬆️ Upgrade VPS", style=discord.ButtonStyle.primary, emoji="⬆️", row=3)
        self.invites_btn = Button(label="📨 Check Invites", style=discord.ButtonStyle.secondary, emoji="📨", row=3)
        self.panel_btn = Button(label="📦 Install Panel", style=discord.ButtonStyle.primary, emoji="📦", row=3)
        self.share_btn = Button(label="👥 Share VPS", style=discord.ButtonStyle.secondary, emoji="👥", row=3)
        
        # Row 5 - Live & Refresh
        self.live_btn = Button(label="🔴 Live Mode", style=discord.ButtonStyle.danger, emoji="🔴", row=4)
        self.refresh_btn = Button(label="🔄 Refresh", style=discord.ButtonStyle.secondary, emoji="🔄", row=4)
        
        # Set callbacks
        self.start_btn.callback = self.start_callback
        self.stop_btn.callback = self.stop_callback
        self.restart_btn.callback = self.restart_callback
        self.reboot_btn.callback = self.reboot_callback
        self.shutdown_btn.callback = self.shutdown_callback
        
        self.stats_btn.callback = self.stats_callback
        self.process_btn.callback = self.process_callback
        self.console_btn.callback = self.console_callback
        self.ssh_btn.callback = self.ssh_callback
        self.logs_btn.callback = self.logs_callback
        
        self.ipv4_btn.callback = self.ipv4_callback
        self.tunnel_btn.callback = self.tunnel_callback
        self.ports_btn.callback = self.ports_callback
        self.backup_btn.callback = self.backup_callback
        self.restore_btn.callback = self.restore_callback
        
        self.reinstall_btn.callback = self.reinstall_callback
        self.upgrade_btn.callback = self.upgrade_callback
        self.invites_btn.callback = self.invites_callback
        self.panel_btn.callback = self.panel_callback
        self.share_btn.callback = self.share_callback
        
        self.live_btn.callback = self.live_callback
        self.refresh_btn.callback = self.refresh_callback
        
        # Add all buttons
        self.add_item(self.start_btn)
        self.add_item(self.stop_btn)
        self.add_item(self.restart_btn)
        self.add_item(self.reboot_btn)
        self.add_item(self.shutdown_btn)
        
        self.add_item(self.stats_btn)
        self.add_item(self.process_btn)
        self.add_item(self.console_btn)
        self.add_item(self.ssh_btn)
        self.add_item(self.logs_btn)
        
        self.add_item(self.ipv4_btn)
        self.add_item(self.tunnel_btn)
        self.add_item(self.ports_btn)
        self.add_item(self.backup_btn)
        self.add_item(self.restore_btn)
        
        self.add_item(self.reinstall_btn)
        self.add_item(self.upgrade_btn)
        self.add_item(self.invites_btn)
        self.add_item(self.panel_btn)
        self.add_item(self.share_btn)
        
        self.add_item(self.live_btn)
        self.add_item(self.refresh_btn)
    
    async def get_stats_embed(self):
        stats = await get_container_stats(self.container)
        
        embed = discord.Embed(
            title=f"```glow\n🖥️ VPS MANAGEMENT - {self.container.upper()}\n```",
            description=f"👤 **Owner:** {self.user.mention}\n📦 **Container:** `{self.container}`",
            color=0x5865F2
        )
        embed.set_thumbnail(url=self.user.avatar.url if self.user.avatar else THUMBNAIL_URL)
        embed.set_image(url=THUMBNAIL_URL)
        
        status_emoji = "🟢" if stats['status'] == 'running' and not self.data.get('suspended') else "⛔" if self.data.get('suspended') else "🔴"
        status_text = stats['status'].upper()
        if self.data.get('suspended'):
            status_text = "SUSPENDED"
        
        embed.add_field(name="📊 STATUS", value=f"{status_emoji} `{status_text}`", inline=True)
        embed.add_field(name="💾 CPU", value=f"```fix\n{stats['cpu']}\n```", inline=True)
        embed.add_field(name="📀 MEMORY", value=f"```fix\n{stats['memory']}\n```", inline=True)
        embed.add_field(name="💽 DISK", value=f"```fix\n{stats['disk']}\n```", inline=True)
        embed.add_field(name="🌐 IP", value=f"```fix\n{stats['ipv4'][0] if stats['ipv4'] else 'N/A'}\n```", inline=True)
        embed.add_field(name="🔌 MAC", value=f"```fix\n{stats['mac']}\n```", inline=True)
        embed.add_field(name="⏱️ UPTIME", value=f"```fix\n{stats['uptime']}\n```", inline=True)
        
        ram_alloc = self.data['ram']
        cpu_alloc = self.data['cpu']
        disk_alloc = self.data['disk']
        ram_bar = "█" * min(int(ram_alloc / 16), 10) + "░" * (10 - min(int(ram_alloc / 16), 10))
        cpu_bar = "█" * min(int(cpu_alloc / 8), 10) + "░" * (10 - min(int(cpu_alloc / 8), 10))
        disk_bar = "█" * min(int(disk_alloc / 100), 10) + "░" * (10 - min(int(disk_alloc / 100), 10))
        
        embed.add_field(name="⚙️ RESOURCES", value=f"```fix\nRAM: {ram_alloc}GB [{ram_bar}]\nCPU: {cpu_alloc} Core(s) [{cpu_bar}]\nDisk: {disk_alloc}GB [{disk_bar}]\n```", inline=False)
        
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
    
    async def reboot_callback(self, interaction):
        await interaction.response.defer()
        await run_lxc(f"lxc restart {self.container}")
        update_vps_status(self.container, 'running')
        await interaction.followup.send(embed=success_embed("Rebooted", f"```fix\n{self.container} rebooted.\n```"), ephemeral=True)
        await self.refresh_callback(interaction)
    
    async def shutdown_callback(self, interaction):
        await interaction.response.defer()
        await run_lxc(f"lxc stop {self.container}")
        update_vps_status(self.container, 'stopped')
        await interaction.followup.send(embed=success_embed("Shutdown", f"```fix\n{self.container} shutdown.\n```"), ephemeral=True)
        await self.refresh_callback(interaction)
    
    async def stats_callback(self, interaction):
        stats = await get_container_stats(self.container)
        embed = info_embed(f"Live Stats: {self.container}")
        embed.add_field(name="📊 Status", value=f"```fix\n{stats['status'].upper()}\n```", inline=True)
        embed.add_field(name="💾 CPU", value=f"```fix\n{stats['cpu']}\n```", inline=True)
        embed.add_field(name="📀 Memory", value=f"```fix\n{stats['memory']}\n```", inline=True)
        embed.add_field(name="💽 Disk", value=f"```fix\n{stats['disk']}\n```", inline=True)
        embed.add_field(name="⏱️ Uptime", value=f"```fix\n{stats['uptime']}\n```", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    async def process_callback(self, interaction):
        await interaction.response.defer()
        out, _, _ = await exec_in_container(self.container, "ps aux --sort=-%cpu | head -15")
        embed = terminal_embed(f"Top Processes: {self.container}", out)
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    async def console_callback(self, interaction):
        modal = CommandModal(self.container)
        await interaction.response.send_modal(modal)
    
    async def ssh_callback(self, interaction):
        await interaction.response.defer()
        await exec_in_container(self.container, "apt-get update -qq && apt-get install -y -qq tmate")
        sess = f"svm5-{random.randint(1000,9999)}"
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
    
    async def logs_callback(self, interaction):
        await interaction.response.defer()
        out, _, _ = await exec_in_container(self.container, "journalctl -n 50 --no-pager 2>/dev/null || dmesg | tail -50")
        embed = terminal_embed(f"Logs: {self.container}", out[:1900])
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    async def ipv4_callback(self, interaction):
        await interaction.response.defer()
        out, _, _ = await exec_in_container(self.container, "ip addr show")
        embed = terminal_embed(f"IPv4 Details: {self.container}", out[:1900])
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    async def tunnel_callback(self, interaction):
        await interaction.response.defer()
        tunnel_url = await create_cloudflared_tunnel(self.container, 80)
        if tunnel_url:
            embed = success_embed("🌐 Tunnel URL Generated")
            embed.add_field(name="URL", value=f"```fix\n{tunnel_url}\n```", inline=False)
            embed.add_field(name="Expires", value="```fix\n24 hours\n```", inline=True)
            await interaction.followup.send(embed=embed, ephemeral=True)
            
            conn = get_db()
            cur = conn.cursor()
            cur.execute('UPDATE panels SET tunnel_url = ? WHERE container_name = ?', (tunnel_url, self.container))
            conn.commit()
            conn.close()
        else:
            await interaction.followup.send(embed=error_embed("Failed", "Could not create tunnel"), ephemeral=True)
    
    async def ports_callback(self, interaction):
        await interaction.response.defer()
        out, _, _ = await exec_in_container(self.container, "netstat -tuln | head -20")
        embed = terminal_embed(f"Open Ports: {self.container}", out)
        await interaction.followup.send(embed=embed, ephemeral=True)
    
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
            options.append(discord.SelectOption(label=s['snapshot_name'], value=s['snapshot_name'], description=f"Created: {s['created_at'][:16]}"))
        
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
    
    async def reinstall_callback(self, interaction):
        options = []
        for os in OS_OPTIONS[:25]:
            options.append(discord.SelectOption(label=os['label'][:100], value=os['value'], description=os['desc'][:100]))
        
        view = View()
        select = Select(placeholder="Select new OS...", options=options)
        
        async def select_cb(sel_interaction):
            os_val = select.values[0]
            os_name = next((o['label'] for o in OS_OPTIONS if o['value'] == os_val), os_val)
            
            confirm_view = View()
            confirm_btn = Button(label="✅ Confirm Reinstall", style=discord.ButtonStyle.danger)
            cancel_btn = Button(label="❌ Cancel", style=discord.ButtonStyle.secondary)
            
            async def confirm_cb(confirm_interaction):
                await confirm_interaction.response.defer()
                msg = await confirm_interaction.followup.send(embed=info_embed("Reinstalling", f"```fix\n{self.container} with {os_name}...\n```"), ephemeral=True)
                
                try:
                    status = await get_container_status(self.container)
                    if status == 'running':
                        await run_lxc(f"lxc stop {self.container} --force")
                    
                    ram_mb = self.data['ram'] * 1024
                    cpu = self.data['cpu']
                    disk = self.data['disk']
                    
                    await run_lxc(f"lxc delete {self.container} --force")
                    await run_lxc(f"lxc init {os_val} {self.container} -s {DEFAULT_STORAGE_POOL}")
                    await run_lxc(f"lxc config set {self.container} limits.memory {ram_mb}MB")
                    await run_lxc(f"lxc config set {self.container} limits.cpu {cpu}")
                    await run_lxc(f"lxc config device set {self.container} root size={disk}GB")
                    await run_lxc(f"lxc start {self.container}")
                    await asyncio.sleep(5)
                    
                    embed = success_embed("OS Reinstalled")
                    embed.add_field(name="📦 Container", value=f"```fix\n{self.container}\n```", inline=True)
                    embed.add_field(name="🐧 New OS", value=f"```fix\n{os_name}\n```", inline=True)
                    await msg.edit(embed=embed)
                except Exception as e:
                    await msg.edit(embed=error_embed("Reinstall Failed", f"```diff\n- {str(e)}\n```"))
            
            confirm_btn.callback = confirm_cb
            cancel_btn.callback = lambda ci: ci.response.edit_message(embed=info_embed("Cancelled"), view=None)
            confirm_view.add_item(confirm_btn)
            confirm_view.add_item(cancel_btn)
            
            embed = warning_embed("⚠️ Confirm Reinstall", f"```fix\nContainer: {self.container}\nCurrent OS: {self.data.get('os_version', 'ubuntu:22.04')}\nNew OS: {os_name}\n```\n\n⚠️ ALL DATA WILL BE LOST!")
            await sel_interaction.response.edit_message(embed=embed, view=confirm_view)
        
        select.callback = select_cb
        view.add_item(select)
        await interaction.response.send_message(embed=info_embed("Reinstall OS"), view=view, ephemeral=True)
    
    async def upgrade_callback(self, interaction):
        stats = get_user_stats(str(self.ctx.author.id))
        invites = stats.get('invites', 0)
        
        options = [
            discord.SelectOption(label="💾 +2GB RAM", value="ram:2", description=f"Cost: 5 invites → New: {self.data['ram']+2}GB"),
            discord.SelectOption(label="💾 +4GB RAM", value="ram:4", description=f"Cost: 10 invites → New: {self.data['ram']+4}GB"),
            discord.SelectOption(label="⚡ +1 CPU Core", value="cpu:1", description=f"Cost: 5 invites → New: {self.data['cpu']+1} cores"),
            discord.SelectOption(label="⚡ +2 CPU Cores", value="cpu:2", description=f"Cost: 10 invites → New: {self.data['cpu']+2} cores"),
            discord.SelectOption(label="💽 +20GB Disk", value="disk:20", description=f"Cost: 5 invites → New: {self.data['disk']+20}GB"),
            discord.SelectOption(label="💽 +50GB Disk", value="disk:50", description=f"Cost: 10 invites → New: {self.data['disk']+50}GB"),
        ]
        
        view = View()
        select = Select(placeholder="Select upgrade...", options=options)
        
        async def select_cb(sel_interaction):
            value = select.values[0]
            resource, amount = value.split(':')
            amount = int(amount)
            cost = 5 if amount in [2,1,20] else 10
            
            if invites < cost:
                return await sel_interaction.response.send_message(embed=error_embed("Not Enough Invites", f"Need {cost} invites, you have {invites}"), ephemeral=True)
            
            confirm_view = View()
            confirm_btn = Button(label="✅ Confirm Upgrade", style=discord.ButtonStyle.success)
            cancel_btn = Button(label="❌ Cancel", style=discord.ButtonStyle.secondary)
            
            async def confirm_cb(confirm_interaction):
                await confirm_interaction.response.defer()
                msg = await confirm_interaction.followup.send(embed=info_embed("Upgrading", f"```fix\n+{amount} {resource.upper()}...\n```"), ephemeral=True)
                
                try:
                    status = await get_container_status(self.container)
                    was_running = status == 'running'
                    
                    if was_running:
                        await run_lxc(f"lxc stop {self.container} --force")
                    
                    if resource == "ram":
                        new_ram = self.data['ram'] + amount
                        await run_lxc(f"lxc config set {self.container} limits.memory {new_ram * 1024}MB")
                        conn = get_db()
                        cur = conn.cursor()
                        cur.execute('UPDATE vps SET ram = ? WHERE container_name = ?', (new_ram, self.container))
                        conn.commit()
                        conn.close()
                        self.data['ram'] = new_ram
                    elif resource == "cpu":
                        new_cpu = self.data['cpu'] + amount
                        await run_lxc(f"lxc config set {self.container} limits.cpu {new_cpu}")
                        conn = get_db()
                        cur = conn.cursor()
                        cur.execute('UPDATE vps SET cpu = ? WHERE container_name = ?', (new_cpu, self.container))
                        conn.commit()
                        conn.close()
                        self.data['cpu'] = new_cpu
                    elif resource == "disk":
                        new_disk = self.data['disk'] + amount
                        await run_lxc(f"lxc config device set {self.container} root size={new_disk}GB")
                        conn = get_db()
                        cur = conn.cursor()
                        cur.execute('UPDATE vps SET disk = ? WHERE container_name = ?', (new_disk, self.container))
                        conn.commit()
                        conn.close()
                        self.data['disk'] = new_disk
                    
                    if was_running:
                        await run_lxc(f"lxc start {self.container}")
                    
                    conn = get_db()
                    cur = conn.cursor()
                    cur.execute('UPDATE user_stats SET invites = invites - ?, last_updated = ? WHERE user_id = ?',
                               (cost, datetime.now().isoformat(), str(self.ctx.author.id)))
                    conn.commit()
                    conn.close()
                    
                    embed = success_embed("Upgraded")
                    embed.add_field(name="📦 Container", value=f"```fix\n{self.container}\n```", inline=True)
                    embed.add_field(name="⚙️ Upgrade", value=f"```fix\n+{amount} {resource.upper()}\nCost: {cost} invites\n```", inline=True)
                    await msg.edit(embed=embed)
                except Exception as e:
                    await msg.edit(embed=error_embed("Upgrade Failed", f"```diff\n- {str(e)}\n```"))
            
            confirm_btn.callback = confirm_cb
            cancel_btn.callback = lambda ci: ci.response.edit_message(embed=info_embed("Cancelled"), view=None)
            confirm_view.add_item(confirm_btn)
            confirm_view.add_item(cancel_btn)
            
            embed = warning_embed("Confirm Upgrade", f"```fix\nContainer: {self.container}\nUpgrade: +{amount} {resource.upper()}\nCost: {cost} invites\nCurrent: {self.data['ram'] if resource=='ram' else self.data['cpu'] if resource=='cpu' else self.data['disk']}\nNew: {self.data[resource] + amount}\n```")
            await sel_interaction.response.edit_message(embed=embed, view=confirm_view)
        
        select.callback = select_cb
        view.add_item(select)
        
        embed = info_embed("Upgrade VPS", f"```fix\nContainer: {self.container}\nCurrent RAM: {self.data['ram']}GB\nCurrent CPU: {self.data['cpu']} cores\nCurrent Disk: {self.data['disk']}GB\nYour Invites: {invites}\n```")
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    
    async def invites_callback(self, interaction):
        stats = get_user_stats(str(self.ctx.author.id))
        invites = stats.get('invites', 0)
        vps_count = len(get_user_vps(str(self.ctx.author.id)))
        
        embed = info_embed("Your Invites")
        embed.add_field(name="📨 Total Invites", value=f"```fix\n{invites}\n```", inline=True)
        embed.add_field(name="🖥️ VPS Count", value=f"```fix\n{vps_count}\n```", inline=True)
        
        next_plan = None
        for plan in FREE_VPS_PLANS['invites']:
            if invites < plan['invites']:
                next_plan = plan
                break
        
        if next_plan:
            embed.add_field(name="🎯 Next Plan", value=f"```fix\n{next_plan['emoji']} {next_plan['name']}\nNeed {next_plan['invites'] - invites} more invites\nRAM: {next_plan['ram']}GB\n```", inline=False)
        else:
            embed.add_field(name="🏆 Status", value="```fix\nYou have reached the maximum plan!\n```", inline=False)
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    async def panel_callback(self, interaction):
        view = PanelInstallView(self.ctx, self.container)
        embed = info_embed("Install Panel", "Select panel to install:")
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    
    async def share_callback(self, interaction):
        modal = ShareModal(self.container)
        await interaction.response.send_modal(modal)
    
    async def live_callback(self, interaction):
        self.live_mode = not self.live_mode
        if self.live_mode:
            self.live_btn.label = "⏹️ Stop Live"
            self.live_btn.style = discord.ButtonStyle.success
            await interaction.response.edit_message(view=self)
            self.live_task = asyncio.create_task(self.live_update_task(interaction))
        else:
            self.live_btn.label = "🔴 Live Mode"
            self.live_btn.style = discord.ButtonStyle.danger
            await interaction.response.edit_message(view=self)
            if self.live_task:
                self.live_task.cancel()
    
    async def live_update_task(self, interaction):
        while self.live_mode:
            try:
                embed = await self.get_stats_embed()
                await interaction.edit_original_response(embed=embed, view=self)
                await asyncio.sleep(5)
            except:
                self.live_mode = False
                break
    
    async def refresh_callback(self, interaction):
        embed = await self.get_stats_embed()
        await interaction.response.edit_message(embed=embed, view=self)


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


class ShareModal(Modal):
    def __init__(self, container):
        super().__init__(title="Share VPS")
        self.container = container
        self.add_item(InputText(label="User ID or @mention"))
        self.add_item(InputText(label="Permissions", placeholder="view, manage, full", required=False, value="view"))
    
    async def callback(self, interaction):
        user_input = self.children[0].value
        perms = self.children[1].value or "view"
        
        user_id = user_input
        if user_input.startswith('<@') and user_input.endswith('>'):
            user_id = user_input[2:-1]
            if user_id.startswith('!'):
                user_id = user_id[1:]
        
        try:
            user = await interaction.client.fetch_user(int(user_id))
            if share_vps(str(interaction.user.id), str(user.id), self.container):
                embed = success_embed("VPS Shared")
                embed.add_field(name="📦 Container", value=f"```fix\n{self.container}\n```", inline=True)
                embed.add_field(name="👤 Shared With", value=user.mention, inline=True)
                embed.add_field(name="🔑 Permissions", value=f"```fix\n{perms}\n```", inline=True)
                await interaction.response.send_message(embed=embed, ephemeral=True)
                
                try:
                    dm = info_embed("VPS Shared With You")
                    dm.add_field(name="📦 Container", value=f"```fix\n{self.container}\n```")
                    dm.add_field(name="👤 Owner", value=interaction.user.mention)
                    await user.send(embed=dm)
                except:
                    pass
            else:
                await interaction.response.send_message(embed=error_embed("Failed"), ephemeral=True)
        except:
            await interaction.response.send_message(embed=error_embed("Invalid User"), ephemeral=True)


# ==================================================================================================
#  📦  PANEL INSTALL VIEW
# ==================================================================================================

class PanelInstallView(View):
    def __init__(self, ctx, container_name: str):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.container = container_name
        self.message = None
        
        ptero_btn = Button(label="🦅 Pterodactyl Panel", style=discord.ButtonStyle.primary, emoji="🦅", row=0)
        ptero_btn.callback = self.ptero_callback
        
        puffer_btn = Button(label="🐡 Pufferpanel", style=discord.ButtonStyle.success, emoji="🐡", row=0)
        puffer_btn.callback = self.puffer_callback
        
        cancel_btn = Button(label="❌ Cancel", style=discord.ButtonStyle.secondary, emoji="❌", row=1)
        cancel_btn.callback = self.cancel_callback
        
        self.add_item(ptero_btn)
        self.add_item(puffer_btn)
        self.add_item(cancel_btn)
    
    async def ptero_callback(self, interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("```diff\n- This menu is not for you!\n```", ephemeral=True)
            return
        await self.install_panel(interaction, "pterodactyl")
    
    async def puffer_callback(self, interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("```diff\n- This menu is not for you!\n```", ephemeral=True)
            return
        await self.install_panel(interaction, "pufferpanel")
    
    async def cancel_callback(self, interaction):
        await interaction.response.edit_message(
            embed=info_embed("Cancelled", "```fix\nPanel installation cancelled.\n```"),
            view=None
        )
    
    async def install_panel(self, interaction, panel_type: str):
        await interaction.response.defer()
        
        admin_user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        admin_email = f"{admin_user}@{random.choice(['gmail.com', 'outlook.com', 'proton.me', 'yandex.com'])}"
        admin_pass = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=16))
        
        progress_msg = await interaction.followup.send(
            embed=discord.Embed(
                title="```glow\n🌈 SVM5-BOT - INSTALLING PANEL 🌈\n```",
                description="```fix\n[░░░░░░░░░░░░░░░░░░░░] 0% | Preparing installation...\n```",
                color=RAINBOW_COLORS[0]
            ),
            ephemeral=True
        )
        
        def get_progress_bar(percent):
            filled = int(percent / 5)
            return "█" * filled + "░" * (20 - filled)
        
        try:
            if panel_type == "pterodactyl":
                steps = [
                    (10, "🔧 Updating system..."),
                    (20, "📦 Installing dependencies..."),
                    (30, "🌐 Installing Nginx, MySQL, Redis..."),
                    (40, "🐘 Installing PHP 8.1..."),
                    (50, "📥 Downloading Pterodactyl..."),
                    (60, "🔧 Configuring environment..."),
                    (70, "📦 Installing Composer packages..."),
                    (80, "🗄️ Setting up database..."),
                    (90, "👤 Creating admin user..."),
                    (100, "🌍 Creating cloudflared tunnel..."),
                ]
                
                color_index = 0
                for progress, desc in steps:
                    await progress_msg.edit(embed=discord.Embed(
                        title="```glow\n🌈 SVM5-BOT - INSTALLING PTERODACTYL 🌈\n```",
                        description=f"```fix\n[{get_progress_bar(progress)}] {progress}% | {desc}\n```",
                        color=RAINBOW_COLORS[color_index % len(RAINBOW_COLORS)]
                    ))
                    color_index += 1
                    
                    if progress == 10:
                        await exec_in_container(self.container, "apt-get update -qq")
                    elif progress == 20:
                        await exec_in_container(self.container, "apt-get install -y -qq curl wget git unzip tar")
                    elif progress == 30:
                        await exec_in_container(self.container, "apt-get install -y -qq nginx mariadb-server redis-server")
                    elif progress == 40:
                        await exec_in_container(self.container, "apt-get install -y -qq php8.1 php8.1-{cli,gd,mysql,pdo,mbstring,tokenizer,bcmath,xml,fpm,curl,zip}")
                    elif progress == 50:
                        await exec_in_container(self.container, "mkdir -p /var/www/pterodactyl")
                        await exec_in_container(self.container, "cd /var/www/pterodactyl && curl -Lo panel.tar.gz https://github.com/pterodactyl/panel/releases/latest/download/panel.tar.gz")
                        await exec_in_container(self.container, "cd /var/www/pterodactyl && tar -xzvf panel.tar.gz && chmod -R 755 storage/* bootstrap/cache/")
                        await exec_in_container(self.container, "cd /var/www/pterodactyl && cp .env.example .env")
                    elif progress == 60:
                        await exec_in_container(self.container, "curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer")
                        await exec_in_container(self.container, "cd /var/www/pterodactyl && composer install --no-dev --optimize-autoloader --no-interaction")
                        await exec_in_container(self.container, "cd /var/www/pterodactyl && php artisan key:generate --force")
                    elif progress == 70:
                        await exec_in_container(self.container, "cd /var/www/pterodactyl && php artisan migrate --seed --force")
                    elif progress == 80:
                        await exec_in_container(self.container, f"cd /var/www/pterodactyl && php artisan p:user:make --email='{admin_email}' --username='{admin_user}' --password='{admin_pass}' --name-first='Admin' --name-last='User' --admin=1 --no-interaction")
                    elif progress == 90:
                        out, _, _ = await exec_in_container(self.container, "ip -4 addr show eth0 | grep -oP '(?<=inet\\s)[0-9.]+' | head -1")
                        ip = out.strip() or SERVER_IP
                        panel_url = f"http://{ip}"
                        tunnel_url = await create_cloudflared_tunnel(self.container, 80)
                        if tunnel_url:
                            panel_url = tunnel_url
                    
                    await asyncio.sleep(1)
                
            else:
                steps = [
                    (10, "🔧 Updating system..."),
                    (20, "📦 Adding Pufferpanel repository..."),
                    (30, "📥 Installing Pufferpanel..."),
                    (40, "⚙️ Configuring services..."),
                    (50, "▶️ Starting Pufferpanel..."),
                    (60, "👤 Creating admin user..."),
                    (70, "🌍 Creating cloudflared tunnel..."),
                    (80, "🔧 Finalizing..."),
                ]
                
                color_index = 0
                for progress, desc in steps:
                    await progress_msg.edit(embed=discord.Embed(
                        title="```glow\n🌈 SVM5-BOT - INSTALLING PUFFERPANEL 🌈\n```",
                        description=f"```fix\n[{get_progress_bar(progress)}] {progress}% | {desc}\n```",
                        color=RAINBOW_COLORS[color_index % len(RAINBOW_COLORS)]
                    ))
                    color_index += 1
                    
                    if progress == 10:
                        await exec_in_container(self.container, "apt-get update -qq")
                    elif progress == 20:
                        await exec_in_container(self.container, "curl -s https://packagecloud.io/install/repositories/pufferpanel/pufferpanel/script.deb.sh | bash")
                    elif progress == 30:
                        await exec_in_container(self.container, "apt-get install -y -qq pufferpanel")
                    elif progress == 40:
                        await exec_in_container(self.container, "systemctl enable pufferpanel")
                    elif progress == 50:
                        await exec_in_container(self.container, "systemctl start pufferpanel")
                    elif progress == 60:
                        await exec_in_container(self.container, f"pufferpanel user add --name '{admin_user}' --email '{admin_email}' --password '{admin_pass}' --admin")
                    elif progress == 70:
                        out, _, _ = await exec_in_container(self.container, "ip -4 addr show eth0 | grep -oP '(?<=inet\\s)[0-9.]+' | head -1")
                        ip = out.strip() or SERVER_IP
                        panel_url = f"http://{ip}:8080"
                        tunnel_url = await create_cloudflared_tunnel(self.container, 8080)
                        if tunnel_url:
                            panel_url = tunnel_url
                    
                    await asyncio.sleep(1)
            
            add_panel(str(self.ctx.author.id), panel_type, panel_url, admin_user, admin_pass, admin_email, self.container, tunnel_url or "")
            
            all_vps = get_all_vps()
            total_vps = len(all_vps)
            total_users = len(set([v['user_id'] for v in all_vps]))
            total_panels = len(get_user_panels(str(self.ctx.author.id)))
            
            success_embed = discord.Embed(
                title="```glow\n✅ PANEL INSTALLED SUCCESSFULLY! ✅\n```",
                description=f"🎉 **{panel_type.title()} has been installed on {self.container}!**\n\n"
                            f"```glow\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n```",
                color=0x00FF88
            )
            success_embed.set_thumbnail(url=THUMBNAIL_URL)
            success_embed.set_image(url=THUMBNAIL_URL)
            
            success_embed.add_field(
                name="🌐 PANEL URL",
                value=f"```fix\n{panel_url}\n```",
                inline=False
            )
            
            if tunnel_url:
                success_embed.add_field(
                    name="🌍 CLOUDFLARED TUNNEL",
                    value=f"```fix\n{tunnel_url}\n```",
                    inline=False
                )
            
            success_embed.add_field(
                name="🔐 CREDENTIALS",
                value=f"```fix\n┌─────────────────────────────────────────────────┐\n│ Username : {admin_user}\n│ Email    : {admin_email}\n│ Password : {admin_pass}\n└─────────────────────────────────────────────────┘\n```",
                inline=False
            )
            
            success_embed.add_field(
                name="📦 CONTAINER",
                value=f"```fix\n{self.container}\n```",
                inline=True
            )
            
            success_embed.add_field(
                name="🔌 PORT",
                value=f"```fix\n{80 if panel_type == 'pterodactyl' else 8080}\n```",
                inline=True
            )
            
            success_embed.add_field(
                name="🌍 PUBLIC STATISTICS",
                value=f"```fix\n┌─────────────────────────────────────────────────┐\n│ Total VPS Created : {total_vps}\n│ Total Users       : {total_users}\n│ Panels Installed  : {total_panels}\n└─────────────────────────────────────────────────┘\n```",
                inline=False
            )
            
            success_embed.set_footer(
                text=f"⚡ SVM5-BOT • Installed by {self.ctx.author.name} • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ⚡",
                icon_url=THUMBNAIL_URL
            )
            
            await progress_msg.edit(embed=success_embed)
            
            try:
                dm_embed = discord.Embed(
                    title="```glow\n🔐 PANEL CREDENTIALS\n```",
                    description=f"Your {panel_type.title()} panel has been installed successfully!",
                    color=0x57F287
                )
                dm_embed.set_thumbnail(url=THUMBNAIL_URL)
                dm_embed.add_field(
                    name="🌐 PANEL URL",
                    value=f"```fix\n{panel_url}\n```",
                    inline=False
                )
                if tunnel_url:
                    dm_embed.add_field(
                        name="🌍 TUNNEL URL",
                        value=f"```fix\n{tunnel_url}\n```",
                        inline=False
                    )
                dm_embed.add_field(
                    name="🔐 LOGIN",
                    value=f"```fix\nUsername: {admin_user}\nEmail: {admin_email}\nPassword: {admin_pass}\n```",
                    inline=False
                )
                dm_embed.add_field(
                    name="📦 CONTAINER",
                    value=f"```fix\n{self.container}\n```",
                    inline=True
                )
                await self.ctx.author.send(embed=dm_embed)
            except:
                pass
            
            logger.info(f"User {self.ctx.author} installed {panel_type} on {self.container}")
            
        except Exception as e:
            await progress_msg.edit(embed=error_embed("Installation Failed", f"```diff\n- {str(e)[:500]}\n```"))


# ==================================================================================================
#  🖥️  COMPLETE .manage COMMAND
# ==================================================================================================

@bot.command(name="manage")
async def manage(ctx, container_name: str = None):
    """Interactive VPS manager with all buttons"""
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
    msg = await ctx.send(embed=embed, view=view)
    view.message = msg


# ==================================================================================================
#  📚  COMPLETE HELP COMMAND WITH SELECT MENU
# ==================================================================================================

HELP_IMAGES = {
    'home': THUMBNAIL_URL,
    'user': THUMBNAIL_URL,
    'vps': THUMBNAIL_URL,
    'console': THUMBNAIL_URL,
    'games': THUMBNAIL_URL,
    'tools': THUMBNAIL_URL,
    'nodes': THUMBNAIL_URL,
    'share': THUMBNAIL_URL,
    'ports': THUMBNAIL_URL,
    'ipv4': THUMBNAIL_URL,
    'panels': THUMBNAIL_URL,
    'ai': THUMBNAIL_URL,
    'os': THUMBNAIL_URL,
    'admin': THUMBNAIL_URL,
    'owner': THUMBNAIL_URL,
    'ip': THUMBNAIL_URL,
}

class HelpView(View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.current_category = "home"
        self.message = None
        
        self.category_options = [
            discord.SelectOption(label="🏠 Home", value="home", emoji="🏠", description="Main menu with overview"),
            discord.SelectOption(label="👤 User Commands", value="user", emoji="👤", description="User commands"),
            discord.SelectOption(label="🖥️ VPS Commands", value="vps", emoji="🖥️", description="VPS management commands"),
            discord.SelectOption(label="📟 Console Commands", value="console", emoji="📟", description="Console commands"),
            discord.SelectOption(label="🎮 Games Commands", value="games", emoji="🎮", description="Game server commands"),
            discord.SelectOption(label="🛠️ Tools Commands", value="tools", emoji="🛠️", description="Development tools"),
            discord.SelectOption(label="🌐 Node Commands", value="nodes", emoji="🌐", description="Cluster management commands"),
            discord.SelectOption(label="👥 Share Commands", value="share", emoji="👥", description="VPS sharing commands"),
            discord.SelectOption(label="🔌 Port Commands", value="ports", emoji="🔌", description="Port forwarding commands"),
            discord.SelectOption(label="🌍 IPv4 Commands", value="ipv4", emoji="🌍", description="IPv4 management commands"),
            discord.SelectOption(label="📦 Panel Commands", value="panels", emoji="📦", description="Panel installation commands"),
            discord.SelectOption(label="🤖 AI Commands", value="ai", emoji="🤖", description="AI chat commands"),
            discord.SelectOption(label="🐧 OS Commands", value="os", emoji="🐧", description="Operating systems"),
            discord.SelectOption(label="🌐 IP Commands", value="ip", emoji="🌐", description="IP management commands"),
        ]
        
        self.select = Select(placeholder="📋 Select a command category...", options=self.category_options)
        self.select.callback = self.select_callback
        self.add_item(self.select)
        
        refresh_btn = Button(label="🔄 Refresh", style=discord.ButtonStyle.secondary, emoji="🔄", row=1)
        refresh_btn.callback = self.refresh_callback
        self.add_item(refresh_btn)
        
        delete_btn = Button(label="🗑️ Close", style=discord.ButtonStyle.danger, emoji="🗑️", row=1)
        delete_btn.callback = self.delete_callback
        self.add_item(delete_btn)
        
        self.update_embed()
    
    def update_embed(self):
        categories = {
            'home': {
                'title': "🏠 SVM5-BOT TOOLS - ULTIMATE VPS MANAGEMENT",
                'desc': f"```glow\nWelcome to {BOT_NAME} - Complete VPS Management Solution\n```\n**Select a category from the dropdown menu to view commands.**",
                'fields': [
                    ("👤 USER", "Basic commands for all users", True),
                    ("🖥️ VPS", "Manage your VPS containers", True),
                    ("📟 CONSOLE", "Terminal access and commands", True),
                    ("🎮 GAMES", "Game server management", True),
                    ("🛠️ TOOLS", "Development tools", True),
                    ("🌐 NODES", "Cluster management", True),
                    ("👥 SHARE", "Share VPS with users", True),
                    ("🔌 PORTS", "Port forwarding", True),
                    ("🌍 IPv4", "IPv4 management", True),
                    ("📦 PANELS", "Panel installation", True),
                    ("🤖 AI", "AI assistant", True),
                    ("🐧 OS", "Operating systems", True),
                    ("🌐 IP", "IP management", True),
                ]
            },
            'user': {
                'title': "👤 USER COMMANDS",
                'desc': "```fix\nBasic commands available to all users\n```",
                'fields': [
                    (".help", "Show this interactive help menu", False),
                    (".ping", "Check bot latency", False),
                    (".uptime", "Show bot uptime", False),
                    (".bot-info", "Detailed bot information", False),
                    (".server-info", "Show server hardware info", False),
                    (".plans", "View free VPS plans", False),
                    (".stats", "View your statistics", False),
                    (".inv", "Check your invites", False),
                    (".invites-top", "Show top inviters", False),
                    (".claim-free", "Claim free VPS with invites", False),
                    (".my-acc", "View your generated account", False),
                    (".gen-acc", "Generate random account", False),
                    (".api-key", "View or regenerate API key", False),
                    (".userinfo", "User information", False),
                ]
            },
            'vps': {
                'title': "🖥️ VPS COMMANDS",
                'desc': "```fix\nManage your VPS containers with interactive buttons\n```",
                'fields': [
                    (".myvps", "List your VPS with status", False),
                    (".list", "Detailed VPS list with IPs", False),
                    (".manage", "Interactive VPS manager with 20+ buttons", False),
                    (".stats", "View VPS statistics", False),
                    (".logs", "View VPS logs", False),
                    (".reboot", "Reboot VPS", False),
                    (".shutdown", "Shutdown VPS", False),
                    (".rename", "Rename VPS container", False),
                ]
            },
            'console': {
                'title': "📟 CONSOLE COMMANDS",
                'desc': "```fix\nTerminal access and console commands\n```",
                'fields': [
                    (".ss", "Take VPS snapshot/console output", False),
                    (".console", "Interactive console with modal", False),
                    (".execute", "Execute command in VPS", False),
                    (".ssh-gen", "Generate temporary SSH access", False),
                    (".top", "Show live process monitor", False),
                    (".df", "Show disk usage", False),
                    (".free", "Show memory usage", False),
                    (".ps", "Show process list", False),
                    (".who", "Show logged-in users", False),
                ]
            },
        }
        
        if is_admin(str(self.ctx.author.id)):
            categories['admin'] = {
                'title': "🛡️ ADMIN COMMANDS",
                'desc': "```fix\nAdministrator commands\n```",
                'fields': [
                    (".create", "Create VPS for user", False),
                    (".delete", "Delete user's VPS", False),
                    (".suspend", "Suspend VPS", False),
                    (".unsuspend", "Unsuspend VPS", False),
                    (".add-resources", "Add resources", False),
                    (".list-all", "List all VPS in system", False),
                    (".add-inv", "Add invites", False),
                    (".remove-inv", "Remove invites", False),
                    (".ports-add", "Add port slots", False),
                    (".serverstats", "Server statistics", False),
                    (".license-verify", "License key verifying", False),
                ]
            }
        
        cat_data = categories.get(self.current_category, categories['home'])
        
        embed = discord.Embed(
            title=f"```glow\n{cat_data['title']}\n```",
            description=cat_data['desc'],
            color=COLORS['primary']
        )
        
        embed.set_thumbnail(url=HELP_IMAGES.get(self.current_category, THUMBNAIL_URL))
        embed.set_image(url=THUMBNAIL_URL)
        
        for name, value, inline in cat_data['fields']:
            embed.add_field(name=f"**{name}**", value=value, inline=inline)
        
        embed.set_footer(
            text=f"⚡ {BOT_NAME} • Use dropdown to navigate ⚡",
            icon_url=THUMBNAIL_URL
        )
        
        self.embed = embed
    
    async def select_callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("```diff\n- This menu is not for you!\n```", ephemeral=True)
            return
        
        self.current_category = self.select.values[0]
        self.update_embed()
        await interaction.response.edit_message(embed=self.embed, view=self)
    
    async def refresh_callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("```diff\n- This menu is not for you!\n```", ephemeral=True)
            return
        
        self.update_embed()
        await interaction.response.edit_message(embed=self.embed, view=self)
    
    async def delete_callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message("```diff\n- This menu is not for you!\n```", ephemeral=True)
            return
        
        await interaction.message.delete()


@bot.command(name="help")
async def help_command(ctx):
    if not LICENSE_VERIFIED and not is_admin(str(ctx.author.id)):
        return await ctx.send(embed=error_embed("License Required", "Please verify license first."))
    view = HelpView(ctx)
    await ctx.send(embed=view.embed, view=view)


@bot.command(name="commands")
async def commands_alias(ctx):
    await help_command(ctx)


# ==================================================================================================
#  🔐  LICENSE VERIFY COMMAND
# ==================================================================================================

@bot.command(name="license-verify")
async def license_verify(ctx, key: str = None):
    """Verify your license key"""
    global LICENSE_VERIFIED
    
    if key is None:
        if LICENSE_VERIFIED:
            embed = success_embed("License Verified", "```fix\nYour license is active and verified.\n```")
        else:
            embed = warning_embed("License Not Verified", "```fix\nNo valid license found. Use .license-verify <key> to activate.\n```")
            embed.add_field(
                name="📌 Valid License Keys",
                value="```fix\nprime2026\npreimdragon\ngamerhindu\n```",
                inline=False
            )
        return await ctx.send(embed=embed)
    
    if key in VALID_LICENSE_KEYS:
        set_setting('license_verified', 'true')
        LICENSE_VERIFIED = True
        
        conn = get_db()
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS license_info (
            license_key TEXT, activated_by TEXT, activated_at TEXT, ip TEXT, mac TEXT
        )''')
        cur.execute('INSERT INTO license_info VALUES (?, ?, ?, ?, ?)',
                   (key, str(ctx.author.id), datetime.now().isoformat(), SERVER_IP, MAC_ADDRESS))
        conn.commit()
        conn.close()
        
        embed = success_embed("✅ License Verified Successfully!")
        embed.add_field(name="🔑 License Key", value=f"```fix\n{key}\n```", inline=True)
        embed.add_field(name="👤 Activated By", value=ctx.author.mention, inline=True)
        embed.set_image(url=THUMBNAIL_URL)
        
        await ctx.send(embed=embed)
    else:
        embed = error_embed("Invalid License Key", f"```diff\n- The key '{key}' is not valid.\n```")
        await ctx.send(embed=embed)


@bot.command(name="license-status")
async def license_status(ctx):
    """Show license status"""
    if LICENSE_VERIFIED:
        embed = success_embed("License Status", "```fix\nLicense is active.\n```")
    else:
        embed = warning_embed("License Status", "```fix\nNo active license found.\n```")
        embed.add_field(name="📌 Activate", value=f"Use `{BOT_PREFIX}license-verify <key>` to activate.", inline=False)
    await ctx.send(embed=embed)


# ==================================================================================================
#  👤  USER COMMANDS
# ==================================================================================================

@bot.command(name="ping")
async def ping(ctx):
    start = time.time()
    msg = await ctx.send(embed=info_embed("Pinging..."))
    end = time.time()
    embed = success_embed("Pong! 🏓")
    embed.add_field(name="📡 API", value=f"```fix\n{round(bot.latency*1000)}ms\n```", inline=True)
    embed.add_field(name="⏱️ Response", value=f"```fix\n{round((end-start)*1000)}ms\n```", inline=True)
    await msg.edit(embed=embed)


@bot.command(name="uptime")
async def uptime_bot(ctx):
    delta = datetime.utcnow() - bot.start_time
    hours = delta.total_seconds() // 3600
    minutes = (delta.total_seconds() % 3600) // 60
    seconds = delta.total_seconds() % 60
    embed = info_embed("Bot Uptime", f"```fix\n{int(hours)}h {int(minutes)}m {int(seconds)}s\n```")
    await ctx.send(embed=embed)


@bot.command(name="bot-info")
async def bot_info(ctx):
    embed = info_embed("Bot Information")
    embed.add_field(name="📦 Version", value="```fix\n1.0.0\n```", inline=True)
    embed.add_field(name="👑 Author", value=f"```fix\n{BOT_AUTHOR}\n```", inline=True)
    embed.add_field(name="🖥️ VPS", value=f"```fix\n{len(get_all_vps())}\n```", inline=True)
    embed.add_field(name="🐧 OS", value=f"```fix\n{len(OS_OPTIONS)}\n```", inline=True)
    embed.add_field(name="🎮 Games", value=f"```fix\n{len(GAMES_LIST)}\n```", inline=True)
    embed.add_field(name="🛠️ Tools", value=f"```fix\n{len(TOOLS_LIST)}\n```", inline=True)
    embed.add_field(name="🌐 IP", value=f"```fix\n{SERVER_IP}\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="server-info")
async def server_info(ctx):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    embed = info_embed("Server Information")
    embed.add_field(name="💻 Hostname", value=f"```fix\n{HOSTNAME}\n```", inline=True)
    embed.add_field(name="🌐 IP", value=f"```fix\n{SERVER_IP}\n```", inline=True)
    embed.add_field(name="⚙️ CPU", value=f"```fix\n{psutil.cpu_count()} cores @ {cpu}%\n```", inline=True)
    embed.add_field(name="💾 RAM", value=f"```fix\n{mem.used//1024//1024}MB/{mem.total//1024//1024}MB ({mem.percent}%)\n```", inline=True)
    embed.add_field(name="📀 Disk", value=f"```fix\n{disk.used//1024//1024//1024}GB/{disk.total//1024//1024//1024}GB ({disk.percent}%)\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="plans")
async def plans(ctx):
    embed = info_embed("Free VPS Plans")
    for p in FREE_VPS_PLANS['invites']:
        embed.add_field(name=f"{p['emoji']} {p['name']}", value=f"```fix\nRAM: {p['ram']}GB | CPU: {p['cpu']} | Disk: {p['disk']}GB\nInvites: {p['invites']}\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="inv")
async def inv(ctx):
    s = get_user_stats(str(ctx.author.id))
    await ctx.send(embed=info_embed("Your Invites", f"```fix\n{s.get('invites',0)}\n```"))


@bot.command(name="invites-top")
async def invites_top(ctx, lim: int = 10):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT user_id, invites FROM user_stats WHERE invites > 0 ORDER BY invites DESC LIMIT ?', (lim,))
    rows = cur.fetchall()
    conn.close()
    if not rows:
        return await ctx.send(embed=info_embed("No invites"))
    embed = info_embed(f"Top {min(lim,len(rows))} Inviters")
    medals = ["🥇","🥈","🥉"]
    for i, r in enumerate(rows,1):
        try:
            u = await bot.fetch_user(int(r['user_id']))
            name = u.name
        except:
            name = "Unknown"
        m = medals[i-1] if i<=3 else f"{i}."
        embed.add_field(name=f"{m} {name}", value=f"```fix\nInvites: {r['invites']}\n```", inline=False)
    await ctx.send(embed=embed)


@bot.command(name="gen-acc")
async def gen_acc(ctx):
    adj = ["cool","fast","dark","epic","blue","swift","neon","alpha","delta"]
    noun = ["wolf","tiger","storm","byte","nova","blade","fox","raven","hawk"]
    name = f"{random.choice(adj)}{random.choice(noun)}{random.randint(10,999)}"
    email = f"{name}@{random.choice(['gmail.com','yahoo.com','outlook.com'])}"
    pwd = ''.join(random.choices(string.ascii_letters+string.digits+"!@#$%", k=16))
    api = hashlib.sha256(f"{ctx.author.id}{time.time()}".encode()).hexdigest()[:32]
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS generated_accounts (user_id TEXT PRIMARY KEY, username TEXT, email TEXT, password TEXT, api_key TEXT, created_at TEXT)''')
    cur.execute('INSERT OR REPLACE INTO generated_accounts VALUES (?,?,?,?,?,?)', (str(ctx.author.id), name, email, pwd, api, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    try:
        dm = success_embed("Your Account")
        dm.add_field(name="👤 Username", value=f"```fix\n{name}\n```")
        dm.add_field(name="📧 Email", value=f"```fix\n{email}\n```")
        dm.add_field(name="🔑 Password", value=f"```fix\n{pwd}\n```")
        dm.add_field(name="🗝️ API", value=f"```fix\n{api}\n```")
        await ctx.author.send(embed=dm)
        await ctx.send(embed=success_embed("Account Generated", "Check your DMs!"))
    except:
        await ctx.send(embed=error_embed("DM Failed", "Enable DMs to receive credentials."))


@bot.command(name="my-acc")
async def my_acc(ctx):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM generated_accounts WHERE user_id = ?', (str(ctx.author.id),))
    row = cur.fetchone()
    conn.close()
    if row:
        embed = info_embed("Your Account")
        embed.add_field(name="👤 Username", value=f"```fix\n{row['username']}\n```")
        embed.add_field(name="📧 Email", value=f"```fix\n{row['email']}\n```")
        embed.add_field(name="🗝️ API", value=f"```fix\n{row['api_key']}\n```")
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=info_embed("No Account", "Use `.gen-acc` to create one."))


@bot.command(name="api-key")
async def api_key_cmd(ctx, action: str = "view"):
    uid = str(ctx.author.id)
    if action.lower() == "regenerate":
        new = hashlib.sha256(f"{uid}{time.time()}{random.randint(1000,9999)}".encode()).hexdigest()[:32]
        conn = get_db()
        cur = conn.cursor()
        cur.execute('UPDATE user_stats SET api_key = ?, last_updated = ? WHERE user_id = ?', (new, datetime.now().isoformat(), uid))
        conn.commit()
        conn.close()
        await ctx.send(embed=success_embed("API Key Regenerated", f"```fix\n{new}\n```"))
    else:
        s = get_user_stats(uid)
        await ctx.send(embed=info_embed("Your API Key", f"```fix\n{s.get('api_key','None')}\n```"))


@bot.command(name="userinfo")
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    elif not is_admin(str(ctx.author.id)) and user.id != ctx.author.id:
        return await ctx.send(embed=error_embed("Access Denied", "You can only view yourself."))
    uid = str(user.id)
    vps = get_user_vps(uid)
    s = get_user_stats(uid)
    embed = info_embed(f"User: {user.display_name}")
    embed.set_thumbnail(url=user.avatar.url if user.avatar else THUMBNAIL_URL)
    embed.add_field(name="🆔 ID", value=f"```fix\n{user.id}\n```", inline=True)
    embed.add_field(name="📨 Invites", value=f"```fix\n{s.get('invites',0)}\n```", inline=True)
    embed.add_field(name="🖥️ VPS", value=f"```fix\n{len(vps)}\n```", inline=True)
    if vps:
        text = "\n".join([f"{'🟢' if v['status']=='running' else '🔴'} `{v['container_name']}`" for v in vps[:3]])
        embed.add_field(name="📋 VPS List", value=text, inline=False)
    await ctx.send(embed=embed)


# ==================================================================================================
#  🖥️  VPS COMMANDS
# ==================================================================================================

@bot.command(name="myvps")
async def myvps(ctx):
    vps = get_user_vps(str(ctx.author.id))
    if not vps:
        return await ctx.send(embed=no_vps_embed())
    embed = info_embed(f"Your VPS ({len(vps)})")
    for i, v in enumerate(vps,1):
        status = "🟢" if v['status']=='running' and not v['suspended'] else "⛔" if v['suspended'] else "🔴"
        text = f"{status} **`{v['container_name']}`**\n```fix\nRAM: {v['ram']}GB | CPU: {v['cpu']} | Disk: {v['disk']}GB\nIP: {v.get('ip_address','N/A')}\n```"
        embed.add_field(name=f"VPS #{i}", value=text, inline=False)
    await ctx.send(embed=embed)


@bot.command(name="list")
async def list_cmd(ctx):
    await myvps(ctx)


@bot.command(name="stats")
async def vps_stats(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    stats = await get_container_stats(container)
    embed = info_embed(f"Stats: {container}")
    embed.add_field(name="📊 Status", value=f"```fix\n{stats['status'].upper()}\n```", inline=True)
    embed.add_field(name="💾 CPU", value=f"```fix\n{stats['cpu']}\n```", inline=True)
    embed.add_field(name="📀 Memory", value=f"```fix\n{stats['memory']}\n```", inline=True)
    embed.add_field(name="💽 Disk", value=f"```fix\n{stats['disk']}\n```", inline=True)
    embed.add_field(name="🌐 IP", value=f"```fix\n{stats['ipv4'][0] if stats['ipv4'] else 'N/A'}\n```", inline=True)
    embed.add_field(name="🔌 MAC", value=f"```fix\n{stats['mac']}\n```", inline=True)
    embed.add_field(name="⏱️ Uptime", value=f"```fix\n{stats['uptime']}\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="logs")
async def logs(ctx, container: str = None, lines: int = 50):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    
    lines = min(lines,200)
    out,_,_ = await exec_in_container(container, f"journalctl -n {lines} --no-pager 2>/dev/null || dmesg | tail -{lines}")
    embed = terminal_embed(f"Logs: {container}", out[:1900])
    await ctx.send(embed=embed)


@bot.command(name="reboot")
async def reboot(ctx, container: str):
    uid = str(ctx.author.id)
    if not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    await ctx.send(embed=info_embed("Rebooting", f"```fix\n{container}\n```"))
    await run_lxc(f"lxc restart {container}")
    update_vps_status(container, 'running')
    await ctx.send(embed=success_embed("Rebooted", f"```fix\n{container}\n```"))


@bot.command(name="shutdown")
async def shutdown(ctx, container: str):
    uid = str(ctx.author.id)
    if not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    await ctx.send(embed=info_embed("Shutting Down", f"```fix\n{container}\n```"))
    await run_lxc(f"lxc stop {container}")
    update_vps_status(container, 'stopped')
    await ctx.send(embed=success_embed("Shutdown", f"```fix\n{container}\n```"))


@bot.command(name="rename")
async def rename(ctx, old: str, new: str):
    uid = str(ctx.author.id)
    if not any(v['container_name']==old for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$', new):
        return await ctx.send(embed=error_embed("Invalid Name", "Use letters, numbers, hyphens only."))
    await ctx.send(embed=info_embed("Renaming", f"```fix\n{old} → {new}\n```"))
    status = await get_container_status(old)
    was = status == 'running'
    if was:
        await run_lxc(f"lxc stop {old}")
        await asyncio.sleep(2)
    await run_lxc(f"lxc move {old} {new}")
    if was:
        await run_lxc(f"lxc start {new}")
    conn = get_db()
    cur = conn.cursor()
    for t in ['vps','shared_vps','installed_games','installed_tools','ipv4','port_forwards','panels']:
        cur.execute(f'UPDATE {t} SET container_name = ? WHERE container_name = ?', (new, old))
    conn.commit()
    conn.close()
    await ctx.send(embed=success_embed("Renamed", f"```fix\n{old} → {new}\n```"))


# ==================================================================================================
#  📟  CONSOLE COMMANDS
# ==================================================================================================

@bot.command(name="ss")
async def ss(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    msg = await ctx.send(embed=info_embed("📸 Snapshot", f"```fix\n{container}\n```"))
    u,_,_ = await exec_in_container(container, "uname -a")
    up,_,_ = await exec_in_container(container, "uptime")
    m,_,_ = await exec_in_container(container, "free -h")
    d,_,_ = await exec_in_container(container, "df -h")
    p,_,_ = await exec_in_container(container, "ps aux | head -15")
    out = f"=== {container} ===\nUname: {u}\nUptime: {up}\n\n{m}\n\n{d}\n\n{p}"
    embed = terminal_embed(f"Snapshot: {container}", out[:1900])
    await msg.edit(embed=embed)


@bot.command(name="console")
async def console(ctx, container: str, *, cmd: str = None):
    uid = str(ctx.author.id)
    if not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    if not cmd:
        view = View()
        btn = Button(label="⚡ Run Command", style=discord.ButtonStyle.primary)
        async def btn_cb(i):
            modal = CommandModal(container)
            await i.response.send_modal(modal)
        btn.callback = btn_cb
        view.add_item(btn)
        return await ctx.send(embed=info_embed(f"Console: {container}", "Click button to run command"), view=view)
    
    msg = await ctx.send(embed=info_embed("Executing", f"```fix\n$ {cmd}\n```"))
    out, err, code = await exec_in_container(container, cmd)
    embed = terminal_embed(f"Output", f"$ {cmd}\n\n{(out or err)[:1900]}")
    embed.add_field(name="Exit Code", value=f"```fix\n{code}\n```")
    await msg.edit(embed=embed)


@bot.command(name="execute")
async def execute(ctx, container: str, *, cmd: str):
    await console(ctx, container, cmd=cmd)


@bot.command(name="top")
async def top(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    out,_,_ = await exec_in_container(container, "ps aux --sort=-%cpu | head -20")
    embed = terminal_embed(f"Top: {container}", out)
    await ctx.send(embed=embed)


@bot.command(name="df")
async def df(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    out,_,_ = await exec_in_container(container, "df -h")
    embed = terminal_embed(f"Disk: {container}", out)
    await ctx.send(embed=embed)


@bot.command(name="free")
async def free(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    out,_,_ = await exec_in_container(container, "free -h")
    embed = terminal_embed(f"Memory: {container}", out)
    await ctx.send(embed=embed)


@bot.command(name="ps")
async def ps_cmd(ctx, container: str = None):
    await top(ctx, container)


@bot.command(name="who")
async def who(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    out,_,_ = await exec_in_container(container, "who")
    embed = terminal_embed(f"Users: {container}", out or "No users")
    await ctx.send(embed=embed)


@bot.command(name="uptime")
async def uptime_cmd(ctx, container: str = None):
    uid = str(ctx.author.id)
    if not container:
        vps = get_user_vps(uid)
        if not vps:
            return await ctx.send(embed=no_vps_embed())
        container = vps[0]['container_name']
    elif not any(v['container_name']==container for v in get_user_vps(uid)):
        return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
    out,_,_ = await exec_in_container(container, "uptime")
    await ctx.send(embed=info_embed(f"Uptime: {container}", f"```fix\n{out}\n```"))


# ==================================================================================================
#  🎮  GAMES COMMANDS (Simplified)
# ==================================================================================================

@bot.command(name="games")
async def games(ctx):
    embed = info_embed("Available Games", f"```fix\nTotal: {len(GAMES_LIST)}\n```")
    for g in GAMES_LIST:
        embed.add_field(name=f"{g['icon']} {g['name']}", value=f"```fix\nPort: {g['port']} | RAM: {g['ram']}MB\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="game-info")
async def game_info(ctx, *, name: str):
    g = next((x for x in GAMES_LIST if x['name'].lower() == name.lower()), None)
    if not g:
        return await ctx.send(embed=error_embed("Not Found", f"```diff\n- {name}\n```"))
    embed = info_embed(f"{g['icon']} {g['name']}")
    embed.add_field(name="🔌 Port", value=f"```fix\n{g['port']}\n```", inline=True)
    embed.add_field(name="💾 RAM", value=f"```fix\n{g['ram']}MB\n```", inline=True)
    embed.add_field(name="🐳 Docker", value=f"```fix\n{g['docker']}\n```", inline=False)
    await ctx.send(embed=embed)


@bot.command(name="my-games")
async def my_games(ctx, container: str = None):
    uid = str(ctx.author.id)
    conn = get_db()
    cur = conn.cursor()
    if container:
        cur.execute('SELECT * FROM installed_games WHERE user_id = ? AND container_name = ?', (uid, container))
    else:
        cur.execute('SELECT * FROM installed_games WHERE user_id = ?', (uid,))
    rows = cur.fetchall()
    conn.close()
    if not rows:
        return await ctx.send(embed=info_embed("No Games", "No games installed."))
    embed = info_embed("Your Games")
    for r in rows:
        embed.add_field(name=f"🎮 {r['game_name']}", value=f"```fix\nContainer: {r['container_name']}\nPort: {r['game_port']}\n```", inline=False)
    await ctx.send(embed=embed)


# ==================================================================================================
#  🛠️  TOOLS COMMANDS (Simplified)
# ==================================================================================================

@bot.command(name="tools")
async def tools(ctx):
    embed = info_embed("Available Tools", f"```fix\nTotal: {len(TOOLS_LIST)}\n```")
    for t in TOOLS_LIST:
        embed.add_field(name=f"{t['icon']} {t['name']}", value=f"```fix\nPort: {t.get('port','None')}\n```", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="tool-info")
async def tool_info(ctx, *, name: str):
    t = next((x for x in TOOLS_LIST if x['name'].lower() == name.lower()), None)
    if not t:
        return await ctx.send(embed=error_embed("Not Found", f"```diff\n- {name}\n```"))
    embed = info_embed(f"{t['icon']} {t['name']}")
    if t.get('port'):
        embed.add_field(name="🔌 Port", value=f"```fix\n{t['port']}\n```", inline=True)
    embed.add_field(name="📝 Command", value=f"```bash\n{t['cmd']}\n```", inline=False)
    await ctx.send(embed=embed)


@bot.command(name="my-tools")
async def my_tools(ctx, container: str = None):
    uid = str(ctx.author.id)
    conn = get_db()
    cur = conn.cursor()
    if container:
        cur.execute('SELECT * FROM installed_tools WHERE user_id = ? AND container_name = ?', (uid, container))
    else:
        cur.execute('SELECT * FROM installed_tools WHERE user_id = ?', (uid,))
    rows = cur.fetchall()
    conn.close()
    if not rows:
        return await ctx.send(embed=info_embed("No Tools", "No tools installed."))
    embed = info_embed("Your Tools")
    for r in rows:
        embed.add_field(name=f"🛠️ {r['tool_name']}", value=f"```fix\nContainer: {r['container_name']}\nPort: {r['tool_port'] or 'None'}\n```", inline=False)
    await ctx.send(embed=embed)


# ==================================================================================================
#  🌐  IP COMMANDS (Simplified)
# ==================================================================================================

@bot.command(name="ip")
async def ip_cmd(ctx, target: str = None):
    """Main IP command - show your IP information"""
    if target and target.lower() == "public":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.ipify.org', timeout=5) as resp:
                    public_ip = await resp.text()
            embed = info_embed("Public IP", f"```fix\n{public_ip}\n```")
            await ctx.send(embed=embed)
        except:
            await ctx.send(embed=error_embed("Failed", "Could not get public IP"))
    else:
        embed = info_embed("Your IP Information")
        embed.add_field(name="🌍 Public IP", value=f"```fix\n{SERVER_IP}\n```", inline=True)
        embed.add_field(name="🔌 MAC Address", value=f"```fix\n{MAC_ADDRESS}\n```", inline=True)
        embed.add_field(name="🖥️ Hostname", value=f"```fix\n{HOSTNAME}\n```", inline=True)
        await ctx.send(embed=embed)


@bot.command(name="myip")
async def my_ip(ctx):
    await ip_cmd(ctx, "public")


@bot.command(name="mac")
async def mac_address(ctx, container: str = None):
    if container:
        uid = str(ctx.author.id)
        if not any(v['container_name'] == container for v in get_user_vps(uid)):
            return await ctx.send(embed=error_embed("Access Denied", "You don't own this VPS."))
        stats = await get_container_stats(container)
        embed = info_embed(f"MAC Address: {container}")
        embed.add_field(name="MAC Address", value=f"```fix\n{stats['mac']}\n```", inline=False)
        await ctx.send(embed=embed)
    else:
        embed = info_embed("Server MAC Address")
        embed.add_field(name="MAC Address", value=f"```fix\n{MAC_ADDRESS}\n```", inline=False)
        await ctx.send(embed=embed)


# ==================================================================================================
#  👑  OWNER/ADMIN COMMANDS (Simplified)
# ==================================================================================================

@bot.command(name="admin-add")
@commands.check(lambda ctx: str(ctx.author.id) in [str(a) for a in MAIN_ADMIN_IDS])
async def owner_admin_add(ctx, user: discord.Member):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT OR IGNORE INTO admins (user_id, added_at) VALUES (?, ?)', 
               (str(user.id), datetime.now().isoformat()))
    conn.commit()
    conn.close()
    await ctx.send(embed=success_embed("Admin Added", f"{user.mention} is now an admin"))


@owner_admin_add.error
async def owner_admin_add_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"❌ {ctx.author.mention}, you do not have permission to use this command!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Could not find that user. Please mention a valid member.")


@bot.command(name="admin-remove")
@commands.check(lambda ctx: str(ctx.author.id) in [str(a) for a in MAIN_ADMIN_IDS])
async def owner_admin_remove(ctx, user: discord.Member):
    if str(user.id) in [str(a) for a in MAIN_ADMIN_IDS]:
        return await ctx.send(embed=error_embed("Cannot Remove", "Cannot remove main admin"))
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM admins WHERE user_id = ?', (str(user.id),))
    conn.commit()
    conn.close()
    await ctx.send(embed=success_embed("Admin Removed", f"{user.mention} is no longer admin"))


@bot.command(name="admin-list")
@commands.check(lambda ctx: str(ctx.author.id) in [str(a) for a in MAIN_ADMIN_IDS])
async def owner_admin_list(ctx):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT user_id FROM admins')
    rows = cur.fetchall()
    conn.close()
    main = "\n".join([f"👑 <@{a}>" for a in MAIN_ADMIN_IDS])
    admins = "\n".join([f"🛡️ <@{r['user_id']}>" for r in rows if r['user_id'] not in [str(a) for a in MAIN_ADMIN_IDS]])
    embed = info_embed("Admin List")
    embed.add_field(name="Main Admin", value=main or "None", inline=False)
    embed.add_field(name="Admins", value=admins or "None", inline=False)
    await ctx.send(embed=embed)


# ==================================================================================================
#  🚀  RUN THE BOT
# ==================================================================================================

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_DISCORD_BOT_TOKEN_HERE":
        print("\n❌ ERROR: Please set your BOT_TOKEN!")
        sys.exit(1)
    update_local_node_stats()
    try:
        bot.run(BOT_TOKEN)
    except discord.LoginFailure:
        print("\n❌ ERROR: Invalid Discord token!")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

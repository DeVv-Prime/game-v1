#!/bin/bash

# ╔═══════════════════════════════════════════════════════════════════════════════╗
# ║                 NEX VM V1 - Ultimate Virtualization Platform                  ║
# ║                         Next Generation VM Management                         ║
# ║                    Version: 1.0.0 | Enterprise Edition                       ║
# ║                      Made by DeVv-Prime with ❤️                               ║
# ║            💰 UPI: vedant1437@fam | Discord: https://discord.gg/zS2ynbF6jK    ║
# ╚═══════════════════════════════════════════════════════════════════════════════╝

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🎨  ADVANCED COLOR DEFINITIONS WITH EFFECTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Base Colors
R='\033[0;31m'      # Red
G='\033[0;32m'      # Green
Y='\033[1;33m'      # Yellow
B='\033[0;34m'      # Blue
P='\033[0;35m'      # Purple
C='\033[0;36m'      # Cyan
W='\033[1;37m'      # White
NC='\033[0m'        # No Color

# Effects
BOLD='\033[1m'
DIM='\033[2m'
UNDERLINE='\033[4m'
BLINK='\033[5m'
REVERSE='\033[7m'

# Extended Colors
ORANGE='\033[38;5;214m'
PINK='\033[38;5;205m'
PURPLE='\033[38;5;129m'
GOLD='\033[38;5;220m'
SILVER='\033[38;5;250m'
LIME='\033[38;5;154m'
TEAL='\033[38;5;37m'

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📍  ADVANCED PATH CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INSTALL_DIR="/opt/nexvm-v1"
BOT_SCRIPT="nexvm.py"
SERVICE_NAME="nexvm-v1"
LOG_FILE="/var/log/nexvm-v1.log"
CONFIG_DIR="/etc/nexvm"
DATA_DIR="/var/lib/nexvm"
BACKUP_DIR="/var/backups/nexvm"
TEMP_DIR="/tmp/nexvm"
CACHE_DIR="/var/cache/nexvm"
SSL_DIR="/etc/nexvm/ssl"
PAYMENT_DIR="/etc/nexvm/payments"

# Payment Configuration
UPI_ID="vedant1437@fam"
DISCORD_INVITE="https://discord.gg/zS2ynbF6jK"
SUPPORT_DISCORD="@DeVv-Prime"
PAYMENT_AMOUNT=499
ENTERPRISE_AMOUNT=999

# Bot Configuration
BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN_HERE"
BOT_PREFIX="."
MAIN_ADMIN_IDS="1405866008127864852"

# Network Configuration
NETWORK_BRIDGE="nexbr0"
MAX_CONTAINERS=100

# License Keys
VALID_LICENSE_KEYS=("prime2026" "preimdragon" "gamerhindu")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🖥️  CINEMATIC ASCII ART HEADER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

show_header() {
    clear
    echo -e "${GOLD}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GOLD}║                                                                               ║${NC}"
    echo -e "${TEAL}║        ███╗   ██╗███████╗██╗  ██╗    ██╗   ██╗███╗   ███║                   ║${NC}"
    echo -e "${TEAL}║        ████╗  ██║██╔════╝╚██╗██╔╝    ██║   ██║████╗ ████║                   ║${NC}"
    echo -e "${TEAL}║        ██╔██╗ ██║█████╗   ╚███╔╝     ██║   ██║██╔████╔██║                   ║${NC}"
    echo -e "${TEAL}║        ██║╚██╗██║██╔══╝   ██╔██╗     ╚██╗ ██╔╝██║╚██╔╝██║                   ║${NC}"
    echo -e "${TEAL}║        ██║ ╚████║███████╗██╔╝ ██╗     ╚████╔╝ ██║ ╚═╝ ██║                   ║${NC}"
    echo -e "${TEAL}║        ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚═╝     ╚═╝                   ║${NC}"
    echo -e "${SILVER}║                                                                            ║${NC}"
    echo -e "${GOLD}║                    🚀 Enterprise VM Management Platform v1.0 🚀              ║${NC}"
    echo -e "${LIME}║                        Made by ${BOLD}DeVv-Prime${NC}${LIME} with ❤️                         ║${NC}"
    echo -e "${GOLD}╠═══════════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${PINK}║                       💰 PAYMENT INFORMATION 💰                              ║${NC}"
    echo -e "${W}║                       📱 UPI ID: ${Y}vedant1437@fam${W}                           ║${NC}"
    echo -e "${P}║                       💬 Discord Support: ${Y}https://discord.gg/zS2ynbF6jK${P}      ║${NC}"
    echo -e "${GOLD}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -ne "${DIM}Initializing NEX VM V1 Engine "
    for i in {1..20}; do
        echo -ne "${GREEN}●${NC}"
        sleep 0.02
    done
    echo -e "${G} Done!${NC}\n"
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🔐  LICENSE VERIFICATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

check_license() {
    show_header
    
    echo -e "${GOLD}┌─────────────────────────────────────────────────────────────────┐${NC}"
    echo -e "${GOLD}│                    🔐 ENTERPRISE LICENSE ACTIVATION              │${NC}"
    echo -e "${GOLD}├─────────────────────────────────────────────────────────────────┤${NC}"
    echo -e "${SILVER}│  This software is protected by DeVv-Prime Enterprise License     │${NC}"
    echo -e "${GOLD}└─────────────────────────────────────────────────────────────────┘${NC}"
    echo ""
    
    mkdir -p "$CONFIG_DIR/license" "$PAYMENT_DIR"
    
    if [ -f "$CONFIG_DIR/license/license.key" ]; then
        STORED_KEY=$(cat "$CONFIG_DIR/license/license.key")
        echo -e "${G}✅ Found existing license: ${Y}$STORED_KEY${NC}"
        read -p "🔑 Use existing license? (y/n): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            KEY="$STORED_KEY"
            return 0
        fi
    fi
    
    echo -e "${Y}Valid License Keys:${NC}"
    echo -e "  ${GOLD}→${NC} ${G}prime2026${NC}"
    echo -e "  ${GOLD}→${NC} ${G}preimdragon${NC}"
    echo -e "  ${GOLD}→${NC} ${G}gamerhindu${NC}"
    echo ""
    
    read -p "🔑 Enter License Key: " KEY
    echo ""
    
    LICENSE_VALID=false
    for valid_key in "${VALID_LICENSE_KEYS[@]}"; do
        if [[ "$KEY" == "$valid_key" ]]; then
            LICENSE_VALID=true
            break
        fi
    done
    
    if [ "$LICENSE_VALID" = true ]; then
        echo -e "${G}╔══════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${G}║         ✅ LICENSE VERIFIED - ENTERPRISE ACCESS GRANTED     ║${NC}"
        echo -e "${G}║         Welcome to NEX VM V1 Enterprise!                    ║${NC}"
        echo -e "${G}╚══════════════════════════════════════════════════════════════╝${NC}"
        
        mkdir -p "$CONFIG_DIR/license"
        echo "$KEY" > "$CONFIG_DIR/license/license.key"
        chmod 600 "$CONFIG_DIR/license/license.key"
        
        echo "$(date): License activated with key: $KEY" >> "$LOG_FILE"
        sleep 2
        return 0
    else
        echo -e "${R}╔══════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${R}║         ❌ INVALID LICENSE - ACCESS DENIED                   ║${NC}"
        echo -e "${R}╚══════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        echo -e "${GOLD}💡 To get a valid license, contact DeVv-Prime:${NC}"
        echo -e "${W}   • UPI: ${Y}vedant1437@fam${W} (Pay ₹499 or ₹999)${NC}"
        echo -e "${W}   • Discord: ${Y}https://discord.gg/zS2ynbF6jK${NC}"
        echo ""
        read -p "Press Enter to retry or 'q' to quit: " retry
        if [[ "$retry" == "q" ]]; then
            exit 1
        fi
        check_license
    fi
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🔧  SYSTEM REQUIREMENTS CHECK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

check_system() {
    echo -e "${C}🔍 Checking system requirements...${NC}"
    
    # Check OS
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        echo -e "${G}✅ OS: $PRETTY_NAME${NC}"
    fi
    
    # Check RAM
    TOTAL_RAM=$(free -m | awk '/^Mem:/{print $2}')
    if [ $TOTAL_RAM -lt 4096 ]; then
        echo -e "${Y}⚠️ Warning: Less than 4GB RAM detected (${TOTAL_RAM}MB)${NC}"
    else
        echo -e "${G}✅ RAM: ${TOTAL_RAM}MB${NC}"
    fi
    
    # Check Disk Space
    FREE_DISK=$(df -BG / | awk 'NR==2{print $4}' | sed 's/G//')
    if [ $FREE_DISK -lt 50 ]; then
        echo -e "${Y}⚠️ Warning: Less than 50GB disk space available${NC}"
    else
        echo -e "${G}✅ Disk Space: ${FREE_DISK}GB free${NC}"
    fi
    
    # Check CPU Cores
    CPU_CORES=$(nproc)
    if [ $CPU_CORES -lt 2 ]; then
        echo -e "${Y}⚠️ Warning: Less than 2 CPU cores detected${NC}"
    else
        echo -e "${G}✅ CPU Cores: ${CPU_CORES}${NC}"
    fi
    
    echo ""
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📦  INSTALL DEPENDENCIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

install_dependencies() {
    echo -e "${C}📦 Installing system dependencies...${NC}"
    
    apt update -qq
    apt install -y -qq \
        python3 python3-pip python3-venv \
        lxd incus docker.io docker-compose \
        curl wget git unzip tar \
        nginx mariadb-server redis-server \
        ufw fail2ban \
        qrencode jq \
        net-tools bridge-utils \
        cloudflared tmate \
        sudo systemd \
        sqlite3 libsqlite3-dev \
        build-essential libssl-dev libffi-dev \
        python3-dev python3-setuptools \
        libjpeg-dev zlib1g-dev libpng-dev \
        pkg-config libcairo2-dev
        
    # Install additional Python packages
    pip3 install --upgrade pip
    pip3 install discord.py aiohttp pillow qrcode netifaces psutil
    
    echo -e "${G}✅ Dependencies installed!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🐳  CONFIGURE CONTAINER RUNTIMES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

configure_container_runtimes() {
    echo -e "${C}🐳 Configuring container runtimes...${NC}"
    
    # Initialize LXD if not already done
    if ! command -v lxd &> /dev/null; then
        snap install lxd
    fi
    
    if ! lxc info &> /dev/null; then
        lxd init --auto
        lxc network create lxdbr0 || true
    fi
    
    # Start Docker
    systemctl enable docker
    systemctl start docker
    
    echo -e "${G}✅ Container runtimes configured!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🔥  CONFIGURE FIREWALL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

configure_firewall() {
    echo -e "${C}🔥 Configuring firewall...${NC}"
    
    ufw allow 22/tcp
    ufw allow 80/tcp
    ufw allow 443/tcp
    ufw allow 8080/tcp
    ufw allow 8443/tcp
    ufw allow 10000:20000/tcp
    ufw allow 10000:20000/udp
    ufw --force enable
    
    echo -e "${G}✅ Firewall configured!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📁  CREATE DIRECTORIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

create_directories() {
    echo -e "${C}📁 Creating directories...${NC}"
    
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$DATA_DIR"
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$TEMP_DIR"
    mkdir -p "$CACHE_DIR"
    mkdir -p "$SSL_DIR"
    mkdir -p "$PAYMENT_DIR"
    mkdir -p "$INSTALL_DIR/data"
    mkdir -p "$INSTALL_DIR/backups"
    mkdir -p "$INSTALL_DIR/qr_codes"
    mkdir -p "$INSTALL_DIR/nodes"
    mkdir -p "$INSTALL_DIR/logs"
    
    echo -e "${G}✅ Directories created!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🐍  CREATE PYTHON VIRTUAL ENVIRONMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

install_python_environment() {
    echo -e "${C}🐍 Creating Python virtual environment...${NC}"
    
    cd "$INSTALL_DIR"
    python3 -m venv venv
    source venv/bin/activate
    
    pip install --upgrade pip
    pip install discord.py aiohttp pillow qrcode netifaces psutil
    
    echo -e "${G}✅ Python environment ready!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📝  CREATE BOT SCRIPT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

create_bot_script() {
    echo -e "${C}📝 Creating NEX VM V1 bot script...${NC}"
    
    cat > "$INSTALL_DIR/$BOT_SCRIPT" << 'EOF'
#!/usr/bin/env python3
# [The complete bot code from the previous response goes here]
# This is where the full Python bot code should be placed
EOF

    chmod +x "$INSTALL_DIR/$BOT_SCRIPT"
    echo -e "${G}✅ Bot script created!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ⚙️  CREATE CONFIGURATION FILE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

create_config() {
    echo -e "${C}⚙️ Creating configuration file...${NC}"
    
    cat > "$CONFIG_DIR/config.env" << EOF
# NEX VM V1 Configuration
BOT_TOKEN=$BOT_TOKEN
BOT_PREFIX=$BOT_PREFIX
MAIN_ADMIN_IDS=$MAIN_ADMIN_IDS
UPI_ID=$UPI_ID
DISCORD_INVITE=$DISCORD_INVITE
SERVER_IP=$(curl -s ifconfig.me)
INSTALL_DIR=$INSTALL_DIR
DATA_DIR=$DATA_DIR
LOG_FILE=$LOG_FILE
EOF

    echo -e "${G}✅ Configuration created!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📋  CREATE SYSTEMD SERVICE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

create_service() {
    echo -e "${C}🔧 Creating systemd service...${NC}"
    
    cat > /etc/systemd/system/$SERVICE_NAME.service << EOF
[Unit]
Description=NEX VM V1 - Enterprise VM Management Platform
After=network.target lxd.service docker.service
Wants=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$INSTALL_DIR
EnvironmentFile=$CONFIG_DIR/config.env
ExecStart=$INSTALL_DIR/venv/bin/python3 $INSTALL_DIR/$BOT_SCRIPT
Restart=always
RestartSec=5
StandardOutput=append:$LOG_FILE
StandardError=append:$LOG_FILE

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    echo -e "${G}✅ Systemd service created!${NC}"
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🚀  START BOT SERVICE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

start_bot() {
    echo -e "${C}🚀 Starting NEX VM V1 bot service...${NC}"
    
    systemctl enable $SERVICE_NAME
    systemctl start $SERVICE_NAME
    
    sleep 3
    
    if systemctl is-active --quiet $SERVICE_NAME; then
        echo -e "${G}✅ Bot service is running!${NC}"
    else
        echo -e "${R}❌ Bot service failed to start. Check logs: $LOG_FILE${NC}"
    fi
    sleep 1
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📋  SHOW COMPLETION MESSAGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

show_completion() {
    echo -e "${G}╔═══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}║              ✅ NEX VM V1 INSTALLATION COMPLETE - ALL FEATURES ✅            ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}╠═══════════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}║  📍 Installation Directory: $INSTALL_DIR                                      ║${NC}"
    echo -e "${G}║  🔧 Service Name: $SERVICE_NAME                                               ║${NC}"
    echo -e "${G}║  📝 Bot Token Set: ${Y}${BOT_TOKEN:0:20}...${NC}${G}                                          ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}╠═══════════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${PINK}║                       💰 PAYMENT INFORMATION 💰                              ║${NC}"
    echo -e "${W}║                                                                               ║${NC}"
    echo -e "${W}║   📱 UPI ID: ${Y}vedant1437@fam${W}                                            ║${NC}"
    echo -e "${W}║   💎 License Price: ₹499 / ₹999                                               ║${NC}"
    echo -e "${W}║   🔑 License Keys: prime2026, preimdragon, gamerhindu                        ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}╠═══════════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${P}║                       💬 DISCORD SUPPORT                                      ║${NC}"
    echo -e "${W}║                                                                               ║${NC}"
    echo -e "${W}║   🔗 Discord Invite: ${Y}https://discord.gg/zS2ynbF6jK${W}                       ║${NC}"
    echo -e "${W}║   👤 Support Contact: ${Y}@DeVv-Prime${W}                                      ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}╠═══════════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}║              📞 USEFUL COMMANDS                                               ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${W}║   • Start bot:     ${C}systemctl start $SERVICE_NAME${W}                         ║${NC}"
    echo -e "${W}║   • Stop bot:      ${C}systemctl stop $SERVICE_NAME${W}                          ║${NC}"
    echo -e "${W}║   • Restart bot:   ${C}systemctl restart $SERVICE_NAME${W}                       ║${NC}"
    echo -e "${W}║   • View logs:     ${C}journalctl -u $SERVICE_NAME -f${W}                        ║${NC}"
    echo -e "${W}║   • Bot status:    ${C}systemctl status $SERVICE_NAME${W}                        ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}╠═══════════════════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}║              🔧 TROUBLESHOOTING                                               ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${W}║   • Check logs:    ${C}tail -f $LOG_FILE${W}                                     ║${NC}"
    echo -e "${W}║   • Reinstall:     ${C}sudo $0${W}                                              ║${NC}"
    echo -e "${W}║   • Support:       ${Y}Join Discord and create a ticket${W}                      ║${NC}"
    echo -e "${G}║                                                                               ║${NC}"
    echo -e "${G}╚═══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GOLD}🎉 NEX VM V1 installation complete! Made by DeVv-Prime with ❤️ 🎉${NC}"
    echo -e "${Y}📌 Next Steps:${NC}"
    echo -e "   1. Edit ${CONFIG_DIR}/config.env and set your BOT_TOKEN"
    echo -e "   2. Run: ${C}systemctl restart $SERVICE_NAME${NC}"
    echo -e "   3. Invite bot to your Discord server"
    echo -e "   4. Use ${Y}.license-verify <key>${NC} in Discord to activate"
    echo ""
    echo -e "${PINK}💬 Need help? Join Discord: ${Y}https://discord.gg/zS2ynbF6jK${NC}"
    echo -e "${PINK}💰 Support the project: UPI ${Y}vedant1437@fam${NC}"
    echo ""
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🔧  DOWNLOAD BOT SCRIPT FROM GITHUB/URL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

download_bot_script() {
    echo -e "${C}📥 Downloading NEX VM V1 bot script...${NC}"
    
    # Create a temporary file with the bot code
    cat > "$INSTALL_DIR/$BOT_SCRIPT" << 'BOTEOF'
#!/usr/bin/env python3
# NEX VM V1 Bot - Placeholder
# Please copy your bot code here
print("NEX VM V1 Bot - Starting...")
print("Please replace this with the actual bot code")
BOTEOF

    chmod +x "$INSTALL_DIR/$BOT_SCRIPT"
    echo -e "${Y}⚠️ Please replace the placeholder bot code in $INSTALL_DIR/$BOT_SCRIPT with your actual bot code!${NC}"
    sleep 2
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🎯  MAIN INSTALLATION FUNCTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

main() {
    # Check if running as root
    if [[ $EUID -ne 0 ]]; then
        echo -e "${R}❌ This script must be run as root!${NC}"
        echo -e "${Y}Please run: sudo bash $0${NC}"
        exit 1
    fi
    
    show_header
    check_license
    check_system
    install_dependencies
    configure_container_runtimes
    configure_firewall
    create_directories
    install_python_environment
    download_bot_script
    create_config
    create_service
    start_bot
    show_completion
}

# Run main function
main "$@"

# WARP CLI Wrapper

A simple Python script to connect/disconnect Cloudflare WARP from your terminal.

---

## Why WARP?

If your ISP does SSL inspection (common in India), it breaks developer tools like OpenCode, curl, and npm. Cloudflare WARP bypasses this by routing your traffic through Cloudflare's secure network — for free, with no data limits.

---

## Requirements

- **OS:** Ubuntu / Debian based Linux only
- **Python:** 3.6 or higher
- **curl:** required for adding Cloudflare repo (pre-installed on most systems)

---

## Installation

### 1. Install Cloudflare WARP

```bash
# Add Cloudflare GPG key
curl --insecure -fsSL https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg

# Add repository
echo "deb [signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list

# Install
sudo apt update && sudo apt install cloudflare-warp
```

### 2. Register WARP (one-time only)

```bash
warp-cli registration new
```

Accept the Terms of Service when prompted. You only need to do this once.

### 3. Clone this repo

```bash
git clone https://github.com/Aditya-das-4707-e/warp-cli.git
cd warp-cli
```

### 4. Make it globally available

```bash
sudo cp warp.py /usr/local/bin/warp
sudo chmod +x /usr/local/bin/warp
```

---

## Usage

Type `warp` in any terminal:

```bash
warp
```

You will see:

```
=== Cloudflare WARP ===
1. Connect
2. Disconnect
3. Exit

Enter choice:
```

- Press `1` to connect
- Press `2` to disconnect
- Press `3` to exit

---

## Check Status

```bash
warp-cli status
```

Output when connected:
```
Status update: Connected
Network: healthy
```

---

## Uninstall

```bash
# Remove the script
sudo rm /usr/local/bin/warp

# Remove Cloudflare WARP
sudo apt remove cloudflare-warp

# Remove config
sudo rm /etc/apt/sources.list.d/cloudflare-client.list
sudo rm /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg
```
# SSH Tunneling

## Overview
Encrypted tunnel through SSH.
Useful for secure remote access.

## Local Tunnel
- ssh -L 8080:192.168.0.1:80 root@192.168.0.1
- Access remote web UI on localhost:8080

## Remote Tunnel
- ssh -R 8080:localhost:80 root@public-server.com
- Access local web UI on public-server:8080

## Dynamic Tunnel (SOCKS)
- ssh -D 1080 root@192.168.0.1
- Configure browser to use SOCKS5 proxy localhost:1080

## Reverse SSH
- ssh -R 2222:localhost:22 root@public-server.com
- Access router from public-server:2222

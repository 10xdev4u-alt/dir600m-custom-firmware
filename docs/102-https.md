# HTTPS Setup

## Overview
Secure HTTP for LuCI web interface.
Uses uhttpd with SSL.

## Setup
1. Install uhttpd-mod-tls:
```
opkg install uhttpd-mod-tls
```
2. Generate certificate:
```
openssl req -x509 -nodes -newkey rsa:2048 \
  -keyout /etc/uhttpd.key \
  -out /etc/uhttpd.crt \
  -days 3650 -subj "/CN=DIR-600M"
```
3. Configure /etc/config/uhttpd:
```
option cert '/etc/uhttpd.crt'
option key '/etc/uhttpd.key'
```
4. Restart: /etc/init.d/uhttpd restart

## Access
- https://192.168.0.1 (accept self-signed cert)

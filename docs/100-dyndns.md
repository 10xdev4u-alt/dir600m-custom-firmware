# Dynamic DNS

## Overview
DNS service for routers with changing public IP.
Useful for remote access.

## Providers
- No-IP (free)
- DynDNS (paid)
- DuckDNS (free)
- afraid.org (free)

## OpenWrt Setup
1. Install ddns-scripts:
```
opkg install ddns-scripts
```
2. Configure /etc/config/ddns:
```
config service 'myddns'
    option service_name 'noip'
    option username 'user'
    option password 'pass'
    option domain 'myrouter.no-ip.com'
    option ip_source 'network'
    option ip_network 'wan'
    option enabled '1'
```
3. Start: /etc/init.d/ddns start

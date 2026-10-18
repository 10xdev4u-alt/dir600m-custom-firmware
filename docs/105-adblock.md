# Ad Blocking

## Overview
Block ads at the DNS level.
Saves bandwidth and improves privacy.

## Option 1: Simple DNS
- /etc/config/dhcp:
```
config dnsmasq
    option serversfile '/etc/dnsmasq.blocklist'
```
- Download StevenBlack hosts:
```
wget https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts -O /etc/dnsmasq.blocklist
/etc/init.d/dnsmasq restart
```

## Option 2: Pi-hole
- Install pi-hole-FTL (lightweight)
- Configure upstream DNS
- Web UI for management

## Option 3: AdGuard Home
- Modern alternative to Pi-hole
- DNS-over-HTTPS support
- Web UI included

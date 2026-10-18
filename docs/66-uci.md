# UCI (Unified Configuration Interface)

## Overview
OpenWrt's unified configuration system.
Replaces D-Link's proprietary config format.

## Commands
- uci show: display configuration
- uci get: get a value
- uci set: set a value
- uci add: add a section
- uci delete: delete a section
- uci commit: commit changes
- uci revert: revert changes

## Example
```
uci set network.lan.ipaddr='192.168.1.1'
uci commit network
/etc/init.d/network restart
```

## Files
- /etc/config/network
- /etc/config/wireless
- /etc/config/dhcp
- /etc/config/firewall
- /etc/config/system

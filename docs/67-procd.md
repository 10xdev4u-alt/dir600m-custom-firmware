# procd (Process Daemon)

## Overview
OpenWrt's init system and process supervisor.
Replaces D-Link's proprietary init.

## Features
- Service management (/etc/init.d/)
- Process supervision (respawn on crash)
- Hotplug handling
- Boot/shutdown scripts

## Service Files
- /etc/init.d/network
- /etc/init.d/firewall
- /etc/init.d/dnsmasq
- /etc/init.d/hostapd
- /etc/init.d/system

## Commands
- /etc/init.d/network start
- /etc/init.d/network stop
- /etc/init.d/network restart
- /etc/init.d/network enable
- /etc/init.d/network disable

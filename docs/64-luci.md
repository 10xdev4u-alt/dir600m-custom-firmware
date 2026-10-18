# LuCI Web Interface

## Overview
Lua-based web interface for OpenWrt.
Replacement for D-Link's GoAhead web server.

## Features
- Modern web UI
- AJAX-based (no page reloads)
- Themes (bootstrap, material)
- i18n support
- REST API (ubus)

## Access
- Default: http://192.168.1.1
- Default user: root
- Default password: (none, set on first login)

## Configuration
- /etc/config/luci
- /usr/lib/lua/luci/

## Apps
- luci-app-diag-devinfo: System info
- luci-app-qos: Quality of Service
- luci-app-wol: Wake-on-LAN
- luci-app-p910nd: Printer server

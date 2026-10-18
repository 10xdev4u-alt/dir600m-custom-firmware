# Firmware Upgrade (sysupgrade)

## Overview
OpenWrt's built-in firmware upgrade tool.
Preserves configuration by default.

## Commands
- sysupgrade /tmp/firmware.bin: upgrade keeping config
- sysupgrade -n /tmp/firmware.bin: upgrade wiping config
- sysupgrade -b /tmp/backup.tar.gz: backup first
- sysupgrade -r /tmp/firmware.bin: revert to previous

## Backup
- sysupgrade -b /tmp/backup.tar.gz
- Creates /etc/ backup
- Includes network, wireless, firewall config

## Revert
- sysupgrade -r /tmp/firmware.bin
- Reverts to previous firmware
- Requires dual partition or TFTP recovery

## Safety
- Always verify MD5 before upgrade
- Backup config first
- Don't power off during upgrade

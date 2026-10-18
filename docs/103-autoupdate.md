# Automatic Updates

## Overview
Keep OpenWrt firmware and packages up to date.
Manual or automatic.

## Manual Update
1. Check for updates:
```
opkg update
opkg list-upgradable
```
2. Upgrade:
```
opkg upgrade <package>
```

## Firmware Update
- Download new firmware
- sysupgrade /tmp/firmware.bin
- Or use LuCI: System -> Backup/Flash

## Auto-Update Script
- /etc/init.d/auto-update
- Runs opkg update + upgrade weekly
- Logs to /var/log/update.log

## Caution
- Always backup before major updates
- Test on spare router first
- Don't auto-update firmware (only packages)

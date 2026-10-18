# ubus (OpenWrt RPC System)

## Overview
OpenWrt's RPC system for inter-process communication.
Used by LuCI and other OpenWrt components.

## Commands
- ubus list: list available objects
- ubus call: call a method
- ubus listen: listen for events
- ubus send: send an event

## Example
```
ubus call system board
ubus call network.interface dump
```

## Objects
- system: system info, upgrade
- network: interfaces, wireless
- service: service management

## Integration
- LuCI uses ubus for all operations
- Replaces UCI direct file access
- More secure than file-based config

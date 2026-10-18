# Z-Wave Support

## Overview
Z-Wave is a wireless protocol for home automation.
Requires USB Z-Wave controller.

## Hardware
- USB Z-Wave controller (Aeotec Z-Stick)
- kmod-usb-serial for serial communication

## Software
- Z-Wave JS:
```
opkg install node node-npm
npm install -g zwave-js
```
- Configure /opt/zwave/config.json
- Start: zwave-js &

## Integration
- MQTT for Home Assistant
- HTTP API for custom scripts
- Web UI for device management

## Notes
- USB controller required
- Limited by 390 MHz CPU
- External server recommended

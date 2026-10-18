# Zigbee Support

## Overview
Zigbee is a low-power wireless protocol for IoT devices.
Requires USB coordinator.

## Hardware
- USB Zigbee coordinator (CC2531, CC2652)
- kmod-usb-serial for serial communication

## Software
- zigbee2mqtt:
```
opkg install node node-npm
npm install -g zigbee2mqtt
```
- Configure /opt/zigbee2mqtt/configuration.yaml
- Start: zigbee2mqtt &

## Integration
- MQTT for Home Assistant
- HTTP API for custom scripts
- Web UI for device management

## Notes
- USB coordinator required
- Limited by 390 MHz CPU
- External server recommended for heavy use

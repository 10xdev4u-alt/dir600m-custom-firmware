# Bluetooth Support

## Overview
Bluetooth for IoT devices, audio, and peripherals.
Requires USB Bluetooth adapter.

## Hardware
- USB Bluetooth 4.0+ adapter
- kmod-bluetooth for kernel support

## Software
- bluez-utils:
```
opkg install bluez-utils
hciconfig hci0 up
bluetoothctl
```

## Usage
- Pair devices: scan, pair, trust, connect
- Audio: pulseaudio + bluez
- BLE: gatttool, bluepy

## Notes
- USB adapter required (no built-in BT)
- Limited by 390 MHz CPU
- BLE better than classic BT for IoT

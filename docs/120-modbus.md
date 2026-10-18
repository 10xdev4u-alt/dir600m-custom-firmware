# Modbus Protocol

## Overview
Industrial communication protocol.
RS-485 or TCP.

## Hardware
- RS-485 adapter (USB or GPIO)
- Modbus RTU (serial) or Modbus TCP (Ethernet)
- Sensors, PLCs, inverters

## Software
- modbus-cli:
```
opkg install modbus-cli
modbus -m rtu -a 1 -b 9600 -p none /dev/ttyUSB0
```

## Registers
- Coils (0x): read/write bits
- Discrete inputs (1x): read bits
- Holding registers (3x): read/write 16-bit
- Input registers (4x): read 16-bit

## Integration
- Home Assistant via MQTT
- HTTP API for custom scripts
- Industrial SCADA systems

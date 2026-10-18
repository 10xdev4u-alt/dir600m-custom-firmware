# UART Access Guide

## Location
4-pin header on PCB (usually near the SoC)

## Pinout (typical)
- Pin 1: VCC (3.3V)
- Pin 2: TX
- Pin 3: RX
- Pin 4: GND

## Settings
- Baud: 115200
- Data: 8 bits
- Parity: None
- Stop: 1 bit
- Flow: None

## Usage
Connect USB-to-TTL adapter (3.3V). Open minicom/screen:
screen /dev/ttyUSB0 115200

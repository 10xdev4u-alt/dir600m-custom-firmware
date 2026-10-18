# UART Pinout for DIR-600M C1

## Header Location
4-pin header near the SoC (usually J1 or J2)

## Pinout (typical)
| Pin | Function |
|-----|----------|
| 1   | VCC 3.3V |
| 2   | TX       |
| 3   | RX       |
| 4   | GND      |

## Settings
- Baud: 115200
- Data: 8 bits
- Parity: None
- Stop: 1 bit
- Flow: None

## Connection
Use USB-to-TTL adapter (3.3V logic, NOT 5V):
- Adapter TX -> Router RX
- Adapter RX -> Router TX
- Adapter GND -> Router GND
- Do NOT connect VCC (router is powered)

## Software
- Linux: screen /dev/ttyUSB0 115200
- Windows: PuTTY

# Serial Support on DIR-600M

## Hardware UART
- 2x UART controllers
- UART0: debug console (115200)
- UART1: available for use

## Debug Console
- Pin header on PCB
- 115200 baud, 8N1
- Shows boot messages
- Recovery mode interface

## USB-to-TTL
- Connect TX/RX/GND to header
- 3.3V logic (NOT 5V)
- Use screen/minicom/PuTTY

## Software Serial
- kmod-usb-serial: USB serial adapters
- kmod-usb-serial-ftdi: FTDI chips
- kmod-usb-serial-cp210x: CP210x chips
- kmod-usb-serial-option: 3G modems

## GPS/Modems
- /dev/ttyUSB0 for 3G modems
- /dev/ttyUSB1 for GPS
- kmod-usb-serial-option for Huawei

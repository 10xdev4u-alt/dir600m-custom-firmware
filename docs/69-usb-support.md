# USB Support on DIR-600M

## Hardware
- USB 2.0 host controller (OHCI/UHCI)
- Single USB port (if present on PCB)

## Supported Devices
- USB storage (flash drives, HDD)
- USB serial (modems, adapters)
- USB printers
- USB 3G/4G modems

## Configuration
- kmod-usb-ohci: OHCI support
- kmod-usb-uhci: UHCI support
- kmod-usb2: EHCI (USB 2.0)
- kmod-usb-storage: mass storage
- kmod-usb-serial: serial adapters
- kmod-usb-serial-option: option-based modems

## Power
- USB power may be limited
- Use powered hub for HDDs
- Check dmesg for power warnings

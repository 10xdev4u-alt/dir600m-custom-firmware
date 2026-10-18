# Network Printer Support

## Overview
Share USB printer on the network.
luci-app-p910nd provides this.

## Setup
1. Connect printer to USB
2. Install luci-app-p910nd
3. Configure /etc/config/p910nd:
```
config p910nd
    option device '/dev/usb/lp0'
    option port '9100'
    option enabled '1'
    option bidirectional '1'
```
4. Start service: /etc/init.d/p910nd start
5. Add printer on clients via port 9100

## Notes
- Printer must be compatible
- Check dmesg for detection
- Use powered hub if needed

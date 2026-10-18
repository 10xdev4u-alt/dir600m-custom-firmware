# Watchdog Timer

## Overview
Hardware watchdog that resets the system on hang.
Available on RTL8196C.

## Kernel Module
- kmod-rtl8196c-wdt: watchdog driver
- /dev/watchdog: watchdog device

## Configuration
/etc/init.d/watchdog:
```
#!/bin/sh /etc/rc.common
START=99
start() {
    echo 30 > /dev/watchdog
}
stop() {
    echo V > /dev/watchdog
}
```

## Usage
- echo 1 > /dev/watchdog: pet the watchdog
- If not pet within timeout, system resets
- Typical timeout: 30-60 seconds

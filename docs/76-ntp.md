# NTP (Network Time Protocol)

## Overview
Time synchronization service.
Ensures accurate system time.

## /etc/config/system
```
config system
    option timezone 'IST-5:30'
    option hostname 'DIR-600M'
    option timeserver 'pool.ntp.org'
```

## Client
- ntpclient: lightweight NTP client
- ntpd: full NTP server
- busybox ntpd: minimal NTP

## Usage
- Check date: date
- Sync manually: ntpclient -s -h pool.ntp.org
- Log: logread | grep ntp

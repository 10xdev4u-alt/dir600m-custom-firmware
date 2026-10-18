# Samba File Sharing

## Overview
SMB/CIFS file sharing for Windows clients.
Heavy for 390 MHz CPU.

## Setup
1. Install samba36-server:
```
opkg install samba36-server
```
2. Configure /etc/samba/smb.conf:
```
[global]
    workgroup = WORKGROUP
    security = user

[share]
    path = /mnt/usb
    read only = no
    guest ok = yes
```
3. Start: /etc/init.d/samba start

## Alternative
- lighter: lighttpd + webdav
- Use NFS for Linux clients
- FTP for simple transfers

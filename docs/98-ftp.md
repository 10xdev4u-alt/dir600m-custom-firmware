# FTP Server

## Overview
File Transfer Protocol server.
Lightweight alternative to Samba.

## Setup
1. Install vsftpd or busybox-ftpd:
```
opkg install vsftpd
```
2. Configure /etc/vsftpd.conf:
```
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_root=/mnt/usb
```
3. Start: /etc/init.d/vsftpd start

## Clients
- Windows: File Explorer -> ftp://192.168.0.1
- Linux: ftp 192.168.0.1 or lftp
- macOS: Finder -> Go -> Connect to Server

## Notes
- Use SFTP (SSH) for security
- FTP is unencrypted

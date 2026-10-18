# WebDAV Server

## Overview
Web-based file sharing via HTTP.
Lightweight, good for remote access.

## Setup
1. Install lighttpd + webdav:
```
opkg install lighttpd lighttpd-mod-webdav
```
2. Configure /etc/lighttpd/lighttpd.conf:
```
server.modules += ( "mod_webdav" )
$HTTP["url"] =~ "^/webdav" {
    webdav.activate = "enable"
    webdav.sqlite3-db = "/etc/lighttpd/webdav.db"
}
```
3. Start: /etc/init.d/lighttpd start

## Access
- Browser: http://192.168.0.1/webdav
- Windows: Map network drive
- macOS: Finder -> Connect to Server

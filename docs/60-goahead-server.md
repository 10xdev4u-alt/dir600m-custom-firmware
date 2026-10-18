# GoAhead Web Server

## Overview
Embedded web server used by D-Link in DIR-600M.
Serves the web management interface.

## Features
- CGI support
- SSL/TLS (optional)
- Basic authentication
- ASP-like templates

## Pages in DIR-600M
- telnet.htm: Telnet config
- userconfig: User management
- admin: Admin settings
- wan_collision: IP conflict notice
- Various JS validators

## Security Issues
- No output encoding (XSS)
- Weak session management
- No CSRF protection (mostly)
- Default credentials

## Replacement
OpenWrt uses uhttpd + LuCI instead.

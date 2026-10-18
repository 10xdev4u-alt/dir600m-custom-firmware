# Security Hardening for OpenWrt

## SSH
- Disable password auth (use keys only)
- Change default port
- Disable root login
- Use dropbear (lighter than openssl)

## Firewall
- Drop all incoming on WAN
- Enable SYN flood protection
- Block private IPs on WAN
- Enable logging for dropped packets

## Services
- Disable unused services
- Bind services to LAN only
- Use HTTPS for LuCI (if possible)
- Regular updates

## Wireless
- WPA2-PSK minimum
- Strong password
- Disable WPS
- Regular password rotation

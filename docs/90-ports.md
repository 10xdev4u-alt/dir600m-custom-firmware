# Port Usage

## Common Ports
- 22: SSH (dropbear)
- 80: HTTP (uhttpd)
- 443: HTTPS (if configured)
- 53: DNS (dnsmasq)
- 67/68: DHCP (dnsmasq)

## Custom Ports
- 23: Telnet (if enabled)
- 8080: Alt HTTP
- 161: SNMP (if enabled)
- 123: NTP (ntpd)

## Firewall
- Block unused ports
- Forward if needed
- Log dropped packets

## Scanning
- nmap -p- 192.168.0.1
- netstat -tlnp
- ss -tlnp

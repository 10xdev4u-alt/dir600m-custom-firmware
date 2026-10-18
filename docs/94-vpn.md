# VPN Support

## OpenWrt VPN Options
- OpenVPN: full-featured, heavy
- WireGuard: modern, lightweight
- IPsec: built-in, complex
- PPTP: legacy, insecure

## WireGuard (Recommended)
```
opkg install wireguard-tools
wg genkey > /etc/wireguard/privatekey
wg pubkey < /etc/wireguard/privatekey > /etc/wireguard/publickey
```

## OpenVPN
```
opkg install openvpn-openssl
# Place config in /etc/openvpn/client.conf
/etc/init.d/openvpn start
```

## Performance
- 390 MHz CPU limits throughput
- WireGuard fastest on this hardware
- Expect ~20-30 Mbps

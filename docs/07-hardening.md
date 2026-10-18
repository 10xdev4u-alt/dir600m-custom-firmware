# Hardening Stock DIR-600M Firmware

1. Disable remote management (Administration -> Remote Management -> Off)
2. Disable Telnet (Telnet.htm -> form2Telnet.cgi -> disable daemon)
3. Change default admin password (max 30 chars)
4. Set SSID to non-script string (CVE-2018-6936 vector)
5. Don't expose web UI to WAN
6. Upgrade to v3.08 (latest patched build)

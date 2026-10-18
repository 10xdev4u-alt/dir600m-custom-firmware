# Security Assessment

## Vulnerabilities in v3.01
- CVE-2018-6936: Stored XSS (SSID, username)
- CVE-2017-10676: XSS in form2userconfig.cgi
- CVE-2017-5874: CSRF

## Mitigations
- Upgrade to v3.08
- Disable remote management
- Disable Telnet
- Sanitize inputs

## Attack Surface
- Web management interface (GoAhead/VWS)
- Telnet daemon (if enabled)
- CGI handlers (form2*.cgi)
- No HTTPS by default

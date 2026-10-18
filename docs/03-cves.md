# Known CVEs for DIR-600M C1

## CVE-2018-6936 (CVSS 5.4 Medium)
- Stored XSS via SSID or user account name
- Affected: C1 firmware 3.01
- PoC: exploit-db 44219, 45343
- Patched in: v3.05ENB01_beta_20170306

## CVE-2017-10676
- XSS in form2userconfig.cgi
- Affected: before C1_v3.05ENB01_beta_20170306

## CVE-2017-5874
- CSRF on Rev Cx
- Affected: before v3.05ENB01_beta_20170306

## Mitigation
- Upgrade to v3.08 (latest)
- Disable remote management
- Disable Telnet
- Sanitize SSID and usernames

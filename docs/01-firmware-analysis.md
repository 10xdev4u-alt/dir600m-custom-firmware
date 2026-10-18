# D-Link DIR-600M C1 — Firmware 3.01 Deep Dive

## Source
- File: `~/Downloads/DIR-600M C1.img` (1,240,979 bytes, md5 23c4f5013c8322d3db25884494e81586)
- Downloaded via D-Link India firmware portal (product "DIR-600M C1", FW3.08B01 listed; 3.01 is the vulnerable baseline referenced by CVE-2018-6936).
- HW: DIR-600M C1, Indian region firmware ("engineered for Indian products only").

## Firmware container format
Header (64 bytes):
```
44 49 52 36 30 30 4d   "DIR600M"
a0 00 00 03 80 00 00 00 00
12 ef 4c 80             (size-ish)
2b 81 a8 95 a8 05
"Wed May 29 17:36:03 2019\0"
"router.img\0"
```
Body: 28 consecutive LZMA (alone format) streams, each ~32 KB, magic `5d 00 00 80 00` + 8-byte uncompressed size. Total decompressed: ~893 KB.

## Extracted content
- Web UI pages for GoAhead/VWS embedded server: telnet.htm, userconfig, wan_collision, admin, etc.
- Embedded JS validators, CSRF token injection (`SendKeyCSRF`).
- Telnet configuration page present (form2Telnet.cgi) — Telnet daemon toggle exposed in web UI.
- Admin user management page: username/password fields, "Can't delete admin" guard, max 30 chars.

## Known CVEs for DIR-600M C1 3.01
- CVE-2018-6936 (CVSS 5.4 Medium): Stored XSS via SSID or user account name. Public PoC (exploit-db 44219, 45343). Affects web management interface; requires ability to set SSID / create user accounts.
- CVE-2017-10676: XSS in form2userconfig.cgi (versions before C1_v3.05ENB01_beta_20170306).
- CVE-2017-5874: CSRF on Rev Cx before v3.05ENB01_beta_20170306.
- CVE-2017-10676/CVE-2017-5874 patched in v3.05ENB01_beta.

## Attack surface (from firmware)
1. Web management interface (GoAhead) — primary XSS/CSRF target.
2. Telnet daemon toggle — if enabled, remote shell access.
3. CGI handlers: form2Telnet.cgi, form2userconfig.cgi, diagnostic ping (RuntimeDiagnosticPing class on similar models).
4. No HTTPS by default; admin password max 36 chars, special chars partially filtered.

## REA usage
- Extracted with custom Python LZMA carver (no binwalk available).
- All 28 streams saved as stream_0..27.bin in /tmp/dir600m-fw.

## Files
- firmware.img, all_streams.bin, stream_*.bin, rootfs.bin (first stream)

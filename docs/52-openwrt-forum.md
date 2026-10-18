# OpenWrt Forum Discussions Summary

## Key Threads
1. "Realtek SoC support in OpenWrt" (2013) - roman's original work
2. "Building OpenWRT for RTL8196C" (2017) - mk24's build attempts
3. "Can RTL8196C be incorporated into the LEDE?" (2015)
4. "Any plans for Realtek SOC support?" (2018)

## Key Findings
- Lexra core is NOT supported by standard gcc
- Requires hacked gcc 4.5-linaro + binutils 2.21.1
- No upstream support, likely never will be
- WiFi drivers are the biggest challenge
- 4MB/32MB is below modern OpenWrt minimums

## Community Verdict
"Realtek is a dead end for OpenWrt" - Borromini (2019)
"DO NOT BUY DEVICES WITH 4MB FLASH / 32MB RAM" - OpenWrt wiki

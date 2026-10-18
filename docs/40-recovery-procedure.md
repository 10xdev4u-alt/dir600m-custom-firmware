# Full Recovery Procedure

## If Router Won't Boot

1. **Enter Recovery Mode**
   - Power off
   - Hold reset button
   - Power on, keep holding 10-15s
   - Router at 192.168.1.6

2. **Prepare TFTP Server**
   - PC IP: 192.168.1.2/24
   - Place firmware files in TFTP root
   - Start TFTP server

3. **Flash Stock Firmware**
   - Upload DIR-600M_C1.img via TFTP
   - Wait for flash to complete
   - Router reboots

4. **If Still Broken**
   - Try UART connection
   - Check for hardware damage
   - Consider JTAG (if available)

## Prevention
- Always keep backup of original firmware
- Verify MD5 before flashing
- Don't power off during flash

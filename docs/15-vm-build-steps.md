# VM Build Steps (Detailed)

1. Install Ubuntu 14.04 in VM
2. apt-get install build-essential libncurses5-dev zlib1g-dev gawk git subversion python unzip wget
3. git clone https://github.com/utessel/edimax.git
4. cd edimax
5. make menuconfig -> select realtek rtl8196c, profile nprove
6. make defconfig
7. make -j4 (expect 1-2 hours)
8. Output: bin/realtek/openwrt-realtek-rtl8196c-nprove-*.bin
9. TFTP flash to router

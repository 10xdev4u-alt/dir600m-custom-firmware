# VM Setup for OpenWrt Build

## Recommended: Ubuntu 14.04 LTS
- Download ISO from old-releases.ubuntu.com
- Install in VirtualBox/VMware
- 4GB RAM, 40GB disk

## Packages
sudo apt-get install build-essential libncurses5-dev zlib1g-dev gawk git subversion python unzip wget

## Build
git clone https://github.com/utessel/edimax.git
cd edimax
make defconfig
make -j4

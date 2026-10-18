# Device Tree (DTS)

## Overview
Hardware description for the kernel.
Tells kernel about SoC, memory, peripherals.

## DIR-600M DTS
```
/dts-v1/;
/include/ "rtl8196c.dtsi"

/ {
    model = "D-Link DIR-600M";
    compatible = "dlink,dir-600m", "realtek,rtl8196c";

    memory {
        reg = <0x0 0x2000000>;  /* 32 MB */
    };

    chosen {
        bootargs = "console=ttyS0,115200 root=/dev/mtdblock4";
    };
};
```

## Compilation
- dtc -O dtb -o dir-600m.dtb dir-600m.dts
- dtc -I dtb -O dts dir-600m.dtb (decompile)

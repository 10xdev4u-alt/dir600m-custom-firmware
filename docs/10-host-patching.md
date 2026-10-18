# Host Tool Patching for Modern glibc

## Patches applied (on hkwi/openwrt-realtek)
1. m4 c-stack.c: SIGSTKSZ glibc 2.38 form
2. m4 freadahead.c: _IO_IN_BACKUP removal, __GLIBC__ guard
3. pkg-config glib: -std=gnu89 for inline semantics
4. bison fseterr.c: _IO_ERR_SEEN glibc guard
5. mklibs elf.hpp/elf_data.hpp/elf.cpp: remove throw() specs
6. rules.mk: HOST_CFLAGS += -fcommon -std=gnu89
7. host-build.mk: add CXXFLAGS

## Remaining blockers
- cmake C++17 dynamic exception specs
- e2fsprogs __s64 type conflict
- gdb wcwidth implicit declaration
- mkimage asm_types.c
- flex, scons, etc.

## Verdict
Multi-day porting effort. Use old VM instead.

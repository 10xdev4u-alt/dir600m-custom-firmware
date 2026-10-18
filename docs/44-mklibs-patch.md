# mklibs Patch Details

## Problem
mklibs-0.1.35 uses C++03 dynamic exception specifications (`throw()`) which are:
- Deprecated in C++11
- Removed in C++17

GCC 11+ defaults to C++17, causing compilation errors.

## Fix
Removed all `throw(...)` specifications from:
- src/mklibs-readelf/elf.hpp
- src/mklibs-readelf/elf_data.hpp
- src/mklibs-readelf/elf.cpp

Used Python script to strip `throw(...)` with nested parens.

## Result
mklibs compiles with modern GCC in C++17 mode.

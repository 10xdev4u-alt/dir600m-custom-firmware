# cmake Patch Details (Not Fixed)

## Problem
cmake-2.8.10.2's bundled cmsys uses C++03 features:
- dynamic exception specifications `throw()`
- auto_ptr (removed in C++17)
- bind1st/bind2nd

GCC 11+ defaults to C++17, causing errors in:
- Source/cmsys/auto_ptr.hxx
- Source/cmsys/hashtable.hxx
- Source/kwsys/hasquetable.hxx.in

## Would Need
1. Add `-std=gnu++14` to HOST_CXXFLAGS (already done in rules.mk)
2. May still need source patches for auto_ptr/bind1st

## Workaround
Use system cmake instead:
- Ubuntu 20.04: cmake 3.16 (works)
- Arch: cmake 4.4.2 (works)
- Just symlink to staging_dir/host/bin/cmake

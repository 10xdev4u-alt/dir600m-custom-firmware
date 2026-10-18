# Re-Packer Usage

## Extract
python3 repack.py extract firmware.img streams/

## Modify
Edit any stream_XX.bin file (e.g., patch telnet.htm to remove toggle)

## Rebuild
python3 repack.py build streams/ new.img

## Verify
python3 repack.py extract new.img streams2/
# compare streams/ and streams2/ - should be identical

# Audio/Speaker Support

## Overview
Connect USB audio devices for announcements.
Text-to-speech and audio playback.

## Hardware
- USB audio adapter (3.5mm jack)
- kmod-usb-audio for audio support

## Software
- alsa-utils:
```
opkg install alsa-utils
aplay /usr/share/sounds/alert.wav
```

## TTS
- espeak:
```
opkg install espeak
espeak "Temperature is 25 degrees" -w /tmp/tts.wav
aplay /tmp/tts.wav
```

## Integration
- MQTT for Home Assistant announcements
- HTTP API for custom scripts
- Scheduled announcements via cron

## Notes
- USB audio adapter required
- 390 MHz CPU limits TTS quality
- Pre-generate common phrases

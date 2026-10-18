# IP Camera Support

## Overview
Connect USB IP cameras for surveillance.
Stream video over HTTP/RTSP.

## Hardware
- USB IP camera (or USB + IP camera module)
- kmod-usb-video for video support

## Software
- mjpg-streamer:
```
opkg install mjpg-streamer
mjpg_streamer -i "input_uvc.so" -o "output_http.so -p 8080"
```

## Usage
- Stream: http://192.168.0.1:8080/?action=stream
- Snapshot: http://192.168.0.1:8080/?action=snapshot
- Motion detection: motion package

## Notes
- USB camera required
- 390 MHz CPU limits resolution
- External storage recommended for recording

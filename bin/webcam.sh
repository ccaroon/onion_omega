/usr/bin/mjpg_streamer --input "input_uvc.so --device /dev/video0 --fps 15 --resolution 1280x720 --led auto" --output "output_http.so --port 8080 --www /www/webcam"

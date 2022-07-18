gst-launch-1.0 v4l2src device=/dev/video6 ! video/x-raw,framerate=9/1,format=UYVY  ! queue ! videoconvert ! pngenc ! multifilesink location='Thermal_%d.png'

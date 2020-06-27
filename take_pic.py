import time
import os
from subprocess import call
# This script takes an image and saves it into "/images"
# Time format e.g. "10:14-26-06-2020.jpg"

# Check if folder exists, else create one.
if not os.path.exists("images"):
	os.makedirs("images")

# Check if camera is available.
if not os.path.exists("/dev/video0"):
	print("Camera is unavailable. Check your USB devices.")
else:
	call(["fswebcam", "-r 1280x720", "-S 10","--no-banner", "./images/%S:%H:%M-%d-%m-%Y.jpg"])
	# -S is the argument to call "skip frames". 
	# 10 frames are skipped so the camera is able to adjust brightness.


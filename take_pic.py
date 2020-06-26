import time
import os
from subprocess import call

if not os.path.exists("images"):
	os.makedirs("images")

# -S is the argument to call "skip frames". 
# 10 frames are skipped so the camera is able to adjust brightness.

# Time format e.g. "10:14-26-06-2020.jpg"
call(["fswebcam", "-r 1280x720", "-S 10", "./images/%H:%M-%d-%m-%Y.jpg"])

import time
from subprocess import call

# -S is the argument to call "skip frames". 
# 10 frames are skipped so the camera is able to adjust brightness.

# Time format e.g. "10:14-26-06-2020.jpg"
call(["fswebcam", "-r 1280x720", "-S 10", "./%H:%M-%d-%m-%Y.jpg"])

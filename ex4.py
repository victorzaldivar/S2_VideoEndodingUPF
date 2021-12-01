import sys
import os

class ejercicio4:
    def __init__(self, a):
        self.a = a

    def subtitles(a):
        os.system("ffmpeg -i BBBvideo.mp4 -vf subtitles=subti.srt outsubti.mp4")
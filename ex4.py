import sys
import os

class ejercicio4:
    def __init__(self, a): # Esta función se tiene que definir siempre cuando creas la clase
        self.a = a

    def subtitles(a):
        os.system("ffmpeg -i BBBvideo.mp4 -vf subtitles=subti.srt outsubti.mp4")
        # Guarda el video mp4 con los subtitulos incorporados en el archivo 'outsubti.mp4'
import sys
import os

class ejercicio1():

    def __init__(self, a): # Esta función se tiene que definir siempre cuando creas la clase
        self.a = a

    def showMVandMB(a):
        os.system("ffmpeg -flags2 +export_mvs -i BBBvideo.mp4 -vf codecview=mv=pf+bf+bb motionvectors.mp4")
        # Guarda el video mp4 con los motion vectors y los macroblocks en el archivo 'motionvectors.mp4'






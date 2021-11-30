import sys
import os

class ejercicio():

    def __init__(self, a):
        self.a = a

    def showMVandMB(self,a):
        while True:  # Creo un menú para interactuar con el user
            try:
                result = int(
                    input("Choose one os these two options. '1','2' (0=return to main menu): \n"
                          "1. Show Motion Vectors \n"
                          "2. Show Macroblocks \n"))
            except ValueError:
                print("You must to enter a number.")
                continue
            if result == 1:
                os.system("ffmpeg -flags2 +export_mvs -i BBBvideo.mp4 -vf codecview=mv=pf+bf+bb motionvectors.mp4")
                continue
            elif result == 2:
                os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vf scale=858:480 Big_Buck_Bunny_60fps_480p.mp4")
                continue
            elif result == 0:  # Para salir del programa
                break
            elif result != 1 and result != 2:
                print("You must enter '1' or '2'.")
                continue






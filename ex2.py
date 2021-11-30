import sys
import os

"""
# era o una de las 3 opciones
os.system("ffmpeg -i input.mp4 -i Sample.mp3 -map 0 -map 1:a -c:v copy -shortest output.mp4")
os.system("ffmpeg -i input.mp4 -i Sample.mp3 -map 0 -map 1:a -c copy -shortest output.mp4")
os.system("ffmpeg -i video.mp4 -i audio.m4a -c copy -map 0:v -map 1:a output.mp4")
"""

class ejercicio2 :
    def __init__(self, a):
        self.a = a

    def exportAudio(self,a):
        while True:  # Creo un menú para interactuar con el user
            try:
                result = int(
                    input("Fist, we have to export an mp3 audio from BBB video. (0=return to main menu): \n"
                          "1. Press '1' to continue \n"))
            except ValueError:
                print("You must to enter a number.")
                continue
            if result == 1:
                os.system("ffmpeg -i input.mp4 -i Sample.mp3 -map 0 -map 1:a -c:v copy -shortest output.mp4")
                ejercicio2.addAudioContainer(self, a)
                continue
            elif result == 0:  # Para salir del programa
                break
            elif result != 1:
                print("You must enter '1' or '0'.")
                continue

    def addAudioContainer(self, a):
        while True:  # Creo un menú para interactuar con el user
            try:
                result = int(
                    input("Now, we have to add the mp3 audio container to BBB video. (0=return to main menu): \n"
                          "1. Press '1' to continue \n"))
            except ValueError:
                print("You must to enter a number.")
                continue
            if result == 1:
                os.system("ffmpeg -i BBBvideo.mp4 -i Sample.mp3 -map 0 -map 1:a -c copy -shortest output.mp4")

                continue
            elif result == 0:  # Para salir del programa
                break
            elif result != 1:
                print("You must enter '1' or '0'.")
                continue
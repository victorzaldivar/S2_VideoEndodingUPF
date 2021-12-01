import sys
import os

class ejercicio2:
    def __init__(self, a):
        self.a = a

    def exportAudio(a):
        while True:  # Creo un menú para interactuar con el user
            try:
                result = int(
                    input("Fist, we have to export an mp3 audio from BBB video. (0=return to main menu): \n"
                          "1. Press '1' to continue \n"))
            except ValueError:
                print("You must to enter a number.")
                continue
            if result == 1:
                os.system("ffmpeg -i BBBvideo.mp4 -vn -ar 44100 -ac 2 -ab 192k -f mp3 Sample.mp3")
                ejercicio2.addAudioContainer(a)
                break
            elif result == 0:  # Para salir del programa
                break
            elif result != 1:
                print("You must enter '1' or '0'.")
                continue

    def addAudioContainer(a):
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
                break

            elif result == 0:  # Para salir del programa
                break
            elif result != 1:
                print("You must enter '1' or '0'.")
                continue
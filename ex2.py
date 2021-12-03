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
            if result == 1: # El primer paso es extraer el audio del BBB video en archivo .mp3
                os.system("ffmpeg -i BBBvideo.mp4 -vn -ar 44100 -ac 2 -ab 192k -f mp3 Sample.mp3")
                # Guardamos el archivo de audio extraído en el directorio como 'Sample.mp3
                ejercicio2.addAudioContainer(a) # llamamos a la función addAudioContainer para hacer el segundo paso
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
            if result == 1: # El segundo paso y definitivo es añadir el archivo de audio 'Sample.mp3' al BBB video
                os.system("ffmpeg -i BBBvideo.mp4 -i Sample.mp3 -map 0 -map 1:a -c copy -shortest output.mp4")
                # La saldida será el video BBB guardado como 'output.mp4' donde dentro habrán 2 containers de video (mp3 y aac)
                break

            elif result == 0:  # Para salir del programa
                break
            elif result != 1:
                print("You must enter '1' or '0'.")
                continue
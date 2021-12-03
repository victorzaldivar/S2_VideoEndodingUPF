import sys
import os

# os.system("ffmpeg -i BBBvideo.mp4 2&> sortida.txt")

class ejercicio3():

    def __init__(self, a):
        self.a = a

    def selectBroadcasting(a):
        #os.system("ffmpeg -i BBBvideo.mp4 >> sortida.txt")
        try:
            with open("sortida.txt") as f: #leemos el fichero de texto 'sortida.txt'
                flat_list = [word for line in f for word in line.split()]
                # Esto te devuelve una lista (flat_list) donde en cada una de las posiciones
                # de la lista están cada una de las palabras del fichero 'sortida.txt'
            a = 'Video:'
            b = 'Audio:'
            # Creamos estas dos variables porq la info que necesitamos sabemos que está en la palabra siguiente a estas
            for i in (range(len(flat_list))): # recorremos cada una de las palabras de la lista
                if a == flat_list[i]: # si nos encontamos con la palabra 'Video:'
                    videocontainer = flat_list[i + 1] # que se guarde la siguiente palabra de la lista
            print("Video container: ", videocontainer)
            for i in (range(len(flat_list))): # recorremos otra vez la lista, pero esta vez para la palabra 'Audio:'
                if b == flat_list[i]:
                    audiocontainer = flat_list[i + 1]
            print("Audio container: ",audiocontainer)


            # Hacemos condicionales comparando las salidas de nuestro fichero 'sortida.txt' con los
            # diferentes codecs de video y audio

            # Le associamos los broadcasting standards correspondientes

            # Hacemos condicionales con 'if' en vez de elif porq un mismo video puede tener varios
            # broadcasting standards que funcionen bien

            if videocontainer == 'h264' or videocontainer == 'mpeg2video' and audiocontainer == 'aac' \
                    or audiocontainer == 'ac3' or audiocontainer == 'mp3':
                print("The Broadcasting standard that would fit with this video is DVB")
            if videocontainer == 'h264' or videocontainer == 'mpeg2video' and audiocontainer == 'aac':
                print("The Broadcasting standard that would fit with this video is ISDB")
            if videocontainer == 'h264' or videocontainer == 'mpeg2video' and audiocontainer == 'ac3':
                print("The Broadcasting standard that would fit with this video is ATSC")
            if videocontainer == 'h264' or videocontainer == 'avs' or videocontainer == 'mpeg2video' and audiocontainer == 'aac' \
                    or audiocontainer == 'ac3' or audiocontainer == 'mp3' or audiocontainer == 'dra' or audiocontainer == 'mp2':
                print("The Broadcasting standard that would fit with this video is DTMB")
        except FileNotFoundError:
            print("No se ha encontrado el archivo de texto")












import sys
import os

# os.system("ffmpeg -i BBBvideo.mp4 2&> sortida.txt")

class ejercicio3():

    def __init__(self, a):
        self.a = a

    def selectBroadcasting(a):
        #os.system("ffmpeg -i BBBvideo.mp4 >> sortida.txt")
        try:
            with open("sortida.txt") as f:
                flat_list = [word for line in f for word in line.split()]
            a = 'Video:'
            b = 'Audio:'
            for i in (range(len(flat_list))):
                if a == flat_list[i]:
                    videocontainer = flat_list[i + 1]
            print("Video container: ", videocontainer)
            for i in (range(len(flat_list))):
                if b == flat_list[i]:
                    audiocontainer = flat_list[i + 1]
            print("Audio container: ",audiocontainer)

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












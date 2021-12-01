import sys
import os

# os.system("ffmpeg -i BBBvideo.mp4 >> sortida.txt")
try:
    with open("sortida.txt") as f:
        flat_list = [word for line in f for word in line.split()]
    a = 'Video:'
    b = 'Audio:'
    for i in (range(len(flat_list))):
        if a == flat_list[i]:
            videocontainer = flat_list[i+1]
    print(videocontainer)
    for i in (range(len(flat_list))):
        if b == flat_list[i]:
            audiocontainer = flat_list[i+1]
    print(audiocontainer)
except FileNotFoundError:
    print("No se ha encontrado el archivo de texto")

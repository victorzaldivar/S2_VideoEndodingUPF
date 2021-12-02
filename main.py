import ex1
import ex2
import ex3
import ex4

header = """
    ################################
       #### S2 - More FFMPEG ####
    ################################
     ## Made by Víctor Zaldívar ##"""

main_options = """
What do you want to do?
    1.- Show macroblocks and motion vectors
    2.- Add a new audio container 
    3.- See which broadcasting standard would fit to BBB video.
    4.- Add subtitles to BBB video
    0.- Exit"""

def show_menu():

    print(header)
    a=0

    exit_game = False
    while not exit_game:
        print(main_options)

        selected_option = input()
        if selected_option == "0":
            exit_game = True

        elif selected_option == "1":
            ex1.ejercicio1.showMVandMB(a)

        elif selected_option == "2":
            ex2.ejercicio2.exportAudio(a)

        elif selected_option == "3":
            ex3.ejercicio3.selectBroadcasting(a)

        elif selected_option == "4":
            ex4.ejercicio4.subtitles(a)

        else:
            print("This is not a valid option! Let's try again...")


if __name__ == '__main__':
    show_menu()
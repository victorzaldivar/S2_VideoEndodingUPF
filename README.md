# S2_VideoEndodingUPF

That's the second Seminar of Audio and Video Encoding made by Víctor Zaldivar. The main purpose for the lab is to implement the ‘ffmpeg’ through python scripts. First thing that I did was download the BBB video from internet and trimm it into a 60 seconds video called 'BBBvideo.mp4'. 

Every task of the seminar is divided in a different python scripts inside the project folder. Although, inside each scripts we can find a class corresponding to the task, and all the methods and functions needed to execute the exercice. By calling the main script, you are able to run all the program and iterate between all the classes and functions.

The first Task consist of showing the motions vector and the macroblocks of the the BBB video. To do it, I use an specific comand of 'ffmpeg' to implement it. The output would be store it as ‘motionvectors.mp4’.

The first Task consist of getting 2 audio containers inside the BBB video. To do it, the first step is extracting the audio of the BBB video as mp3 file by 'ffmpeg'. Then, we have to add this audio file as a new container inside the original video using 'ffmpeg' too. The information of the output should be:

![image](https://user-images.githubusercontent.com/94495723/145200976-5a3d88ca-14be-4e29-bb22-1bca4e558d91.png)

The output would be store it as ‘output.mp4’. As we can see, we have 3 different containers on the information about the output file, one video codec (h264) and 2 audio codecs (aac and mp3).

The third Task consist of predict which standard broadcasting would be fit with any video. In that case, we are working only with the BBB video but can be done by any other one. The first thing that I did was save the information about the BBB video inside a text file using the following 'ffmpeg' command: "ffmpeg -i BBBvideo.mp4 2&> sortida.txt". As the information that we want is the audio and video codecs, we can notice that this informations are on the word behind the words 'Audio:' and 'Video:'. For that, I read and iterate over the text file to extract the strings with the informations about the codecs. Finally, using conditionals, we can predict which standard broadcasting would be fit for the BBB video. 

The last Task consist of showing subtitles on the the BBB video. To do it, I downloaded a .str file from a movie on internet and by a text editor I changed somethings to do the subtitles according to the lenght of the video and to get the desired subtitles. The .str file is stored as 'subti.srt' and the output video would be store it as ‘outsubti.mp4’. __THERE ARE A EATER EGG ON THIS EXERCISE__.

# Problems
In exercise 3, for saving the information on the text file I did it with this command ("ffmpeg -i BBBvideo.mp4 2&> sortida.txt") on the ubuntu terminal. When I tried to call this command through the python script using 'os.system' the system fails. I tried to add a time.sleep or using others ffmpeg commands but it doesn't work anything. This is why are the 'sortida.txt' as a file inside the project folder. 

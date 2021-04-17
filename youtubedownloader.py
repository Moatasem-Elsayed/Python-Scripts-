from pytube import YouTube ,Playlist
from tkinter import filedialog  
import os 

select=int(input("1- PlayList \n 2- Single Video"))
link=input("Please enter your url:")
print("please choose the downloading path :")
pathsave= filedialog.askdirectory() 

def finish():
    print("dowanload is done")
    os.startfile(pathsave)

if select == 2:   
    video=YouTube(link)
    video.streams.get_highest_resolution().download(output_path=pathsave)
elif select == 1:
    playlist=Playlist(link)
    for video in playlist.videos:
         video.streams.get_highest_resolution().download(output_path=pathsave)
else :
    exit()
video.register_on_complete_callback(finish())
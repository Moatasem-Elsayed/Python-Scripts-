from pytube import YouTube ,Playlist
from tkinter import filedialog  
import os 
import time
select=int(input("1- PlayList \n2- Single Video\n"))
link=input("Please enter your url:")
print("please choose the downloading path :")
pathsave= filedialog.askdirectory() 
cnt=0
    
def finish():
    print("dowanload is done")
    os.startfile(pathsave)
    cnt=0
    
def progress():
    global cnt 
    cnt=cnt+1
    print("Loading..",end=" ")
    print(cnt)
       

if select == 2:   
    video=YouTube(link)
    video.streams.get_highest_resolution().download(output_path=pathsave)
    
elif select == 1:
    playlist=Playlist(link)
    for video in playlist.videos:
         video.streams.get_highest_resolution().download(output_path=pathsave)
         video.register_on_progress_callback(progress())
         
else :
    exit()


video.register_on_complete_callback(finish())

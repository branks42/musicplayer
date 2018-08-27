from tkinter import *
from pygame import mixer
from tkinter.filedialog import askopenfilename

song = ""

def open_():
    global song
    window.filename = askopenfilename(initialdir = "Place directory here",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    song = str(window.filename)
    print(song)

    
def play_():
   mixer.init()                               
   mixer.music.load(song) 
   mixer.music.play()
    
def stop_():
    mixer.music.stop()

# Want to add time scrubber and ability to make playlists eventually    
    
window = Tk()
 
window.title("Workhorse Music Player")

btn = Button(window, text="PLAY",bg='#F2C417',fg='#347ED1',bd=8,command = play_, height=2, width=15)
btn.grid(column=1, row=0)
Button(window, text="STOP",bg='#F2C417',fg='#347ED1',bd=8,command = stop_, height=2, width=15).grid(column=2, row=0)
Button(window, text="OPEN",bg='#F2C417',fg='#347ED1',bd=8,command = open_, height=2, width=15).grid(column=3, row=0)


window.mainloop()

# END.

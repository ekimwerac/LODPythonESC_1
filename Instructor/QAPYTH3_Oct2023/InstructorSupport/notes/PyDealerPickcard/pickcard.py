import os
import sys
import tkinter
import random

dirpath = ".\Bitmaps"
files = os.listdir(dirpath)

def show_next():
    random.shuffle(files)
    #print ("show next",files[0])
    
    gifpath = os.path.join(dirpath, files[0])
    gif = tkinter.PhotoImage(file=gifpath)
    img.config(image=gif)
    root.mainloop()
    
def end_it():
    root.quit()
    
root = tkinter.Tk()
root.title("Pickcard")
root.geometry("200x200+0+0")
root.wm_iconbitmap('qa.ico')

Fm = tkinter.Frame(padx=15, pady=15)
Fm.pack()

img = tkinter.Label()
img.pack()

bNext = tkinter.Button(Fm,text="Next",command=show_next)
bNext.pack({"side": "left"})
bExit = tkinter.Button(Fm,text="Exit",command=end_it)
bExit.pack({"side": "left"})

show_next()



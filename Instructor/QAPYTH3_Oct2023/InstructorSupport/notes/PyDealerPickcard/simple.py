import os
import sys
import tkinter
import random
import threading

dirpath = ".\Bitmaps"
files = os.listdir(dirpath)

def show_next():
    tid = threading.Thread (target=thread_func)
    tid.start()
    tid.join()

def thread_func():
    random.shuffle(files)
    #print ("show next",files[0])
    
    i = 0
    #while True:
    gifpath = os.path.join(dirpath, files[i])
    gif = tkinter.PhotoImage(file=gifpath)
    img.config(image=gif)
    root.mainloop() 
    i+=1
    if i >= len(files):
        i = 0
    
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



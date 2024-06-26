import os, sys
import tkinter

initialised = False
dirpath = '.\Bitmaps'
    
def initialise():
    global root, initialised
    root = tkinter.Tk()
    root.title("Display")
    root.geometry("200x100+0+0")
    root.wm_iconbitmap('qa.ico')

    initialised = True

def endit(arg):
    global root
    root.quit()
    
def display_file(gifname):
    if not gifname.endswith('gif'):
        raise ValueError("Invalid name: <"+gifname+">")
    
    gifpath = os.path.join(dirpath, gifname)
    if not os.path.isfile(gifpath):
    	raise IOError("Incorrect file name: <"+gifpath+">")
    
    if not initialised: initialise()
    tkinter.At(20,20)
    print ("display_file:",gifpath)
    
    Fm = tkinter.Frame(padx=15, pady=15)
    Fm.pack()
        
    gif = tkinter.PhotoImage(file=gifpath)
    img = tkinter.Label()
    img.pack()
    img.config(image=gif)
    root.after (1000, endit,'')
    root.mainloop()
   
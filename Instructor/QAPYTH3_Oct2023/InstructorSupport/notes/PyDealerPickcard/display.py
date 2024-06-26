import os, sys
import tkinter


dirpath = '.\Bitmaps'
gifname = sys.stdin.readline()[:-1]
if not gifname.endswith('gif'):
    raise ValueError("Invalid name: <"+gifname+">")
    
gifpath = os.path.join(dirpath, gifname)

root = tkinter.Tk()
root.title("Display")
root.geometry("200x100+0+0")

Fm = tkinter.Frame(padx=15, pady=15)
Fm.pack()
img = tkinter.Label()
img.pack()

gif = tkinter.PhotoImage(file=gifpath)
img.config(image=gif)
    
root.mainloop(  )
import tkinter as tk
import os
from tkinter import filedialog as fd
from gtts import gTTS
from tkinter import messagebox as mb
root = tk.Tk()
root.geometry("400x80")
root.title("Text to Speech")
root.resizable(width=False,height=False)
var = tk.StringVar()
var.set("Enter Text")
enter = tk.Entry(root, textvariable=var, width=50)
enter.pack(side="top")

def hit():
    global loc
    file = gTTS(text=var.get(), slow=False,lang='en')
    try:
      loc = fd.asksaveasfilename(defaultextension="*.mp3")
      file.save(loc)
    except:
        loc = "null"

def hit1(event):
    hit()
def play():
   try:
       if loc!="null":
         os.system("afplay "+loc)
       else:
           mb.showerror(title="Text to Speech", message="First Convert!")

   except:
       mb.showerror(title="Text to Speech", message="First Convert!")


but1 = tk.Button(root, text="play", command=play)
but1.pack(side="bottom")

but = tk.Button(root, text="convert",command=hit)
but.pack(side="bottom")

root.bind("<Return>", hit1)

root.mainloop()
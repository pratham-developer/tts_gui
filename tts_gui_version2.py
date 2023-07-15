import tkinter as tk
import os
from tkinter import filedialog as fd
from gtts import gTTS
from tkinter import messagebox as mb
root = tk.Tk()
root.geometry("565x420")
root.title("Text to Speech")
root.resizable(width=False,height=False)
sc=tk.Scrollbar(root)
sc.pack(side="right", fill="y")

enter = tk.Text(height=21, width=60, yscrollcommand=sc.set, font=("Arial", 15))
enter.pack(side="top")

sc.config(command=enter.yview)

def hit():
    global loc
    try:
      file = gTTS(text=enter.get("1.0","end-1c"),lang='en')
      try:
          loc = fd.asksaveasfilename(defaultextension="*.mp3")
          file.save(loc)
      except:
          loc = "null"
    except:
        mb.showerror(title="Text to Speech", message="Enter Text!")

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

enter.insert("1.0","Enter Text")
root.mainloop()
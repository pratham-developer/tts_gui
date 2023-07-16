import tkinter as tk
import os
from tkinter import filedialog as fd
from gtts import gTTS
from tkinter import messagebox as mb
from langdetect import detect
import socket
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
      tex = enter.get("1.0", "end-1c")
      file = gTTS(text=tex, lang=detect(tex), slow=False)
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

say = tk.Label(root)
say.place(x=30, y=380)

say1 = tk.Label(root, text="* supports multiple languages")
say1.place(x=350, y= 380)

ip = socket.gethostbyname(socket.gethostname())
network = not ip == '127.0.0.1'
if network==True:
    say.config(text="internet available ✅")
elif network==False:
    say.config(text="internet not available ❌")

root.mainloop()

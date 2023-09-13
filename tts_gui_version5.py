import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog as fd
from gtts import gTTS
from tkinter import messagebox as mb
from langdetect import detect
import socket
import PyPDF2
root = tk.Tk()
root.geometry("565x470")
root.title("Text to Speech")
root.resizable(width=False,height=False)
sc=ttk.Scrollbar(root)
sc.pack(side="right", fill="y")
enter = tk.Text(height=21, width=60, yscrollcommand=sc.set, font=("Arial", 15))
enter.pack(side="top")
sc.config(command=enter.yview)

choose = ttk.Combobox(root,values=["India","US","UK","Canada","Australia","Ireland"])
choose.place(x=340,y=420)
choose.current(0)
choose['state']='readonly'
def hit():
    global loc
    try:
      tex = enter.get("1.0", "end-1c")
      file = gTTS(text=tex, lang=detect(tex))
      if detect(tex)=='en':
          acc = choose.get()
          if acc =="India":
              way="co.in"
          elif acc=="US":
              way="us"
          elif acc=="UK":
              way="co.uk"
          elif acc=="Canada":
              way="ca"
          elif acc=="Australia":
              way="com.au"
          elif acc=="Ireland":
              way="ie"
          file=gTTS(text=tex,lang='en', tld=way)
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

def pdf():
   global loc
   try:
    fi = fd.askopenfilename(defaultextension=".pdf")
    book = open(fi,'rb')
    read = PyPDF2.PdfReader(book)
    num = len(read.pages)
    tex=""
    for i in range(0,num):
        page = read.pages[i]
        tex = tex + page.extract_text()
    file = gTTS(text=tex, lang=detect(tex))
    if detect(tex) == 'en':
            acc = choose.get()
            if acc == "India":
                way = "co.in"
            elif acc == "US":
                way = "us"
            elif acc == "UK":
                way = "co.uk"
            elif acc == "Canada":
                way = "ca"
            elif acc == "Australia":
                way = "com.au"
            elif acc == "Ireland":
                way = "ie"
            file = gTTS(text=tex, lang='en', tld=way)
    try:
         loc = fd.asksaveasfilename(defaultextension="*.mp3")
         file.save(loc)
    except:
            loc = "null"
   except:
    mb.showerror(title="Text to Speech", message="Choose a valid pdf")



but1 = ttk.Button(root, text="play", command=play)
but1.place(x=220,y=365)

but = ttk.Button(root, text="convert",command=hit)
but.place(x=220,y=400)

but2 = ttk.Button(root, text="convert pdf",command=pdf)
but2.place(x=211,y=435)


enter.insert("1.0","Enter Text")

say = ttk.Label(root)
say.place(x=30, y=385)

say1 = ttk.Label(root, text="[supports multiple languages]")
say1.place(x=10, y= 420)

ip = socket.gethostbyname(socket.gethostname())
network = not ip == '127.0.0.1'
if network==True:
    say.config(text="internet available ✅")
elif network==False:
    say.config(text="internet not available ❌")

say2 = ttk.Label(root,text='choose the english accent👇')
say2.place(x=350,y=385)

root.mainloop()

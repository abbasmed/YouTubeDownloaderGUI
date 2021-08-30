#!/usr/bin/python3
# By @abbasmed

from pytube import YouTube
from tkinter import *
from tkinter import ttk


class App():
     def __init__(self,master):
          self.label = ttk.Label(text = 'Welcome to the YouTube Downloader',
                                 justify = CENTER,
                                 foreground = 'red',
                                 font = ('Courier',12,'bold')).pack()
          self.passlink = ttk.Entry(master, width = 70)
          self.passlink.pack()
           
          logo1 = PhotoImage(file = 'C:\Users\med\Desktop\yt_logo.jpg')
          logo = logo1.subsample(5,5)

          self.button = ttk.Button(master, text = 'Download',
                                   image = logo,
                                   compound = LEFT,
                                   command = self.downl).pack()

          self.file_type = StringVar()
          self.video_type = ttk.Radiobutton(master, text = 'video', variable = self.file_type,value = 'v').pack()
          #self.video_type.pack()
          
          self.audio_type = ttk.Radiobutton(master, text = 'audio', variable = self.file_type,value = 'a').pack()
          #self.audio_type.pack()

     def downl(self):
          if self.file_type.get() == 'v':
               file_ = YouTube(self.passlink.get()).streams.first().download()
          elif self.file_type.get() == 'a':
               file_ = YouTube(self.passlink.get()).streams.filter(only_audio=True).all()
               file_[0].download()
          return file_

def main():
     root = Tk()
     myapp = App(root)
     root.mainloop()

if __name__ == '__main__' : main()

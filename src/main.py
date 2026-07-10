import tts_all
import tkinter
from tkinter import *

class GUI_TTS():
    def __init__(self):
        self.rot = Tk()
        self.rot.title("TTS app")
        width, height = 300, 500
        self.rot.geometry(f"{width}x{height}")
        self.rot.maxsize(400, 600), self.rot.minsize(200, 400)
        self.rot.mainloop()

if __name__ == "__main__":
    GUI_TTS()
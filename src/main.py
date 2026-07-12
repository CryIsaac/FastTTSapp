import tts_all, threading, queue
from tkinter import *
from tkinter import ttk, Tk

class GUI():
    def __init__(self, rot):
        self.rot = rot
        self.rot.title("TTS app")
        self.rot.geometry("300x400")
        self.initButtons()
    def initButtons(self):
        self.config1()
    
    def config1(self):
        self.tts = tts_all.pyttsx3TTS()
        def console_say():
            print(f"{self.entry.get()}, {self.combobox.get()}")

        
        
        self.entry = ttk.Entry()
        self.entry.pack(anchor='n', fill="x", ipady=2, pady=2)
        
        self.say_btn = ttk.Button(text="SAY", command=console_say)
        self.say_btn.pack(anchor="ne", fill="x", side="right")

        list_combobox = [voice.name for voice in self.tts.voices]
        self.combobox = ttk.Combobox(state="readonly", values=list_combobox)
        self.combobox.set(list_combobox[0])
        self.combobox.pack(anchor='n', fill="x", expand=True, side="right", pady=2)
        

    def config2(self):
        self.tts = None
        
    def config3(self):
        self.tts = None
    

if __name__ == "__main__":
    rot = Tk()
    app = GUI(rot)
    rot.mainloop()
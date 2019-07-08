from tkinter import *
import tkinter.ttk

class homeUI():
    def __init__(self, master):
        self.master=master
        self.f1 = Frame(master)
        self.f1.pack(fill="both", expand=True, padx=20, pady=20)
        self.master.title("_________ Forum")
        self.master.geometry('1024x768')





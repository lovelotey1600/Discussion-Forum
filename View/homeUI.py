import sys
sys.path.append("..")
from tkinter import *
import tkinter as tk
import tkinter.ttk
#from tkinter import scrolledtext
from Controller.ForumFunctions import *

class homeUI():
    def insertQuestion(self):
        self.ques=self.q.get()
        self.ans=self.a.get()
        print(self.ques)
        f=ForumFunctions
        f.createQuestion(f,self.ques,self.ans)
        self.win.destroy()

    def startDiscussion(self):
        self.win = tk.Toplevel()
        self.win.wm_title("Window")
    
        self.l = Label(self.win, text="Enter your question Title: ")
        self.l.grid(row=0, column=0,padx=10, pady=10)

        self.q=Entry(self.win, width=20)
        self.q.grid(row=0, column=1,padx=10, pady=10)

        self.l2 = Label(self.win, text="Elaborate your problem: ")
        self.l2.grid(row=1, column=0,padx=10, pady=10)

        self.a=Entry(self.win, width=20)
        self.a.grid(row=1, column=1,padx=10, pady=10)


        self.b = Button(self.win, text="Submit", command=self.insertQuestion)
        self.b.grid(row=2, column=1)

        
    def search(self):
        self.w2.remove(self.b2)
        self.searchT=Entry(self.master,width=20)
        self.w2.add(self.searchT)
        self.w2.add(self.b2)
        

    def __init__(self, master):
        self.master=master
        self.f1 = Frame(master)
        self.f1.pack()
        self.master.title("_________ Forum - Home")
        self.master.geometry('1024x768')
        self.p1= PanedWindow()
        self.p1.pack(fill="both", expand=True)

        self.w2 = PanedWindow(self.p1, orient = VERTICAL)  
        self.p1.add(self.w2)  

        self.label=Label(self.p1,text="Forum ",anchor="n")
        self.p1.add(self.label)


        #Left Pane
        self.b1=Button(self.p1,text="Create a Chatroom ")
        self.b1.pack(padx=10, pady=10)
        self.w2.add(self.b1)

        self.b3=Button(self.p1,text="Start a new Dicussion ",command=self.startDiscussion)
        self.b3.pack(padx=10, pady=10)
        self.w2.add(self.b3)

        self.b4=Button(self.p1,text="Search for a discussion ",command=self.search)
        self.b4.pack(padx=10, pady=10)
        self.w2.add(self.b4)

        

        self.b2=Button(self.p1,text="Exit")
        self.b2.pack(padx=10, pady=10,side="bottom")
        self.w2.add(self.b2)






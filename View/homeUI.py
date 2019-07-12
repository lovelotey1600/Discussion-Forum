import sys
sys.path.append("..")
from tkinter import *
import tkinter as tk
import tkinter.ttk
from Controller.ForumFunctions import *

class homeUI():
    def on_configure(self,event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def refresh(self):
        l=ForumFunctions
        self.list=l.getList1(l)
        self.questions=l.getQuestions(l)
        
        for i in range(0,self.list):
            
            # --- add widgets in frame ---

            self.label_widgets.append(Label(self.forumFrame,text=self.questions[i],font=(None,20)))
            self.label_widgets[-1].grid(row= i+1, column =0, sticky='e', padx=10, pady=10)

    def search(self,searchstr):
        
        f=ForumFunctions
        val=f.search(f,searchstr)
        if val==1:
            messagebox.showinfo("Search Completed ","There is no question like this present on the forum")   

    def insertQuestion(self):
        self.ques=self.q.get()
        self.ans=self.a.get()
        f=ForumFunctions
        f.createQuestion(f,self.ques,self.ans)
        self.refresh()
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


        self.b = tkinter.ttk.Button(self.win, text="Submit", command=self.insertQuestion)
        self.b.grid(row=2, column=1)

        
    def searchTextBox(self):
        self.w2.remove(self.b2)
        self.searchT=Entry(self.master,width=20,)
        self.searchT.bind("<Return>", (lambda event: self.search(self.searchT.get())))
        self.b3.grid(column=0,row=3,padx=10, pady=10)
        self.w2.add(self.searchT)
        self.b3=tkinter.ttk.Button(self.p1,text="S",command=lambda:self.search(self.searchT.get()))
        self.b3.grid(column=1,row=3,padx=10, pady=10)
        self.w2.add(self.b3)
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
        self.b1=tkinter.ttk.Button(self.p1,text="Create a Chatroom ")
        self.b1.grid(column=0,row=0,padx=10, pady=10)
        self.w2.add(self.b1)

        self.b3=tkinter.ttk.Button(self.p1,text="Start a new Dicussion ",command=self.startDiscussion)
        self.b3.grid(column=0,row=1,padx=10, pady=10)
        self.w2.add(self.b3)

        self.b4=tkinter.ttk.Button(self.p1,text="Search for a discussion ",command=self.searchTextBox)
        self.b4.grid(column=0,row=2,padx=10, pady=10)
        self.w2.add(self.b4)

        

        self.b2=tkinter.ttk.Button(self.p1,text="Exit")
        self.b2.grid(column=0,row=4,padx=10, pady=10)
        self.w2.add(self.b2)

        #Right pane
        self.canvas=Canvas(self.p1)
        self.canvas.pack(side=tk.LEFT)
        self.p1.add(self.canvas)

        self.scroll=Scrollbar(self.p1,command=self.canvas.yview)
        self.scroll.pack(side=tk.LEFT,fill='y')
        self.p1.add(self.scroll)

        self.canvas.configure(yscrollcommand = self.scroll.set)
        self.canvas.bind('<Configure>', self.on_configure)

        self.label_widgets=[]
        self.forumFrame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.forumFrame, anchor='w')
        self.refresh()


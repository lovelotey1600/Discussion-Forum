from tkinter import *
import tkinter.ttk

class homeUI():
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

        self.b3=Button(self.p1,text="Start a new Dicussion ")
        self.b3.pack(padx=10, pady=10)
        self.w2.add(self.b3)

        self.b4=Button(self.p1,text="Search for a discussion ",command=self.search)
        self.b4.pack(padx=10, pady=10)
        self.w2.add(self.b4)

        

        self.b2=Button(self.p1,text="Exit")
        self.b2.pack(padx=10, pady=10,side="bottom")
        self.w2.add(self.b2)


root = Tk()
my_gui = homeUI(root)
root.mainloop()




from tkinter import *
import tkinter.ttk
class StartUP:
    def __init__(self, master):
        self.master=master
        self.f1 = Frame(master)
        self.f1.pack(fill="both", expand=True, padx=20, pady=20)
        self.master.title("_________ Forum")
        self.master.geometry('1024x768')
        self.f2=Frame(master)
        self.f2.place(in_=self.f1, anchor="c", relx=.5, rely=.5)

        #Registration Section
        self.l1=Label(self.f2,text="Registration")
        self.l1.grid(row=1,column=1)

        self.l2=Label(self.f2,text="Enter User ID")
        self.l2.grid(row=2,column=1)

        self.ruID=Entry(self.f2,width=20)
        self.ruID.grid(column=2,row=2)

        self.b1=Button(self.f2,text="Register")
        self.b1.grid(row=5,column=2)

        #Login Section
        self.l3=Label(self.f2,text="Login")
        self.l3.grid(row=1,column=5)

        self.l4=Label(self.f2,text="Enter User ID")
        self.l4.grid(row=2,column=5)

        self.luID=Entry(self.f2,width=20)
        self.luID.grid(column=6,row=2)

        self.l5=Label(self.f2,text="Enter Password")
        self.l5.grid(row=3,column=5)

        self.passwd=Entry(self.f2,width=20)
        self.passwd.grid(column=6,row=3)

        self.b1=Button(self.f2,text="Log in")
        self.b1.grid(row=5,column=6)
        
        #Seperator
        self.separatorb = tkinter.ttk.Separator(self.f2)
        self.separatorb.grid(row=4, column=0, columnspan=7, sticky="we")

        self.separatort = tkinter.ttk.Separator(self.f2)
        self.separatort.grid(row=0, column=0, columnspan=7, sticky="we")

        self.separatorl = tkinter.ttk.Separator(self.f2,orient=VERTICAL)
        self.separatorl.grid(row=0, column=0, rowspan=4, sticky="ns")

        self.separatorr = tkinter.ttk.Separator(self.f2,orient=VERTICAL)
        self.separatorr.grid(row=0, column=7, rowspan=4, sticky="ns")

        self.separatorc = tkinter.ttk.Separator(self.f2,orient=VERTICAL)
        self.separatorc.grid(row=0, column=4, rowspan=4, sticky="ns")



root = Tk()
my_gui = StartUP(root)
root.mainloop()




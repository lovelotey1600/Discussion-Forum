from tkinter import *
import tkinter.ttk
import sys
sys.path.append("..")

from View.RegsitrationUI import *
from View.homeUI import *
from Controller.signupIN import *
class StartUP:
    def toggleRegistrationUI(self):
        if self.ruID.get=="":
            messagebox.showinfo("Registration","You need to enter some user id.")
        else:
            self.u=self.ruID.get()
            self.u="@"+self.u
            r=register
            chk =r.usrrchk(r,self.u)
            if chk==1:
                self.master.destroy()
                root = Tk()
                my_gui = RegistrationUI(root,self.u)
                root.mainloop()
    
    def toggleLoginUI(self):
        if self.luID.get=="" and self.passwd.get()=="":
            messagebox.showinfo("Log in","You need to enter some user id and password.")
        else:
            self.uid=self.luID.get()
            self.uid="@"+self.uid
            self.pd=self.passwd.get()
            l=login
            chk = l.usrlogin(l,self.uid,self.pd)
            if chk==1:
                self.master.destroy()
                root = Tk()
                my_gui = homeUI(root)
                root.mainloop()
            
        


        pass

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
        self.l1.grid(row=1,column=1,padx=10, pady=10)

        self.l2=Label(self.f2,text="Enter User ID")
        self.l2.grid(row=2,column=1,padx=10, pady=10)

        self.ruID=Entry(self.f2,width=20)
        self.ruID.grid(column=2,row=2,padx=10, pady=10)

        self.b1=Button(self.f2,text="Register",command=self.toggleRegistrationUI)
        self.b1.grid(row=5,column=2,padx=10, pady=10)

        #Login Section
        self.l3=Label(self.f2,text="Login")
        self.l3.grid(row=1,column=5,padx=10, pady=10)

        self.l4=Label(self.f2,text="Enter User ID")
        self.l4.grid(row=2,column=5,padx=10, pady=10)

        self.luID=Entry(self.f2,width=20)
        self.luID.grid(column=6,row=2,padx=10, pady=10)

        self.l5=Label(self.f2,text="Enter Password")
        self.l5.grid(row=3,column=5,padx=10, pady=10)

        self.passwd=Entry(self.f2,width=20)
        self.passwd.grid(column=6,row=3,padx=10, pady=10)

        self.b1=Button(self.f2,text="Log in",command=self.toggleLoginUI)
        self.b1.grid(row=5,column=6,padx=10, pady=10)
        
        #Seperator
        self.separatorb = tkinter.ttk.Separator(self.f2)
        self.separatorb.grid(row=4, column=0, columnspan=8, sticky="we",padx=10, pady=10)

        self.separatort = tkinter.ttk.Separator(self.f2)
        self.separatort.grid(row=0, column=0, columnspan=8, sticky="we",padx=10, pady=10)

        self.separatorl = tkinter.ttk.Separator(self.f2,orient=VERTICAL)
        self.separatorl.grid(row=0, column=0, rowspan=5, sticky="ns",padx=10, pady=10)

        self.separatorr = tkinter.ttk.Separator(self.f2,orient=VERTICAL)
        self.separatorr.grid(row=0, column=7, rowspan=5, sticky="ns",padx=10, pady=10)

        self.separatorc = tkinter.ttk.Separator(self.f2,orient=VERTICAL)
        self.separatorc.grid(row=0, column=4, rowspan=5, sticky="ns",padx=10, pady=10)








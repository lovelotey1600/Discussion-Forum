import sys
sys.path.append("..")
from tkinter import messagebox
from Model.DbConnection import *
class DbFunctions:
    
    def registerAccountDB(self,n,ui,uh,pd):
        try:
            self.mydb=DbConnection.getConnection()
            self.mycursor=self.mydb.cursor()
            self.sql="insert into users(uname,uid,usrh,passwd) values (%s,%s,%s,%s)"
            self.values=(n,ui,uh,pd)
            self.mycursor.execute(self.sql,self.values)
            self.mydb.commit()
            messagebox.showinfo("Registration completed",n+ " has been successfully registered")   
        except Exception as e:  
            messagebox.showinfo("Error", "you cannot register \n "+str(e))   

    




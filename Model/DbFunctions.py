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

    def checkRegisteredAccountDB(self,uid):
        
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select * from users where usrh = (%s)"
        self.values=(uid,)
        self.mycursor.execute(self.sql,self.values)
        re=self.mycursor.fetchone()
        if re is None:
            return 1
        else:
            messagebox.showinfo("Registration ",uid+ " had been already registered. Please try logging in.")   

    def checkLoginCredentials(self,uid,pd):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select * from users where usrh = (%s) and passwd =(%s)"
        self.values=(uid,pd)
        self.mycursor.execute(self.sql,self.values)
        re=self.mycursor.fetchone()
        if re is not None:
            return 1
        else:
            messagebox.showinfo("Login ","Invalid username or password.")   
        pass
    
    def crtForumTable(self):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="CREATE TABLE IF NOT EXISTS `forumTable` (ques_id bigint PRIMARY KEY AUTOINCREMENT NOT NULL,questionTitle TEXT not null);"
        self.mycursor.execute(self.sql)
        self.mydb.commit()
        
    def crtQuesTable(self,ques):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="insert into forumTable(questionTitle) values(%s)"
        self.que=(ques,)
        self.mycursor.execute(self.sql,self.que)
        self.mydb.commit()

        self.sql1="select ques_id from 'forumTable' where questionTitle=(%s);"
        self.que=(ques,)
        self.mycursor.execute(self.sql1,self.que)
        re=self.mycursor.fetchone()
        self.sql2="CREATE TABLE IF NOT EXISTS (%s) (answer_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,answer TEXT not null,upvote int DEFAULT '0',date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);"
        self.quID=(re,)
        self.mycursor.execute(self.sql2,self.quID)
        self.mydb.commit()

    def insertAnsTable(self,que,ans):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="insert into (%s)(answer) values(%s) "
        self.values=(que,ans)
        self.mycursor.execute(self.sql,self.values)
        self.mydb.commit()
       
        pass
    #create table (%s) (answer text not null,uid varchar(50),upvote int Default '0',date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"



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
            self.mydb.close()
        except Exception as e:  
            messagebox.showinfo("Error", "you cannot register \n "+str(e))   
            self.mydb.close()

    def checkRegisteredAccountDB(self,uid):
        
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select * from users where usrh = (%s)"
        self.values=(uid,)
        self.mycursor.execute(self.sql,self.values)
        re=self.mycursor.fetchone()
        if re is None:
            self.mydb.close()
            return 1
        else:
            messagebox.showinfo("Registration ",uid+ " had been already registered. Please try logging in.")   
            self.mydb.close()

    def checkLoginCredentials(self,uid,pd):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select * from users where usrh = (%s) and passwd =(%s)"
        self.values=(uid,pd)
        self.mycursor.execute(self.sql,self.values)
        re=self.mycursor.fetchone()
        if re is not None:
            self.mydb.close()
            return 1
        else:
            messagebox.showinfo("Login ","Invalid username or password.")   
            self.mydb.close()
           
    def crtForumTable(self):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="CREATE TABLE IF NOT EXISTS `forumTable` (ques_id bigint PRIMARY KEY AUTO_INCREMENT NOT NULL,questionTitle TEXT not null);"
        self.mycursor.execute(self.sql)
        self.mydb.commit()
        self.mydb.close()

    def searchQues(self,ques):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select * from forumTable where questionTitle = (%s)"
        self.que=(ques,)
        self.mycursor.execute(self.sql,self.que)
        re=self.mycursor.fetchone()
        if re is None:
            self.mydb.close()
            return 1
        else:
            self.mydb.close()
            return re[1]
        


    def crtQuesTable(self,ques):
        qu=self.searchQues(self,ques)
        if qu==1:
            self.mydb=DbConnection.getConnection()
            self.mycursor=self.mydb.cursor()
            self.sql="insert into forumTable(questionTitle) values(%s)"
            self.que=(ques,)
            self.mycursor.execute(self.sql,self.que)
            self.mydb.commit()
            self.mydb.close()

            self.mydb=DbConnection.getConnection()
            self.mycursor=self.mydb.cursor()
            self.sql1="select ques_id from forumTable where questionTitle = %s ;"
            self.que=(ques,)
            self.mycursor.execute(self.sql1,self.que)
            self.re=self.mycursor.fetchone()
            self.l=str(self.re[0])
            self.l=self.l+"q"

            self.mydb.close()


            self.mydb=DbConnection.getConnection()
            self.mycursor=self.mydb.cursor()
            self.sql2="CREATE TABLE IF NOT EXISTS {table} (answer_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,answer TEXT not null,upvote int DEFAULT '0',date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);"
            self.mycursor.execute(self.sql2.format(table=self.l))
            self.mydb.commit()
            self.mydb.close()
        else:
            messagebox.showinfo("Error ","This question had previously been asked. Try searching for that question")   
            self.mydb.close()

    def insertAnsTable(self,que,ans):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="insert into {table} (answer) values (%s) "
        self.values=(ans,)
        self.mycursor.execute(self.sql.format(table=self.l),self.values)
        self.mydb.commit()
        self.mydb.close()
       
    def getList(self):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select count(*) from forumTable"
        self.mycursor.execute(self.sql)
        re=self.mycursor.fetchone()
        self.mydb.close()
        return re[0]
        
    def getQuestions(self):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="select questionTitle from forumTable ORDER BY ques_id DESC"
        self.mycursor.execute(self.sql)
        re=self.mycursor.fetchall()
        self.mydb.close()
        list_of_questions=[]
        for i in range(len(re)):
            list_of_questions.append(re[i][0])
        
        return list_of_questions
    
        
    



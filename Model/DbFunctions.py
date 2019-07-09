import sys
sys.path.append("..")

from Model.DbConnection import *
class DbFunctions:
    
    def registerAccountDB(self,n,ui,uh,pd):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        print(n)
        self.sql="insert into users(uname,uid,usrh,passwd) values (%s,%s,%s,%s)"
        self.values=(n,ui,uh,pd)
        self.mycursor.execute(self.sql,self.values)
        self.mydb.commit()
        
    




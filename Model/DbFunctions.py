from DbConnection import *
class DbFunctions:
    
    def registerAccountDB(self,n,ui,uh,pd):
        self.mydb=DbConnection.getConnection()
        self.mycursor=self.mydb.cursor()
        self.sql="insert into table users(uname,uid,usrh,passwd) values (%s,%s,%s,%s)"
        self.values=(n,ui,uh,pd)
        self.mycursor.execute(self.sql,self.values)
        
    




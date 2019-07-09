import mysql.connector
class DbConnection:
    @staticmethod
    def getConnection():
        return mysql.connector.connect(host="localhost",user="root",passwd="",database="db")





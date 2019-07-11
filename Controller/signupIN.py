
import sys
sys.path.append("..")
from Model.DbFunctions import *

class register:
    def usrgstr(self,name,eid,userh,passwd):
        m1=DbFunctions
        m1.registerAccountDB(m1,name,eid,userh,passwd)
    def usrrchk(self,uid):
        m1=DbFunctions
        return m1.checkRegisteredAccountDB(m1,uid)


class login:
    def usrlogin(self,uid,passwd):
        m1=DbFunctions
        return m1.checkLoginCredentials(m1,uid,passwd)
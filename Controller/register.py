
import sys
sys.path.append("..")
from Model.DbFunctions import *

class register:
    def usrgstr(self,name,eid,userh,passwd):
        print(name)
        print(eid)
        print(userh)
        print(passwd)
        m1=DbFunctions
        m1.registerAccountDB(m1,name,eid,userh,passwd)
       





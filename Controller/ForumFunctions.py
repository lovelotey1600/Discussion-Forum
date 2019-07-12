import sys
sys.path.append("..")
from Model.DbFunctions import *

class ForumFunctions:
    
    def getList1(self):
        f2=DbFunctions
        f2.crtForumTable(f2)
        return f2.getList(f2)
        
    def getQuestions(self):
        f2=DbFunctions
        return f2.getQuestions(f2)
    
    def search(self,q):
        f2=DbFunctions
        return f2.searchQues(f2,q)

    def createQuestion(self,ques,ans):
        f2=DbFunctions
        f2.crtQuesTable(f2,ques)
        f2.insertAnsTable(f2,ques,ans)

    


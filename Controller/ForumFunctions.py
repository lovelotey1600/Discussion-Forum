import sys
sys.path.append("..")
from Model.DbFunctions import *

class ForumFunctions:

    def createQuestion(self,ques,ans):
        f2=DbFunctions
        f2.crtForumTable(f2)
        f2.crtQuesTable(f2,ques)
        f2.insertAnsTable(f2,ques,ans)




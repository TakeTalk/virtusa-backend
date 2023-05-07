from service.cityNameService import *

class Knowledge:
    primary = ['hospital', 'doctor']
    citys = getAllCityName()
    gestureWords = ['hi','hello','hlw',"what's up",'hey','how are you']
    leaving =['bye','good']
    unexpected= ['what','name','who','thank you']
    preps=['nearme', 'nearby']
    appo=['appoinment']
    hospital=['apollo']
    knowledgeWords = primary + citys + gestureWords + appo + hospital + preps + leaving+ unexpected



    def ct(self):
        return self.citys

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

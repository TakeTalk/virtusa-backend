from service.cityNameService import *

class Knowledge:
    primary = ['hospital', 'doctor']
    citys = getAllCityName()
    gestureWords = ['hi','hello','hlw',"what's up",'hey','how are you']
    preps=['nearme', 'nearby']
    appo=['appoinment']
    hospital=['apollo']
    knowledgeWords = primary + citys + gestureWords + appo + hospital + preps



    def ct(self):
        return self.citys

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

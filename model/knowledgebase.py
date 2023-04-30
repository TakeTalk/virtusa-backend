from service.cityNameService import *

class Knowledge:
    primary = ['hospital', 'doctor']
    citys = getAllCityName()
    gestureWords = ['hi','hello','hlw',"what's up"]
    preps=['nearme', 'nearby']

    knowledgeWords = primary + citys+gestureWords+preps



    def ct(self):
        return self.citys

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

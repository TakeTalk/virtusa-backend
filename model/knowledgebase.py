from service.cityNameService import *

class Knowledge:
    primary = ['hospital', 'doctor']
    citys = getAllCityName()
    knowledgeWords = primary + citys


    def ct(self):
        return self.citys

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

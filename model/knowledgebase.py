from service.cityNameService import *

class Knowledge:
    primary = ['hospital', 'nearby', 'cardiology', 'suggest', 'doctor']
    knowledgeWords = primary + getAllCityName()

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

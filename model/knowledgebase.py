
from service.cityNameService import *
class knowledge:
    primary = ['ho']
    knowledgeWords = primary+getAllCityName()
    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

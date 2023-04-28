from service.cityNameService import *

class Knowledge:
    primary = ['hospital', 'doctor']
    citys = getAllCityName()
    gestureWords = ['hi','hello','hlw',"what's up"]
    preps=['near me', 'near by']
    knowledgeWords = primary + citys+gestureWords+preps



    def ct(self):
        return self.citys

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

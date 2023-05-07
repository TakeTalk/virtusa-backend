from service.cityNameService import *


class Knowledge:
    primary = ['hospital', 'doctor', 'my', 'location', 'area', 'clinic','me']
    cities = getAllCityName()
    gestureWords = ['hi', 'hello', 'hlw', "what's up", 'hey', 'how are you']
    preps = ['near', 'around', 'here']
    appointment = ['appointment', 'book']
    hospital = ['apollo']
    knowledgeWords = primary + cities + gestureWords + appointment + hospital + preps

    def ct(self):
        return self.cities

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

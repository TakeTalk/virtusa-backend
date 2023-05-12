from service.cityNameService import *


class Knowledge:
    primary = ['hospital', 'doctor', 'my', 'location', 'area', 'clinic', 'me']
    cities = getAllCityName()
    gestureWords = ['hi', 'hello', 'hlw', 'hey']
    preps = ['near', 'around', 'here', 'nearest']
    leaving = ['bye', 'good']
    unexpected = ['what', 'name', 'who', 'yourself', 'your', 'you']
    greetUser = ['thank', 'you']
    appointment = ['appointment', 'book']
    hospital = ['apollo']
    knowledgeWords = primary + cities + gestureWords + appointment + hospital + preps + unexpected + leaving + greetUser

    medicineSigns = {
        'ac': "before meals",
        'bid': "twice a day",
        'gt': "drop",
        'hs': "at bedtime",
        'od': "right eye",
        'os': "left eye",
        'po': "by mouth",
        'pc': "after meals",
        'prn': "as needed",
        'q3h': "every three hours",
        'qd': "every day",
        'qid': "four times a day",
        'tid': 'three times a day',
        'tab': 'tablet',
        's.o.s.': 'if there is a need',
        'cap': 'capsule',
        'caps': 'capsule',
        'cf': 'with food',
        'tablet': 'tablet',
        'syp': 'syrup',
        'syrup': 'syrup',
        'ors': 'orsl',
        't.d.s': 'three times a day',
        'tds': 'three times a day',
        'q6h': 'every 6 hours',
        'sd': 'subdermal',
        's.d.': 'subdermal'
    }
    medicineTime = {
        'ac': "before meals",
        'bid': "twice a day",
        'gt': "drop",
        'hs': "at bedtime",
        'od': "right eye",
        'os': "left eye",
        'po': "by mouth",
        'pc': "after meals",
        'prn': "as needed",
        'q3h': "every three hours",
        'qd': "every day",
        'qid': "four times a day",
        'tid': 'three times a day',
        'sos': 'if there is a need',
        '505': 'if there is a need',
        'cf': 'with food',
        't.d.s': 'three times a day',
        'tds': 'three times a day',
        'q6h': 'every 6 hours',
    }

    def ct(self):
        return self.cities

    def getKnowledgeBaseWords(self):
        return self.knowledgeWords

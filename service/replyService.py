from service.TokenizeService import *
from service.UserService import *
from model.knowledgebase import *
from collections import defaultdict


knowledge = Knowledge()


def replyMessage(sentence, email):
    userName = getNameByEmail(email)
<<<<<<< HEAD
    getWords = tokenize(sentence)
    userLocation = getLocationByEmail(email)
=======
    getWords = tokenize(sentence);
    data = defaultdict(list)
>>>>>>> ee242c98b15083210fd9c522582906e1181ad224

    ans=[]
    greet = 'greeting'
    rslt = 'reasult'
    for word in getWords:
        if word in knowledge.gestureWords:
            data[greet]= f'Hello {userName}!!'
        if word in knowledge.citys:
<<<<<<< HEAD
            ans.append(fetch(word))
        if word in knowledge.preps:
            ans.append((fetchByLatLong(userLocation[0],userLocation[1])))
=======
            data[rslt] = fetch(word)
    ans.append(data)
>>>>>>> ee242c98b15083210fd9c522582906e1181ad224
    return ans



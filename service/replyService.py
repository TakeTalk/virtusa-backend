from service.TokenizeService import *
from service.UserService import *
from model.knowledgebase import *
from collections import defaultdict


knowledge = Knowledge()


def replyMessage(sentence, email):
    userName = getNameByEmail(email)
    getWords = tokenize(sentence);
    data = defaultdict(list)

    ans=[]
    greet = 'greeting'
    rslt = 'reasult'
    for word in getWords:
        if word in knowledge.gestureWords:
            data[greet]= f'Hello {userName}!!'
        if word in knowledge.citys:
            data[rslt] = fetch(word)
    ans.append(data)
    return ans



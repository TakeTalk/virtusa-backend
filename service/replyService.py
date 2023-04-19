from service.TokenizeService import *
from service.UserService import *
from model.knowledgebase import *

knowledge = Knowledge()


def replyMessage(sentence, email):
    userName = getNameByEmail(email)
    getWords = tokenize(sentence);

    ans=[]

    for word in getWords:
        if word in knowledge.gestureWords:
            ans.append( f'Hello {userName}!!')
        if word in knowledge.citys:
            ans.append(fetch(word))
    return ans



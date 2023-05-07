from service.TokenizeService import *
from service.UserService import *
from model.knowledgebase import *
from collections import defaultdict
from service.AppointmentService import *
from service.unknownService import *

knowledge = Knowledge()


def replyMessage(sentence, email):
    userName = getFirstNameByEmail(email)
    getWords = tokenize(sentence.lower())
    data = defaultdict(list)

    ans = []
    greet = 'greeting'
    leave ='exit'
    doc='this is me'
    sgst = 'hospital suggestion'

    if 'hospital' in getWords:
        for word in getWords:
            if word in knowledge.citys:
                data[sgst] = getHospitalSuggestionByAddress(word)
            if word in knowledge.preps:
                data[sgst] = getHospitalSuggestionNearby(email)
    if 'book' in getWords:
        if 'appointment' in getWords:
            getApolloAppointment(email)
            data['appointment'] = "Appointment booked, you will get a call shortly from Apollo Hospital."

    if 'bye' in getWords:
        data['bye'] =f'good bye {userName}!'


    '''
    for w in getWords:
        if w == 'bye':
            data[leave]=f'good bye {userName}!'
        if w in knowledgeWords.unexpected:
            data[leave]= "my pleasure"
    '''


    for w in getWords:
        if w in knowledgeWords.unexpected:
            data[doc]="I am proton !"

    for word in getWords:
        if word in knowledge.gestureWords:
            data[greet] = f'Hello {userName} ! How can I assist you today?'

    if data == {}:
        # data['not found'] = emotion(sentence)
        data['not found'] = 'sorry'

    ans.append(data)
    return ans

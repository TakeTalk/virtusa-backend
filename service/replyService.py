from service.TokenizeService import *
from service.UserService import *
from model.knowledgebase import *
from collections import defaultdict
from service.AppointmentService import *
from service.unknownService import *

knowledge = Knowledge()


def replyMessage(sentence, email):
    userName = getFirstNameByEmail(email)
    # UserPhone = getPhoneByEmail(email)
    getWords = tokenize(sentence.lower());
    data = defaultdict(list)

    ans = []
    greet = 'greeting'
    sgst = 'hospital suggestion'
    for word in getWords:
        if word in knowledge.gestureWords:
            data[greet] = f'Hello {userName} ! How can I assist you today?'
        if word in knowledge.citys:
            data[sgst] = fetch(word)
        if word in knowledge.preps:
            data[sgst] = fetchByLatLong(word)
        if word in knowledge.appo:
            getApolloAppointment(email)
            data['appointment'] = "Appointment booked, you will get a call shortly from Apollo Hospital."

    if data == {}:
        data['not found'] = emotion(sentence)

    ans.append(data)
    return ans

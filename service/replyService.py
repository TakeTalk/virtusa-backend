from service.TokenizeService import *
from service.UserService import *
from model.knowledgebase import *
from collections import defaultdict
from service.AppointmentService import *
from service.unknownService import *

knowledge = Knowledge()


def replyMessage(sentence, email):
    userName = getFirstNameByEmail(email)
    phone = getPhoneByEmail(email)
    getWords = tokenize(sentence.lower())
    data = defaultdict(list)

    ans = []
    greet = 'greeting'
    suggest = 'hospital suggestion'
    leave ='exit'
    doc='this is me'
    sgst = 'hospital suggestion'

    if 'hospital' in getWords or 'doctor' in getWords or 'clinic' in getWords:
        for word in getWords:
            if word in knowledge.cities:
                data[suggest] = getHospitalSuggestionByAddress(word)
        if 'here' in getWords:
            data[suggest] = getHospitalSuggestionNearby(email)

        if 'near' in getWords or 'around' in getWords:
            if 'me' in getWords:
                data[suggest] = getHospitalSuggestionNearby(email)

        if 'my' in getWords:
            if 'location' in getWords:
                data[suggest] = getHospitalSuggestionNearby(email)
            if 'area' in getWords:
                data[suggest] = getHospitalSuggestionNearby(email)

    if 'book' in getWords:
        if 'appointment' in getWords:
            getApolloAppointment(email)
            data[
                'appointment'] = f"Congratulations !! Your appointment is successfully booked to Appolo Hospital.Hospital representative will call you at {phone} shortly."

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
        data['not found'] = emotion(sentence)
        # data['not found'] = 'sorry'

    ans.append(data)
    return ans

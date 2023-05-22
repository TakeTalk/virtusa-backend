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
    leave = 'exit'
    doc = 'this is me'

    if 'hospital' in getWords or 'doctor' in getWords or 'clinic' in getWords:
        for word in getWords:
            if word in knowledge.cities:
                data[suggest] = getHospitalSuggestionByAddress(word)
        if 'here' in getWords:
            data[suggest] = getHospitalSuggestionNearby(email)

        if 'near' in getWords or 'around' in getWords:
            if 'me' in getWords:
                data[suggest] = getHospitalSuggestionNearby(email)
        if 'nearest' in getWords:
            data[suggest] = getHospitalSuggestionNearby(email)

        if 'my' in getWords:
            if 'location' in getWords:
                data[suggest] = getHospitalSuggestionNearby(email)
            if 'area' in getWords:
                data[suggest] = getHospitalSuggestionNearby(email)

    if 'book' in getWords:
        if 'appointment' in getWords:
            getApolloAppointment(email)
            updatePoint(email, 100)
            data[
                'appointment'] = f"Congratulations !! Your appointment is successfully booked to Appolo Hospital. You wll recieve a call within 15 mins from +918045-305-263."

    if 'bye' in getWords:
        data[leave] = f'Good bye {userName}!, see you soon! :)'

    if 'thank' in getWords:
        if 'you' in getWords:
            data[leave] = "As a good doctor, it is my duty to help you , to understand you 😊."

    if 'about' in getWords:
        if 'yourself' in getWords:
            data[
                doc] = "Hey there! I am proton . Ah, it was a long process. 3 genius guys .. Oops 😐 sorry 5 genius guys made me this much capable to handle heavy task. I am very thankful to them."
        if 'you' in getWords:
            data[
                doc] = "Hey there! I am proton . Ah, it was a long process. 3 genius guys .. Oops 😐 sorry 5 genius guys made me this much capable to handle heavy task. I am very thankful to them."
        if 'your' in getWords:
            data[
                doc] = "Hey there! I am proton . Ah, it was a long process. 3 genius guys .. Oops 😐 sorry 5 genius guys made me this much capable to handle heavy task. I am very thankful to them."

    if 'who' in getWords:
        if 'you' in getWords:
            data[
                doc] = "Hey there! I am proton . Ah, it was a long process. 3 genius guys .. Oops 😐 sorry 5 genius guys made me this much capable to handle heavy task. I am very thankful to them."

    for word in getWords:
        if word in knowledge.gestureWords:
            data[greet] = f'Hello {userName} ! How can I assist you today?'

    if data == {}:
        data['not found'] = emotion(sentence)
        # data['not found'] = 'sorry'

    ans.append(data)
    return ans

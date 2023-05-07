from Connection import *
from service.ChatService import addChat

userCollection = database['userDetails']


def signInUser(userDetails):
    try:
        query = {"email": userDetails["email"]}
        existingUser = userCollection.find_one(query)
        if existingUser is None:
            userCollection.insert_one(userDetails)
            addChat(userDetails["email"])
            return userDetails
        else:
            updatedLocation = {
                "$set": {"location_lat": userDetails['location_lat'], "location_long": userDetails['location_long']}}
            userCollection.update_one(query, updatedLocation)
            return userCollection.find_one(query)
    except:
        print('something went wrong')


def getNameByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return existingUser['name']


def getFirstNameByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    name = existingUser['name']
    firstName = ''
    for n in name:
        if n != ' ':
            firstName += n
        else:
            break
    return firstName


def getPhoneByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return existingUser['phone']


def getLocationByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    location = [existingUser['location_lat'], existingUser['location_long']]
    return location

from Connection import *
from model.userOrganModel import UserOrganStatus

from service.ChatService import addChat
from service.UserOrganService import addHealth

userCollection = database['userDetails']



def signInUser(userDetails):
    try:
        query = {"email": userDetails["email"]}
        existingUser = userCollection.find_one(query)
        if existingUser is None:
            userCollection.insert_one(userDetails)
            addChat(userDetails["email"])
            addHealth(userDetails["email"])

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


def editPhone(email, phone):
    query = {"email": email}
    existingUser = userCollection.find_one(query)
    updatedPhone = {
        "$set": {"phone": phone}}
    userCollection.update_one(query, updatedPhone)
    return userCollection.find_one(query)


def updatePoint(email, point):
    query = {"email": email}
    existingUser = userCollection.find_one(query)
    updatedPoints = {
        "$set": {"rewardsPoints": point}}
    userCollection.update_one(query, updatedPoints)
    return userCollection.find_one(query)


def getPoint(email):
    query = {"email": email}
    user = userCollection.find_one(query)
    return user['rewardsPoints']


def getPhoneByMail(email):
    query = {"email": email}
    existingUser = userCollection.find_one(query)
    if existingUser is not None:
        return existingUser['phone']
    else:
        return None

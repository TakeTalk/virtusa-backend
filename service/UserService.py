from Connection import *

userCollection = database['userDetails']


def signInUser(userDetails):
    try:
        existingUser = userCollection.find_one({"email": userDetails["email"]})
        if existingUser is None:
            userCollection.insert_one(userDetails)
            return userDetails
        else:
            return existingUser
    except:
        print('something went wrong')


def getNameByEmail(email):
    existingUser = userCollection.find_one({"email": email})
    return existingUser['name']

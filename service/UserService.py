from Connection import *


userCollection = database['userDetails']


def signupUser(userDetails):

    try:
        existingUser = userCollection.find_one({"email": userDetails["email"]})
        if existingUser is None:
            userCollection.insert_one(userDetails)
            return userDetails
        else:
            return 'User exists'
    except:
        print('something went wrong')





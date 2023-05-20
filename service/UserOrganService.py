import json

from Connection import *

healthCollection = database['userHealth']


def addHealth(email: str):
    healthCollection.insert_one({'email': email})


def updateHealth(userHealth, email):
    query = {'email': email}
    userHealthDetails = dict(userHealth)
    healthCollection.update_one(query, {"$set": userHealthDetails})
    currentHealth = healthCollection.find_one(query)
    return getInsurance(currentHealth)


def getInsurance(userHealth):
    insurance = []
    if userHealth['brain']:
        tempIns = ['Get 10% Off at Insurance on Brain', 2000, 'test']
        insurance.append(tempIns)

    return insurance


def getUserHealth(email):
    userChat = healthCollection.find_one({'email': email})
    return userChat

import json

from Connection import *

healthCollection = database['userHealth']
insuranceCollection = database['insuranceSuggestion']


def addHealth(email: str):
    healthCollection.insert_one({'email': email})


def updateHealth(userHealth, email):
    query = {'email': email}
    userHealthDetails = dict(userHealth)
    healthCollection.update_one(query, {"$set": userHealthDetails})
    currentHealth = healthCollection.find_one(query)
    return getInsurance(currentHealth)


def getInsurance(userHealth):
    insuranceSuggestion = []
    if userHealth['brain']:
        cursor = insuranceCollection.find({"organ": "brain"})
        insuranceSuggestion = getInsuranceSuggestion(cursor, insuranceSuggestion)

    if userHealth['heart']:
        cursor = insuranceCollection.find({"organ": "heart"})
        insuranceSuggestion = getInsuranceSuggestion(cursor, insuranceSuggestion)

    if userHealth['kidney']:
        cursor = insuranceCollection.find({"organ": "kidney"})
        insuranceSuggestion = getInsuranceSuggestion(cursor, insuranceSuggestion)

    if userHealth['lungs']:
        cursor = insuranceCollection.find({"organ": "lungs"})
        insuranceSuggestion = getInsuranceSuggestion(cursor, insuranceSuggestion)

    if userHealth['liver']:
        cursor = insuranceCollection.find({"organ": "liver"})
        insuranceSuggestion = getInsuranceSuggestion(cursor, insuranceSuggestion)

    if userHealth['bone']:
        cursor = insuranceCollection.find({"organ": "bone"})
        insuranceSuggestion = getInsuranceSuggestion(cursor, insuranceSuggestion)

    return insuranceSuggestion


def getInsuranceSuggestion(cursor, insuranceSuggestion):
    for insurance in cursor:
        tempIns = [insurance['title'], insurance['coin'], insurance['image']]
        insuranceSuggestion.append(tempIns)
    return insuranceSuggestion


def getUserHealth(email):
    userChat = healthCollection.find_one({'email': email})
    return userChat

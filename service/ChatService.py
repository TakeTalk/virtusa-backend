import json

from Connection import *

chatCollection = database['chatDetails']


def addChat(email):
    chat = {'email': email, 'history': []}
    chatCollection.insert_one(chat)


def updateChat(chatModel, email):
    query = {'email': email}
    chatHistory = dict(chatModel)
    chatCollection.update_one(query, {'$push': {'history': chatHistory}})
    return chatCollection.find_one(query)


def getChat(email):
    userChat = chatCollection.find_one({'email': email})
    return userChat['history']

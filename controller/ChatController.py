from config import *

from service.ChatService import *

from model.ChatModel import ChatModel

from bson import json_util
import json


@app.get("/getChat/{email}")
def getChatByEmail(email: str):
    return getChat(email)


@app.put("/updateChat/{email}")
def updateChatByEmail(email: str, chat: ChatModel):
    response = updateChat(chat, email)
    json_response = json.loads(json_util.dumps(response))
    return json_response

import app
from config import *
from model.UserModel import UserBody
from service.UserService import *

from bson import json_util
import json


@app.post('/signIn')
def signIn(userBody: UserBody):
    response = signInUser(dict(userBody))
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.put('/updatePhone/{email}/{phone}')
def updatePhone(email: str, phone: str):
    response = editPhone(email, phone)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.get('/getPhone/{email}')
def getPhone(email: str):
    return getPhoneByMail(email)

# @app.post('/addChat')
# def postChat():

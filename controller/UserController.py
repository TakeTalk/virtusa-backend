import app
from config import *
from model.UserModel import UserBody
from service.UserService import *
from service.UserOrganService import *

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


@app.put('/updatePoints/{email}/{points}')
def updateRewards(email: str, points: int):
    response = updatePoint(email, points)
    json_response = json.loads(json_util.dumps(response))
    return json_response


@app.get('/getPoints/{email}')
def getRewards(email: str):
    return getPoint(email)


@app.get('/getPhone/{email}')
def getPhone(email: str):
    return getPhoneByMail(email)


@app.put('/updateHealth/{email}')
def updatePhone(email: str, userHealth: UserOrganStatus):
    response = updateHealth(userHealth, email)
    json_response = json.loads(json_util.dumps(response))
    return json_response

# @app.post('/addChat')
# def postChat():

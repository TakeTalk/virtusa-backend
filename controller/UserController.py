from config import *
from model.UserModel import UserBody
from service.UserService import *

from bson import json_util
import json


@app.post('/signIn')
def signIn(userBody : UserBody):
    response = signInUser(dict(userBody))
    json_response = json.loads(json_util.dumps(response))
    return json_response

from config import *
# from pydantic import BaseModel
from model.UserModel import UserBody
from service.UserService import *


@app.post('/signUp')
def signUp(item:UserBody):
    signupUser(dict(item))


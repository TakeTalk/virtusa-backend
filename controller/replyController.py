from config import *

from service.replyService import *


@app.get("/reply/{email}/{sentence}")
def reply(email:str,sentence:str):
    return replyMessage(sentence, email)

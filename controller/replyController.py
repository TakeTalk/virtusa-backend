from config import *

from service.replyService import *


@app.get("/reply")
def reply(sentence, email):
    return replyMessage(sentence, email)

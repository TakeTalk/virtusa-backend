from config import *

from service.replyService import *
from service.ImageToText import *
from fastapi import UploadFile


@app.get("/reply/{email}/{sentence}")
def reply(email: str, sentence: str):
    return replyMessage(sentence, email)


@app.post("/medicineDetect/{email}/{timeStamp}")
async def create_upload_file(file: UploadFile, email: str, timeStamp: str):
    return detect_text(file, email, timeStamp)

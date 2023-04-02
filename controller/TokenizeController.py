from config import *
from service.TokenizeService import *

@app.get("/test")
def test(sentence):
    return tokenize(sentence)
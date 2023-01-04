from flask import Flask
import knowldgeBase
from pymongo import MongoClient
import random
import json


app = Flask(__name__)

def parse_json(data):
    return json.loads(json.dumps(data))

@app.route('/bot-reply/<text>')
def reply(text):
    t=text.lower()
    if(t in knowldgeBase.greetings[0]):
        return random.choice(knowldgeBase.greetings[1])
    if(t in knowldgeBase.thanks[0]):
        return knowldgeBase.thanks[1]
    if(t in knowldgeBase.sorry[0]):
        return knowldgeBase.sorry[1]
    else:
        return "I am sorry! I don't understand you"
@app.route('/connect-db')
def connect():
    client = MongoClient("mongodb://ec2-43-204-130-213.ap-south-1.compute.amazonaws.com/?directConnection=true")
    db = client["virtusa"]
    col=db["hospitalDetails"]

    datas=col.find_one()
    return parse_json(datas)
    # for data in datas:
    #     return (data)

if(__name__=='__main__'):
    app.run(port=4000)
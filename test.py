from flask import Flask
from pymongo import MongoClient
import json
app = Flask(__name__)
client = MongoClient("mongodb://ec2-43-204-130-213.ap-south-1.compute.amazonaws.com/?directConnection=true")
db = client["virtusa"]
col=db["hospitalDetails"]
def fetch_data():
    datas=col.find()
    for data in datas:
        return (data)
    client.close()
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@app.route('/')
def hello_world():
    JSONEncoder().encode(fetch_data())
    

if __name__ == '__main__':
    app.run()
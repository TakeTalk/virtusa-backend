from pymongo import MongoClient

try:
    client = MongoClient("mongodb://ec2-43-204-171-36.ap-south-1.compute.amazonaws.com:27017")
    database = client['proton']
    print('connection successfully')
except: 
    print('connection fail')

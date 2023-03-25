import sys
from fastapi import FastAPI
import uvicorn
sys.path.append('C:/Users/anikd/virtusa-bot/service') 
from location import *

app = FastAPI()
 
@app.get('/suggest-hospital-by-address/')
def getSuggestionByLocation(address):
    return fetch(address)

@app.get('/suggest-hospital-by-latlong')
def getSuggestionByLatLong(lat,longt):
    return fetchByLatLong(lat,longt)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000)

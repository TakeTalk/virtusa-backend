import sys
from fastapi import FastAPI
import uvicorn

from service.location import *

app = FastAPI()
 
@app.get('/suggest-hospital-by-address/')
def getSuggestionByLocation(address):
    return fetch(address)

@app.get('/suggest-hospital-by-latlong')
def getSuggestionByLatLong(lat,longt):
    return fetchByLatLong(lat,longt)

def runApplication():
    uvicorn.run(app, host='127.0.0.1', port=5000)


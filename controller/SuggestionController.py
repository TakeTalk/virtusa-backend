from config import *

from service.LocationService import *

@app.get('/suggest-hospital-by-address/')
def getSuggestionByLocation(address):
    return fetch(address)


@app.get('/suggest-hospital-by-latlong/{lat}/{longt}')
def getSuggestionByLatLong(lat:str, longt:str):
    return fetchByLatLong(lat, longt)


from config import *

from service.LocationService import *

@app.get('/suggest-hospital-by-address/')
def getSuggestionByLocation(address):
    return fetch(address)


@app.get('/suggest-hospital-by-latlong')
def getSuggestionByLatLong(lat, longt):
    return fetchByLatLong(lat, longt)


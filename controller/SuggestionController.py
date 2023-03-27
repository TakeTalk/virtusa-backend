from service.LocationService import *

from config import *

@app.get('/suggest-hospital-by-address/')
def getSuggestionByLocation(address):
    return fetch(address)


@app.get('/suggest-hospital-by-latlong')
def getSuggestionByLatLong(lat, longt):
    return fetchByLatLong(lat, longt)


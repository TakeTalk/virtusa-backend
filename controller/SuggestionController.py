from config import *

from service.LocationService import *


@app.get('/suggest-hospital-by-address/')
def getSuggestionByLocation(address):
    return getHospitalSuggestionByAddress(address)


@app.get('/suggest-hospital-by-latlong/{email}')
def getSuggestionByLatLong(email: str):
    return getHospitalSuggestionNearby(email)

import threading
from concurrent.futures import ThreadPoolExecutor

import requests
from operator import itemgetter

from service.UserService import *

from Connection import *

hospitalCollection = database['hospital']


def lat_solve(adr):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={adr}&key=AIzaSyDlFsW1aC6dcvXX7mZp_jpF1pMOqfy2ETs"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json_response = response.json()
    repository1 = json_response["results"][0]["geometry"]["location"]["lat"]
    repository2 = json_response["results"][0]["geometry"]["location"]["lng"]

    loc = [repository1, repository2]
    return loc


def nearby(location_lat, location_long):
    range = 7000
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location_lat},{location_long}&radius={range}&types=hospital|health&keyword=best&key=AIzaSyDlFsW1aC6dcvXX7mZp_jpF1pMOqfy2ETs"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()

    result = json_response["results"]

    return result


def createLink(lat, lng):
    mapLink = f"https://www.google.com/maps/place/{lat}+{lng}"
    return mapLink


def fetch(location_lat, location_long):
    total = []
    t1 = threading.Thread(target=total.append(nearby(location_lat, location_long)), args=(10,))
    t1.start()
    t1.join()

    total = total[0]

    name = []

    i = 0

    limit = 0

    if len(total) >= 5:
        limit = 5
    else:
        limit = len(total)

    while len(name) < limit:

        if total[i]["business_status"] == "OPERATIONAL":
            loc = [total[i]["geometry"]["location"]['lat'], total[i]["geometry"]["location"]['lng']]
            loc_link = createLink(loc[0], loc[1])
            temp = {'name': total[i]["name"], 'vicinity': total[i]["vicinity"], 'rating': total[i]["rating"],
                    'link': loc_link}
            name.append(temp)

            i += 1
    return name


def getHospitalSuggestionByAddress(adr):
    existingHospital = hospitalCollection.find_one({'address': adr})
    if existingHospital is not None:
        return existingHospital['hospital']
    else:
        location = lat_solve(adr)
        hospital = fetch(location[0], location[1])

        hospitalDetails = {'address': adr, 'hospital': hospital}

        hospitalCollection.insert_one(hospitalDetails)

        return hospital


def getHospitalSuggestionNearby(email):
    location = getLocationByEmail(email)
    return fetch(location[0], location[1])

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=lodging&key=API_KEY'

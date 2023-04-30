import requests
from operator import itemgetter


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


def nearby(adr):
    range = 2000
    result = []
    while len(result) < 9:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat_solve(adr)[0]},{lat_solve(adr)[1]}&radius={range}&types=hospital|health&keyword=best&key=AIzaSyDlFsW1aC6dcvXX7mZp_jpF1pMOqfy2ETs"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.json()
        result = json_response["results"]
        range = range + 1000

    return result


def nearbyLatLong(lat, longt):
    range = 2000
    result = []
    while len(result) < 9:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{longt}&radius={range}&types=hospital|health&keyword=best&key=AIzaSyDlFsW1aC6dcvXX7mZp_jpF1pMOqfy2ETs"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.json()
        result = json_response["results"]
        range = range + 1000

    return result


def createLink(lat, lng):
    mapLink = f"https://www.google.com/maps/place/{lat}+{lng}"
    return mapLink


def fetch(adr):
    total = nearby(adr)
    print(len(total))
    total = sorted(total, key=itemgetter('rating'), reverse=True)  # sorting a list of dict by one value which is rating
    name = []
    i = 0
    while (len(name) < 5):
        if (total[i]["business_status"] == "OPERATIONAL"):
            loc = [total[i]["geometry"]["location"]['lat'], total[i]["geometry"]["location"]['lng']]
            loc_link = createLink(loc[0], loc[1])
            temp = {}
            temp['name'] = total[i]["name"]
            temp['vicinity'] = total[i]["vicinity"]
            temp['rating'] = total[i]["rating"]
            temp['link'] = loc_link
            name.append(temp)
            i += 1
    return name


def fetchByLatLong(lat, longt):
    total = nearbyLatLong(lat, longt)
    print(len(total))
    total = sorted(total, key=itemgetter('rating'), reverse=True)  # sorting a list of dict by one value which is rating
    name = []
    i = 0
    while (len(name) < 5):
        if (total[i]["business_status"] == "OPERATIONAL"):
            loc = [total[i]["geometry"]["location"]['lat'], total[i]["geometry"]["location"]['lng']]
            loc_link = createLink(loc[0], loc[1])
            temp = {}
            temp['name'] = total[i]["name"]
            temp['vicinity'] = total[i]["vicinity"]
            temp['rating'] = total[i]["rating"]
            temp['link'] = loc_link
            name.append(temp)
            i += 1
    return name

# print(fetch("chinsurah"))


# print(nearby("restaurant","siuri"))

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=lodging&key=API_KEY'

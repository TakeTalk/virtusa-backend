from Connection import *

cityCollection = database['allCity']


def getAllCityName():
    allCity = cityCollection.find({})
    allCityList = []
    for city in allCity:
        allCityList.append(city.get('city').lower())
    return allCityList

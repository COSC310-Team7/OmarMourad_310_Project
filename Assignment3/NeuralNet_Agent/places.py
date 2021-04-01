#Google Places API to access directory information and display them in a meaningful way

# import googlemaps

import requests

#api key in local file 
api_file = open("C:/Users/droga/Desktop/UBCO/COSC minor/COSC 310/Assignments/API keys/places_api_key.txt", "r")
api_key = api_file.read()
api_file.close()
# client = googlemaps.Client(key)


def findPlace(text):
    global api_key
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    fields = "formatted_address,name,opening_hours,rating"
    #get response
    r = requests.get(url + text + "&inputtype=textquery&fields=" + fields + "&key=" + api_key)

    #organize and store data to return
    address = r.json()["candidates"][0]["formatted_address"]
    name = r.json()["candidates"][0]["name"]
    hours = r.json()["candidates"][0]["opening_hours"]
    rating = r.json()["candidates"][0]["rating"]

    final = address + "\n" +  name + "\n" + str(hours) + "\n" + str(rating) + " star(s)"
    # print(final)

    return final


print(findPlace("Boston Pizza"))

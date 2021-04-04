#This file gets the directions between 2 points but ignores traffic and road activity
#It also gets the fastest/most common route between 2 points - sticking to the first route

import requests
import re #to clean up HTML instructions

#api key hidden in a local file
api_file = open("C:/Users/droga/Desktop/UBCO/COSC minor/COSC 310/Assignments/API keys/directions_api_key.txt", "r")
api_key = api_file.read()
api_file.close()

def getDirections(org, dest, mode):
    global api_key
    url = "https://maps.googleapis.com/maps/api/directions/json?origin="
    origin = org
    destination = dest

    #get response
    if mode == "walking" or mode == "transit" or mode == "bicycling" or mode =="driving":
        r = requests.get(url + origin + "&destination=" + destination + "&mode=" + mode +  "&key=" + api_key) 
    else:
        r = requests.get(url + origin + "&destination=" + destination + "&key=" + api_key)

    distance = r.json()["routes"][0]["legs"][0]["distance"]["text"]
    duration = r.json()["routes"][0]["legs"][0]["duration"]["text"]
    summary = r.json()["routes"][0]["summary"]
    travelMode = r.json()["routes"][0]["legs"][0]["steps"][0]["travel_mode"]

    #steps sort:
    steps = r.json()["routes"][0]["legs"][0]["steps"]
    i = 0
    instruction = "\n"
    for item in steps:
        instruction += "Step " + str(i) + ") " + cleanhtml(r.json()["routes"][0]["legs"][0]["steps"][i]["html_instructions"]) + " - DISTANCE: " + r.json()["routes"][0]["legs"][0]["steps"][i]["distance"]["text"] + "\n"
        i += 1


    final = "Distance: " + distance + " - Duration: " + duration + " - Mode: " + travelMode + " - Via: " + summary + instruction
    return final

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# print(getDirections("Kelowna BC", "Vernon BC", "walking"))


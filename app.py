import requests
import datetime
from pprint import pprint 

time = datetime.date.today()

url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/EDDS/{time}T08:00/{time}T20:00"

querystring = {"withLeg":"false","direction":"Both","withCancelled":"true","withCodeshared":"true","withCargo":"true","withPrivate":"true","withLocation":"false"}

headers = {
	"X-RapidAPI-Key": "57e40df905msh89f91a584028707p1724bfjsn063fbf3c8395",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.json())
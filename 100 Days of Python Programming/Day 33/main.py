# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
# print(iss_position)

import requests

MY_LAT = 7.226350
MY_LNG = 80.609110
FORMATTED_TIME = 0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": FORMATTED_TIME
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


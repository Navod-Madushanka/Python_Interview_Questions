import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "962934a493a95c3b3b7a39a9a36ad665"

weather_params = {
    "lat": 7.2955,
    "lon": 80.6356,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
print(response.status_code)
data = response.json()

if data["weather"][0]["id"]<700:
    print("Bring an Umbrella")
else:
    print("Do not bring an Umbrella")

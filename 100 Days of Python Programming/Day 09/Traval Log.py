travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_Dictionary = {}
    new_Dictionary["country"] = country
    new_Dictionary["visits"] = visits
    new_Dictionary["cities"] = cities
    travel_log.append(new_Dictionary)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
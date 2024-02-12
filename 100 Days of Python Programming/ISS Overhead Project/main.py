import requests
from datetime import datetime
import smtplib
import time
import schedule

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
my_email = "navodmaithripala@gmail.com"
password = "idwrxesqvzuzobmc"


def location_check():
    if MY_LAT == iss_latitude and MY_LONG == iss_longitude:
        return True
    return False


def time_check():
    if time_now > sunset:
        return True
    return False


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
def send_email():
    location_ok = location_check()
    time_ok = time_check()

    if location_ok and time_ok:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="navodmaithripala@yahoo.com",
                                msg=f"Subject:ISS Position\n\nLook up Now")


schedule.every(60).seconds.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)

# BONUS: run the code every 60 seconds.

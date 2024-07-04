import requests
from datetime import datetime
import time

# MY_LAT = 15.507351 # Your latitude
# MY_LONG = -140.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


MY_LAT = iss_latitude # change to latitude below
MY_LONG = iss_longitude # change to longitude below

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": 37.839149,
    "lng": -94.355278,
    "formatted": 0,
    "tzid": "America/Chicago" 
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(iss_latitude)
print(iss_longitude)

print(sunrise)
print(sunset)

print(time_now.hour)
#If the ISS is close to my current position

while True:
    time.sleep(60)
    if iss_latitude >= MY_LAT -5 and iss_latitude <= MY_LAT +5:
        if iss_longitude >= MY_LONG -5 and iss_longitude <= MY_LONG +5:
            if time_now.hour >= sunset or time_now.hour <= sunrise:
                print("Email Sent")
            else: 
                print("It is not night time")
        else:
            print("Longitude is too far off")
    else:
        print("Latitude is too far off.")


# and it is currently dark


# Then send me an email to tell me to look up.


# BONUS: run the code every 60 seconds.





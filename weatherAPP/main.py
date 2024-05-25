import requests
import smtplib
from datetime import datetime


#following are environment variables these files should be confidential
# import os
# import requests
# import smtplib
# from datetime import datetime
#
# MY_EMAIL = os.getenv("MY_EMAIL")
# MY_PWD = os.getenv("MY_PWD")
# API_KEY = os.getenv("API_KEY")
#

MY_EMAIL = "akinduscience@gmail.com"
MY_PWD = "yqma fvmg kpcp dr"
today = datetime.today()

MY_API = "https://api.openweathermap.org/data/2.5/forecast"
MY_CITY = "Colombo"
API_KEY= "d176a14e7940922b7e4645c0759a150b"

MY_POS = {
    "lat": 6.9763072,
    "lon": 79.95392,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(MY_API, params=MY_POS)
response.raise_for_status()
data = response.json()

# weather_condition = data["list"][0]["weather"][0]
# print(weather_condition)

will_rain = False
for hour_data in data["list"]:
    #tapping into the json data which came as list
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PWD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="akindukodithuwakku@gmail.com",
                            msg=f"subject:Bad Weather ALERT!"
                                 f"\n\n {today} \nTake an Umbrella before go outside.\n"
                                f"Expected precipitation during the day time. "
                                 f"\nGood Luck Warrior!")
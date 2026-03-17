import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = "53.219383"
MY_LONG = "6.566502"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)
response.raise_for_status()
weather_data = response.json()['list']
# print(weather_data[0]['weather'][0]['id'])

weather_id = [weather_data[value]['weather'][0]['id'] for value in range(0, len(weather_data))]
for id in weather_id:
    if id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="It's going to rain today. Remember to bring an ☔️",
            to="whatsapp:+919987674266",
        )
        print(message.status)
        break


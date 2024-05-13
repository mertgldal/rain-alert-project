import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.getenv('OWM_API_KEY')
latitude = os.getenv('MY_HOME_LAT')
longitude = os.getenv('MY_HOME_LON')

weather_params = {
    "appid": api_key,
    "lat": latitude,
    "lon": longitude,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)

response.raise_for_status()
data = response.json()

send_sms = False

for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    # print(condition_code)
    if condition_code < 600:
        send_sms = True


if send_sms:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today.\nRemember to bring an ☔.",
                                     from_=os.getenv('TWILIO_PHONE_NUM'),
                                     to=os.getenv('MY_PHONE_NUM')
                                     )
    print(message.status)

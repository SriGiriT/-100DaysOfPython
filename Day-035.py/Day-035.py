import requests
import os
from twilio.rest import Client
# Download the helper library from https://www.twilio.com/docs/python/install
account_sid = str(os.environ.get("ACCOUNT_SID_API_RAIN"))
auth_token = str(os.environ.get("AUTH_TOKEN_API_RAIN"))

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a32b69bbc19768392e3300707d316519"
weather_params = {
  "lat":15.621332,
  "lon":120.019192,
  "appid": api_key,
  "exclude":"current,minutely,daily,alerts"
}
response = requests.get(OWN_Endpoint, params=weather_params)
data = response.json()
weather_slice = data["hourly"][:12]
list_weather_id = [i["weather"][0]["id"] for i in weather_slice]
print(list_weather_id)
will_rain = False
for i in list_weather_id:
  if i<700:
    will_rain=True

if will_rain:
  client = Client(account_sid, auth_token)
  message = client.messages \
    .create(
      body="It's going to rain today, Remember to bring an umbrella",
      from_="+17692091254",
      to="+919344953235"
    )
  print(message.status)
# print(data)
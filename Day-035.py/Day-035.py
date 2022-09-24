from urllib import response
import requests
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a32b69bbc19768392e3300707d316519"
weather_params = {
  "lat":10.958118,
  "lon":76.954951,
  "appid": api_key
}
response = requests.get(OWN_Endpoint, params=weather_params)
print(response.json())
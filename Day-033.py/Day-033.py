import time
import smtplib
import requests
import datetime as dt



current_position = (76.959057, 10.995325)

def is_iss_overhead():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()
  iss_position = (float(data["iss_position"]["longitude"]), float(data["iss_position"]["latitude"]))
  print(iss_position)
  if current_position[0]-5 <= iss_position[0] <= current_position[0]+5 and  current_position[1]-5 <= iss_position[1] <= current_position[1]+5:
    return True 

def is_night():
  parameters = {
    "lat": 10.995325,
    "lng": 76.959057,
    "formatted": 0
  }

  time = dt.datetime.now().hour
  sunrise_response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
  sunrise_response.raise_for_status()
  sunrise_response_data = sunrise_response.json()
  sunrise = int(sunrise_response_data['results']['sunrise'].split("T")[1].split(":")[0])
  sunset = int(sunrise_response_data['results']['sunset'].split("T")[1].split(":")[0])
  if time>=sunset or time<=sunrise:
    return True

while True:
  time.sleep(60)
  if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login("tsrigiri369@gmail.com", "vwfnrpewaicfpjps")
      connection.sendmail(
        from_addr="tsrigiri369@gmail.com",
        to_addrs="tsrigiri369@gmail.com",
        msg="Subject:Look up👆\n\nThe ISS is above you in the sky."
      )
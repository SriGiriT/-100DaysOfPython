



import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
Token = "G@$3G@$3G@$3G@$3"
Username =  "srigirit"
user_params = {
    "token" : Token,
    "username": Username,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"
"""
id	string	[required] It is an ID for identifying the pixelation graph.
Validation rule: ^[a-z][a-z0-9-]{1,16}
name	string	[required] It is the name of the pixelation graph.
unit	string	[required] It is a unit of the quantity recorded in the pixelation graph. Ex. commit, kilogram, calory.
type	string	[required] It is the type of quantity to be handled in the graph. Only int or float are supported.
color	string	[required] Defines the display color of the pixel in the pixelation graph.
shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.
"""

graph_id = "graph1";
graph_params = {
    "id": graph_id,
    "name": "Coding commit",
    "unit": "times",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN":Token
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{Username}/graphs/{graph_id}"
# date = datetime.now()
date = datetime(year=2022, month=11, day=19)

"""
date	string	[required] The date on which the quantity is to be recorded. It is specified in yyyyMMdd format.
quantity	string	[required] Specify the quantity to be registered on the specified date.
Validation rule: int^-?[0-9]+ float^-?[0-9]+.[0-9]+
optionalData	string	[optional] Additional information other than quantity. It is specified as JSON string.
The amount of this data must be less than 10 KB.
"""
add_pixel_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "500"
}
response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)


# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
date1 = datetime(year=2022, month=11, day=21)
put_pixel_endpoint = f"{pixela_endpoint}/{Username}/graphs/{graph_id}/{date1.strftime('%Y%m%d')}"
put_pixel_params = {
    "quantity": "900"
}
response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
print(response.text)


date2 = datetime(year=2022, month=11, day=22)
delete_pixel_endpoint = f"{pixela_endpoint}/{Username}/graphs/{graph_id}/{date2.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)


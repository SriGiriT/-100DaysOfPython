
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

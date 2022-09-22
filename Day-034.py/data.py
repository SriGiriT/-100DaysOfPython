import requests

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=params)
response_data = response.json()
question_data = response_data['results']

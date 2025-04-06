import requests
from datetime import datetime


USERNAME = "artur"
TOKEN = "sdfjkslkdfjlsdflkjsdflkjsdflkjsf"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "artur",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

#today = datetime.now()
today = datetime(year=2021, month=6, day=5)

graph_params = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How may kilometers did you cycle today?")
}

response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# response = requests.post(url=f"{pixela_graph_endpoint}/{GRAPH_ID}", json=graph_params, headers=headers)
# print(response.text)

# response = requests.put(url=f"{pixela_graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}", json=graph_params, headers=headers)
# print(response.text)

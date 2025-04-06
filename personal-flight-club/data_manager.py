import requests

SHEETY_ENDPOINT = "https://api.sheety.co/52860ba1426629b8e0bf08bc23c0b94a/flightDeals/prices"
SHEETY_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer vwewwRswszzH5i9J0eEl5vvoqoHPp2cA+SZJDuhzKXXK9AulL/az3Q=="
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data


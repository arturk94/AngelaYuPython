import requests
from datetime import datetime

APP_ID = "548f7226"
API_KEY = "dac5ca61f797cfadeaed2b440e83bdb9"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "arturk94"
}

params = {
 "query": input("Tell me which exercises you did today."),
 "gender": "male",
 "weight_kg": 95.0,
 "height_cm": 185.0,
 "age": 47
}


response = requests.post(url=exercise_endpoint, data=params, headers=headers)
data = response.json()["exercises"]


today = datetime.now()
date = datetime.strftime(today, "%d/%m/%Y")
time = datetime.strftime(today, "%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/52860ba1426629b8e0bf08bc23c0b94a/myWorkouts/workouts"
#sheety_endpoint = "https://api.sheety.co/arturk94/workoutTracking/workouts"
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer AAAADJDJDSIdkfhsjkZFDhkjdfhjs=fjhsjhdfjhsss==sjhdjfhjhfd"
}

for exercise in data:
    sheety_params = {
      "workout": {
        "date": date,
        "time": time,
        "exercise": exercise['name'].title(),
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories']
      }
    }
    print(sheety_params)
    response2 = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(response2.text)






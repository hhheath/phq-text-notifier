## Heath Blandford 2022-08-06

import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client
from datetime import date

load_dotenv()

PHQ_TOKEN = os.getenv('PHQ_TOKEN')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUM = os.getenv('TWILIO_PHONE_NUM')
MY_PHONE_NUM = os.getenv('MY_PHONE_NUM')
POI = os.getenv('POI')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

today = date.today()

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": f"Bearer {PHQ_TOKEN}",
      "Accept": "application/json"
    },
    params={
      "limit": 5,
      "start.gte": f"{today}",
      "start.lte": f"{today}",
      "within": f"{POI}",
      "category": "politics,conferences,expos,concerts,festivals,performing-arts,sports,community"
    }
)

events = response.json()

message_body = "Events today: \n\n"

for e in events['results']:
    message_body = message_body + f"{e['title']}, {e['phq_attendance']}\n"  

message = client.messages \
                .create(
                     body=message_body,
                     from_=TWILIO_PHONE_NUM,
                     to=MY_PHONE_NUM
                 )


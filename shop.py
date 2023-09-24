#!/usr/bin/python3
import datetime
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE_NUMBER, TO_PHONE_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

my_weekly_list = [
        'sugar','delmonte','maize floor','milk','mineral water'
        ]

def text_list(lst):
    msg_body = '\n'.join(lst)
    message = client.messages.create(
            from_ = FROM_PHONE_NUMBER,
            body = msg_body,
            to = TO_PHONE_NUMBER
            )
while True:
    if datetime.datetime.now():
        print("Here is your list!")
        text_list(my_weekly_list)
        time.sleep(86400)

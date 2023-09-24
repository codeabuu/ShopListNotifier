#!/usr/bin/python3
import time
import datetime
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE_NUMBER, TO_PHONE_NUMBER

# Initialize the Twilio client with your account SID and auth token
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Define a list of items for your weekly shopping list
my_weekly_list = [
        'sugar','delmonte','maize floor','milk','mineral water'
        ]

# Define a function to send a text message with the provided list of items
def text_list(lst):
    msg_body = '\n'.join(lst)# Join the list items into a single message
    message = client.messages.create(
            from_ = FROM_PHONE_NUMBER,#your twilio phone no
            body = msg_body,
            to = TO_PHONE_NUMBER#recipients phine number
            )
# Continuously run the following code
while True:
    if datetime.datetime.now():
        print("Here is your list!")
        # Send the shopping list via text message using the text_list function
        text_list(my_weekly_list)
        time.sleep(86400)

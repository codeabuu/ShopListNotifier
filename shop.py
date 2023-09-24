#!/usr/bin/python3
import time
import datetime
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE_NUMBER, TO_PHONE_NUMBER

# Initialize the Twilio client with your account SID and auth token
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Define a list of items for your weekly shopping list
my_weekly_list = []

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
    enter_list = input("Enter item to add to your list(or 'done' to send): ").strip()

    if enter_list.lower() == 'done':
        if my_weekly_list:
            print("Here is your list!")
            text_list(my_weekly_list)
            time.sleep(120)
            my_weekly_list = []# Clear the shopping list after sending
        else:
            print("Shopping list empty")
    else:
        my_weekly_list.append(enter_list)

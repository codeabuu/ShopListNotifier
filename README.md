
README.md

This Python script allows you to create and send a weekly shopping list as a text message using Twilio. Git clone this repo the follow these instructions:

1. Install the required dependencies:
	pip install twilio
2. Create a Twilio account and obtain your account SID, auth token, and phone number.
3. Update the config.py file with your Twilio account SID, auth token, and phone number.
4. Run the script:
	shop.py
5. Enter items to add to your list. When you are finished, type done and the script will send you a text message tou your phone number with your shopping list.

Example:
	Enter item to add to your list(or 'done' to send): milk
Enter item to add to your list(or 'done' to send): eggs
Enter item to add to your list(or 'done' to send): bread
Enter item to add to your list(or 'done' to send): done

Here is your list!
* milk
* eggs
* bread

Additional Notes

The script will send the text message as per your set time until you send the done command. 
This is to prevent you from forgetting about your list.
You can also modify the script to send the shopping list to multiple phone numbers.
You can also use the script to send a text message with the shopping list on a specific day
**N.B** To keep your code running continuously in the background, even if your laptop is shut off, you'll need to host it on a remote server or use a cloud-based platform.
and time each week.

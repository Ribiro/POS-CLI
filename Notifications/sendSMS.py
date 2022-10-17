import africastalking
from dotenv import load_dotenv
import os

load_dotenv()


def send_sms(phone_number, message):
    # # Initialize SDK
    username = os.getenv("username")
    api_key = os.getenv("api_key")
    africastalking.initialize(username, api_key)

    # # Initialize a service e.g. SMS
    sms = africastalking.SMS

    number = phone_number
    code = '+254'
    number = number[1:]
    number = code + number
    message = message

    # Use the service synchronously
    response = sms.send(message, [number])
    print(response)

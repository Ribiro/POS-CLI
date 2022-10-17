import africastalking


def send_sms(phone_number, message):
    # # Initialize SDK
    username = "classapp"
    api_key = "288fbe4b335da8bf760888a22762f7d47b28ccd82688e119ceede7cb65fbfbf7"
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

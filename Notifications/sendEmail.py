import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("sender_email")
receiver_email = 'ribiro05@gmail.com'
password = os.getenv("password")

subject = "Testing"
text = "Testing sending email"

message = 'Subject: {}\n\n{}'.format(subject, text)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(sender_email, password)
print("login Success")
server.sendmail(sender_email, receiver_email, message, subject)

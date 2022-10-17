import smtplib
sender_email = 'ribirodenis05@gmail.com'
receiver_email = 'ribiro05@gmail.com'
password = 'hjutmbojageqodkg'

subject = "Testing"
text = "Testing sending email"

message = 'Subject: {}\n\n{}'.format(subject, text)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(sender_email, password)
print("login Success")
server.sendmail(sender_email, receiver_email, message, subject)

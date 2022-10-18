def send_email(receiver_email, subject, text):
    # imports
    import smtplib
    from dotenv import load_dotenv
    import os

    load_dotenv()

    sender_email = os.getenv("sender_email")
    receiver_email = receiver_email
    password = os.getenv("password")

    subject = subject
    text = text

    message = 'Subject: {}\n\n{}'.format(subject, text)

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message, subject)
    print("Email Sent Successfully!")

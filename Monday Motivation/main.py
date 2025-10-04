import datetime as dt
import smtplib
import random
import os

# Function to send email
def sending_mail(user_email, receiver_address, passkey, message):
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=user_email, password=passkey)
    connection.sendmail(from_addr=user_email, to_addrs=receiver_address, msg=message)
    print("Motivation Boost sent successfully!")
    connection.close()

# Load quotes from file
with open("quotes.txt", "r") as file:
    quotes = [line.strip() for line in file.readlines()]
    random_quote = random.choice(quotes)

# Get credentials from environment variables
PRIMARY_EMAIL = os.getenv("PRIMARY_EMAIL")
EMAIL_PASSKEY = os.getenv("EMAIL_PASSKEY")
TO_EMAIL = os.getenv("TO_EMAIL")

motivation_message = random_quote

# Get current day and time
date = dt.datetime.now()
current_day = dt.date.today().strftime("%A").lower()
current_time = date.strftime("%H:%M")

# Send email every Monday at 06:00
if current_day == "monday" and current_time == "06:00":
    if PRIMARY_EMAIL and EMAIL_PASSKEY and TO_EMAIL:
        sending_mail(
            user_email=PRIMARY_EMAIL,
            receiver_address=TO_EMAIL,
            passkey=EMAIL_PASSKEY,
            message=f"SUBJECT: Monday Motivation\n\n{motivation_message}"
        )
    else:
        print("Email credentials are not set. Please set environment variables.")

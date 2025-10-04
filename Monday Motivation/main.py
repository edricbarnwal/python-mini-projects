import datetime as dt
import smtplib 
import random

def sending_mail(user_email, receiver_address ,passkey, message):
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=user_email, password=passkey)
    connection.sendmail(from_addr=user_email, to_addrs=receiver_address, msg=message)
    print("Motivation Boost Succesfully.")
    connection.close()

with open(r"D:\PYTHON BOOTCAMP\DAY - 32 Send Email\monday_motivation\quotes.txt", "r") as file:
    quotes =  [line.strip() for line in file.readlines()]
    random_quote = random.choice(quotes)

primary_email = "edricbarnwal@gmail.com"
passkey = "arhj dpdu akrz mkdj"
to_email = "yash.barnwal2405work@gmail.com"
motivation_message = random_quote

date = dt.datetime.now()
current_day = dt.date.today().strftime("%A").lower()
current_time = date.strftime("%H:%M")

if current_day == "monday" and current_time == "06:00":
    sending_mail(user_email=primary_email, receiver_address=to_email, passkey=passkey, message=f"SUBJECT :Monday Motivation \n\n{motivation_message}")



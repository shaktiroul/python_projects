import smtplib
import random
import datetime as dt

MY_EMAIL = "random@gmail.com"
MY_PASSWORD = "random@123" 

now = dt.datetime.now()

if now.weekday() == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}.")

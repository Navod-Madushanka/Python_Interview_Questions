import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "navodmaithripala@gmail.com"
password = "idwrxesqvzuzobmc"

if weekday == 5:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="navodmaithripala@yahoo.com",
                            msg=f"Subject:Monday Quote\n\n{quote}")

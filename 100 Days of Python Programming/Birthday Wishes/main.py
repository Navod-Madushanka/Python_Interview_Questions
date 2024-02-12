##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("birthdays.csv")

# Initialize the birthdays_dict dictionary
birthdays_dict = {}

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    # Extract the month and day data from the row
    month = row["month"]
    day = row["day"]

    # Create a tuple from the month and day data
    key = (month, day)

    # Add the row data to the dictionary
    birthdays_dict[key] = row.to_dict()

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
today_month = dt.datetime.now().month
today_date = dt.datetime.now().day

if (today_month, today_date) in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    letter_id = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_id}.txt") as letter:
        content = letter.read()
        name = birthdays_dict[today_month, today_date]["name"]
        new_letter = content.replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

my_email = "navodmaithripala@gmail.com"
password = "idwrxesqvzuzobmc"

to_email = birthdays_dict[today_month, today_date]["email"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email,
                        msg=f"Subject:Happy Birthday\n\n{new_letter}")




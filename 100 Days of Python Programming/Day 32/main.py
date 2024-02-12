# import smtplib
#
# my_email = "navodmaithripala@gmail.com"
# password = "idwrxesqvzuzobmc"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="navodmaithripala@yahoo.com", msg="Subject:This is the subject of email\n\nThis is the Body of email.")

import datetime as dt

print(dt.datetime.now().microsecond)





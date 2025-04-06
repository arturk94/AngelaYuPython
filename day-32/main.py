# import smtplib
#
# my_email = "arturtest@yahoo.com"
# password = "mzkenqspnlwwexdn"
# #my_email = "arturktest@gmail.com"
# #password = "memsYc-ziwzak-tebno9"
#
# #with smtplib.SMTP("smtp.gmail.com") as connection:
# with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         #to_addrs="arturtest@yahoo.com",
#         to_addrs="arturktest@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# print(now)
#
# date_of_birth = dt.datetime(year=1974, month=1, day=1)
# print(date_of_birth)




import datetime as dt
import random as rd
import smtplib

now = dt.datetime.now()
dayofweek = now.strftime("%A")
print(dayofweek)

with open(file="quotes.txt", mode="r") as quotes:
    all_quotes = quotes.readlines()
    quote = rd.choice(all_quotes )
    print(quote)

MY_EMAIL = "arturktest@gmail.com"
MY_PASSWORD = "memsYc-ziwzak-tebno9"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="arturktest@gmail.com",
        msg=f"Subject:{dayofweek} Motivation\n\n{quote}")

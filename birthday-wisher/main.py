#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "arturktest@gmail.com"
MY_PASSWORD = "memsYc-ziwzak-tebno9"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
for tuple in birthdays_dict:
    print(tuple)
    if tuple == today_tuple:
        birthday_person = birthdays_dict[today_tuple]
        #print(birthday_person)
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
            #print(contents)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )



# import datetime as dt
# import pandas as pd
# import random as rd
# import smtplib
#
# PLACEHOLDER = "[NAME]"
# now = dt.datetime.now()
# year = now.year
# #month = now.month
# #day = now.day
# month = 1
# day = 1
#
# try:
#     data = pd.read_csv("birthdays.csv")
# except FileNotFoundError:
#     print("No birthdays file found.")
# else:
#     serie = data.loc[(data['month'] == month) & (data["day"] == day)]
#     birthday = serie.to_dict(orient="records")
#     if len(birthday) > 0:
#         for friend in birthday:
#             with open(f"./letter_templates/letter_{rd.randint(1,3)}.txt") as letter:
#                 mail = letter.read().replace(PLACEHOLDER, friend["name"].strip())
#                 MY_EMAIL = "arturktest@gmail.com"
#                 MY_PASSWORD = "memsYc-ziwzak-tebno9"
#
#                 with smtplib.SMTP("smtp.gmail.com") as connection:
#                     connection.starttls()
#                     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#                     connection.sendmail(
#                         from_addr=MY_EMAIL,
#                         to_addrs=friend["email"],
#                         msg=f"Subject:Happy Birrhday!\n\n{mail}")
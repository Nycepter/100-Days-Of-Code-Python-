import smtplib
import datetime as dt
import random
import pandas





my_email = "nycepter@gmail.com"
my_password = "wzgiirneenpphias"

 

today = dt.datetime.now()
year = today.year
month = today.month
weekday = today.weekday()

today_tuple = (today.month, today.day)

def send_email(email, message):
    with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday! \n\n {message}")


##################### Extra Hard Starting Project ######################


data = pandas.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    birthday_persons_email = birthday_person["email"]
    file_path = f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace("[NAME]", birthday_person["name"])
        send_email(birthday_persons_email, new_content)
    





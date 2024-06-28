import smtplib
import datetime as dt
import random

my_email = "nycepter@gmail.com"
my_password = "wzgiirneenpphias"

 

now = dt.datetime.now()
year = now.year
month = now.month2
weekday = now.weekday()

dob = dt.datetime(year=1993, month=1, day=3)


if weekday == 4:
    with open("Day 32/Birthday Wisher (Day 32) start/quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote_choice = random.choice(all_quotes)
    with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="acj.the.boss@gmail.com", msg=f"Subject:Great News! \n\n {quote_choice}")
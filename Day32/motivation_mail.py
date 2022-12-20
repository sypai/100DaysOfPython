import datetime as dt
import smtplib
import random

address = "smtp.gmail.com"
sender_email = 'suyashbajpai.web@gmail.com'
sender_password = 'tvfuhjbaasdbjznf'

def mail(quote, mail_to):
    with smtplib.SMTP(address) as connection:
        connection.starttls()
        connection.login(
            user=sender_email,
            password=sender_password
        )
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=mail_to,
            msg=f"Subject:Start your monday with high motivation!\n\n{quote}"
        )

quotes = []
with open('quotes.txt') as file:
    quotes = file.readlines()

quote = random.choice(quotes)

current = dt.datetime.now()
if current.weekday() == 1:
    if current.hour >= 1 and current.minute <= 36:
        mail(quote, "suyashbajpai.ibm@gmail.com")

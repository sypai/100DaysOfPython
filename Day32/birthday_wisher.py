import smtplib
import datetime as dt
import random
import pandas as pd

address = "smtp.gmail.com"
sender_email = 'suyashbajpai.web@gmail.com'
sender_password = ''

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

data = pd.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='index')
mail_list = [] 

for birthday in birthdays.values():
    to_add = {}
    if birthday['month'] == now.month and birthday['day'] == now.day:
        to_add['name'] = birthday['name']
        to_add['email'] = birthday['email']
        mail_list.append(to_add)

# If there is a birthday today, select a letter from letter templates and replace [NAME] with person's name      
if len(mail_list) > 0:
    
    for person in mail_list:
        
        num = random.randint(1, 3)
        file_name = f'./letter_templates/letter_{num}.txt'
        
        name = person['name']
        email = person['email']
        subject = "That day of the year!"

        with open(file_name) as file:
            letter = file.read()
            message = letter.replace("[NAME]", name)
        
        with smtplib.SMTP(address) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=email,
                msg=f"Subject:{subject}\n\n{message}"
                )
        print(name, email, subject, message)


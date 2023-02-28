# imports
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# constants
URL = 'https://www.amazon.in/SanDisk-Portable-Smartphone-Compatible-Warranty/dp/B08GTXVG9P/ref=sr_1_5?keywords=external%2Bssd%2B500gb&qid=1677565204&sprefix=external%2Bsdd%2Caps%2C254&sr=8-5&th=1'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
ACCEPT_LANGUAGE = 'en-US,en;q=0.9'
ACCEPT_ENCODING = 'gzip, deflate, br'
address = 'smpt.gmail.com'
sender_email = ''
sender_password = ''

header = {
    'Accept-Language' : ACCEPT_LANGUAGE,
    'User-Agent' : USER_AGENT,
    'Accept-Encoding':ACCEPT_LANGUAGE
}

# Making a get request to the URL
response = requests.get(URL, headers=header)

# Making soup 
soup = BeautifulSoup(response.content, 'lxml')

# Getting the Price from the soup
price = soup.select_one('span.a-price > span.a-offscreen').getText()

# Price is a string like '$7,299.00', Let's convert it to decimal
PRICE_THRESHOLD = 6500.00

price = price.split('₹')[1]
price = price.replace(',', '')
price = float(price)

PRICE_DROP_ALERT = f'Subject:AMAZON PRICE DROP ALERT for YOUR_ITEM\n\nHey User, Your '

if price < PRICE_THRESHOLD:
    # Send an Email if price goes below threshold
    with smtplib.SMTP(address) as connection:
        connection.starttls()
        connection.login(
            user=sender_email,
            password=sender_password
        )
        connection.sendmail(
            from_addr=sender_email,
            to_addrs='',
            msg=PRICE_DROP_ALERT
        )
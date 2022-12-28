import requests

STOCK = "AMZN"
COMPANY_NAME = "TESLA"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_key = ''
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': stock_api_key
}

response = requests.get(STOCK_API_ENDPOINT, params=parameters)

stock_data = response.json()['Time Series (Daily)']
stock_list = [values for (key, values) in stock_data.items()]
yesterday = float(stock_list[0]['4. close'])
day_before_yesterday = float(stock_list[1]['4. close'])

print(yesterday, day_before_yesterday)

def alarm():
    # ring[0] : False for Less than 5% change, True for more
    # ring[1] : Percent change
    # ring[2] : 1 for Increase, -1 for Decrease
    ring = [False, 0, 0] 
    change = yesterday - day_before_yesterday
    if change > 0:
        percent = (change / yesterday) * 100
        ring[1] = round(percent)
        ring[2] = 1
    else:
        percent = (-change / day_before_yesterday) * 100
        ring[1] = percent
        ring[2] = -1
    
    if percent > 5:
        ring[0] = True

    return ring

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
NEWS_API_KEY = ''
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
parameters = {
    'apiKey' : NEWS_API_KEY,
    'q' : COMPANY_NAME,
    # 'country' : 'us'
}
response = requests.get(NEWS_ENDPOINT, params=parameters)
news_data = response.json()['articles']

update = alarm()
if not update[0]:
    if update[2] == 1:
        symbol = '🔺' 
    elif update[2] == -1: 
        symbol = '🔻'

    stock_string = f"""
{STOCK}: {symbol}{update[1]}%    
Headline: {news_data[0]['title']}
Brief: {news_data[0]['description'].rstrip()}
    """

print(stock_string)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# parameters['function'] = 'CURRENCY_EXCHANGE_RATE'
# parameters['from_currency'] = 'usd'
# parameters['to_currency'] = 'inr'
# response = requests.get(STOCK_API_ENDPOINT, params=parameters)
# conversion_data = response.json()
# print(conversion_data)
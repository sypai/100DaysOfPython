from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.select('.athing .title .titleline a')

article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

for _ in range(len(articles)):
    print(f'{_+1}: {article_texts[_]}\n{article_links[_]}\n')
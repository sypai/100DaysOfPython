URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

import requests
from bs4 import BeautifulSoup

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies_list = soup.select('.gallery .article-title-description__text .title')
movies = []
for movie in movies_list:
    movies.append(movie.getText())

with open('movies.txt', 'w', encoding='utf-8') as file:
    for _ in range(99, -1, -1):
        file.write(f'{movies[_]}\n')

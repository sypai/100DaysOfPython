### Imports
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

### Constants
URL = 'https://www.billboard.com/charts/hot-100/'
SPOTIFY_CLIENT_ID = 'f02417fa20e74e76a5d5ce8173aac226'
SPOTIFY_CLIENT_SECRET = '84cf4c58febc4e2298d91e01cb712ddc'
REDIRECT_URI = 'http://example.com'

### User Input
date = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD :")

### Scraping BillBoard's Website to get 100 songs from the user entered time 
URL_with_date = URL + date
top_100 = {}
print(URL_with_date)
response = requests.get(URL_with_date)
soup = BeautifulSoup(response.text, 'html.parser')

# Getting the Song's name (Title)
titles = soup.select('.o-chart-results-list__item h3#title-of-a-story')

# For every title, get the artist's name and store it in a dictionary
for title in titles:
    artist = title.find_next_sibling().getText().strip()
    name = title.getText().strip()
    top_100[name] = artist

# We can make a text file : Song name by Artist name
'''
Write the songs in a text file 
with open(f'songs_{date}.txt', 'w', encoding='UTF-8') as file:
    for title, artist in top_100.items():
        file.write(f'{title} by {artist}\n')
'''

### Using the Spotify API to make a playlist of the Songs fetched above

# Authenticating our app to access spotify using Spotipy
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                            client_id=SPOTIFY_CLIENT_ID,
                                            client_secret=SPOTIFY_CLIENT_SECRET,
                                            redirect_uri=REDIRECT_URI,
                                            show_dialog=True,
                                            cache_path="token.txt"
                                            ))
                                        

user_id = sp.me()['id']

# Create a Playlist for the entered date
playlist = sp.user_playlist_create(user=user_id,
                         name=f'Billboard Top 100 : {date}',
                         public=False
                         )
playlist_id = playlist['uri']

# Loop through our dictionary top_100, 'search' song in spotify and add it to our playlist
year = date.split('-')[0]
songs_uri_list = []
for title, artist  in top_100.items():
    # Search Query :  https://developer.spotify.com/documentation/web-api/reference/#/operations/search
    q = f'track:{title} artist:{artist} year:{year}'
    result = sp.search(q, type='track', limit=1)
    # Some Songs might not be found, error handling
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uri_list.append(uri)
    except IndexError:
        try:
            q = f'track:{title} artist:{artist}'
            result = sp.search(q, type='track', limit=1)
            uri = result['tracks']['items'][0]['uri']
            songs_uri_list.append(uri)
        except IndexError:
            print(f"{title} by {artist} not found. Skipped...")

sp.playlist_add_items(playlist_id, songs_uri_list)


    






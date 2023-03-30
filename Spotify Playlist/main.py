from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

pp = pprint.PrettyPrinter(depth=4)

x = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{x}/")
billboard = response.text

soup = BeautifulSoup(billboard, "html.parser")

song_title = soup.select("li.o-chart-results-list__item h3.c-title")
songs = []
song_artist = soup.select('li.o-chart-results-list__item h3.c-title + span.c-label')
artists = []



for tag in song_title:
    song_name = tag.getText().strip()
    songs.append(song_name)

for tag in song_artist:
    song_artist = tag.getText().strip()
    artists.append(song_artist)
    

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id='c0a5120fc5784b8d91408ce5d5857186',
        client_secret='117bc86a81be459593a97cfbdae21b0b',
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

#YYYY = x[0:5]

uri = []

i = 0
song_length = len(songs)
while i < song_length:
    searchResults = sp.search(q=f"track: {songs[i]} artist: {artists[i]}", type='track')['tracks']['items']
    try: 
        song_uri = searchResults[0]['uri']
        uri.append(song_uri)  
    except IndexError: 
        print(f"{songs[i]} doesn't exist in Spotify. Skipped.")
    i += 1


playlist = sp.user_playlist_create(user_id, f'{x} Billboard 100', public=False)
playlist_id = playlist['id']

playlist = sp.user_playlist_add_tracks(user=user_id, playlist_id = playlist_id, tracks = uri)
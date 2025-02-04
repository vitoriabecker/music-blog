import requests 

params = {'track_name':'bang', 'artist_name':'anitta'}
x = requests.get('https://lrclib.net/api/get', params=params)

print(x.json())
x = x.json()
print(x.get('plainLyrics'))
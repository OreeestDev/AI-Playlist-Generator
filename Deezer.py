import requests
from Parsing import *

tracks = parse_playlist()

def Deezer_Promt():
    for track in tracks:
        r = requests.get('https://api.deezer.com/search', params={'q': f'artist:"{track["artist"]}" track:"{track["title"]}"'})




Deezer_Promt()
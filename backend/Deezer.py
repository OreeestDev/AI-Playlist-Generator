import time

import requests

from Promts import create_playlist



def Deezer_Promt(tracks):
    all_tracks = []
    for track in tracks:
        r = requests.get('https://api.deezer.com/search',
                         params={'q': f'artist:"{track["artist"]}" track:"{track["title"]}"'})
        time.sleep(1)
        data = r.json()
        if data["data"]:
            track_info = {
                "id": data["data"][0]["id"],
                "title": data["data"][0]["title"],
                "artist": data["data"][0]["artist"]["name"],
                "album": data["data"][0]["album"]["cover_medium"],
                "preview": data["data"][0]["preview"],
                "link": data["data"][0]["link"]
            }
            all_tracks.append(track_info)

        else:
            print("Data not found")

    print(all_tracks)



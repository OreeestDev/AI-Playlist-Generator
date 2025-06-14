import requests
import json




def prompt(content):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-app-or-website.com",
        "X-Title": "Mood Playlist Generator"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {
                "role": "user",
                "content": f" {content}  "
            }
        ],
        "route": "fallback",
        "transforms": ["middle"],
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()

        playlist_content = data["choices"][0]["message"]["content"]
        tracks = playlist_content.split("\n")
       # with open('response_data.json', 'w') as json_file:
       #      json.dump(tracks, json_file, indent=4)

       # for track in tracks:
       #     print(track)
        return tracks

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None


def parse_playlist(raw_tracks):


    data = raw_tracks

    tracks = []


    for line in data:

        if not line or len(line) < 3:
            continue


        if not line[0].isdigit():
            continue


        dot_position = line.find('.')
        if dot_position == -1 or dot_position > 3:
            continue





        artist_start = line.find('**') + 2
        artist_end = line.find('**', artist_start)
        if artist_start == 1 or artist_end == -1:
            continue

        artist = line[artist_start:artist_end].strip()



        title_start = line.find('*', artist_end + 2) + 1
        title_end = line.rfind('*')

        if title_start <= 0 or title_end == -1 or title_start >= title_end:
            print(f"Помилка індексів для назви: start={title_start}, end={title_end}")

            dash_pos = line.find('–', artist_end)
            if dash_pos != -1:
                title_start = line.find('*', dash_pos) + 1
                title_end = line.find('*', title_start)

        if title_start > 0 and title_end > title_start:
            title = line[title_start:title_end].strip()

            tracks.append({
                'artist': artist,
                'title': title
            })
        else:
            print(f"Не вдалося виділити назву для рядка: {line}")

    print(tracks)
    return tracks

def create_playlist(promt):
    raw_tracks = prompt(promt)

    playlist_content = parse_playlist(raw_tracks)

    return playlist_content



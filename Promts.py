import requests
import json


def prompt(mood):
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
                "content": f"Create a Spotify playlist for {mood} mood."
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
        with open('response_data.json', 'w') as json_file:
            json.dump(tracks, json_file, indent=4)

        for track in tracks:
            print(track)
        return playlist_content

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None


# Test the function
prompt("sad")

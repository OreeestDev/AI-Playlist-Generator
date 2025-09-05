import json
from Promts import prompt

playlist_content = prompt("Make a plalist for sad mood")

def parse_playlist():


    data = playlist_content

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









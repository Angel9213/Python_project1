import requests
from bs4 import BeautifulSoup

# Set the request headers
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/127.0.0.0 Safari/537.36"
}

# Define the artist's URL
artist_url = "https://music.91q.com/artist/A10273267"

# Send a request to get the webpage content
response = requests.get(artist_url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Get song information
song_boxes = soup.find_all(name="div", class_="song-box")
artists = soup.find_all(name="div", class_="artist ellipsis")

# Print song names and corresponding URLs
for index in range(1, len(song_boxes)):
    song_name = song_boxes[index].a.string
    song_link = "https://music.91q.com" + song_boxes[index].a["href"]
    print(song_name, song_link)

# Print artist names
for index in range(1, len(artists)):
    songer_name = " "
    songers = artists[index].find_all(name="a")
    for songer in songers:
        songer_name += songer.string + " "
    print(songer_name.strip())
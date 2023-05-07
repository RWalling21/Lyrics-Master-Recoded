import requests
from bs4 import BeautifulSoup
import sys

def get_titles(artist, limit=10):
    artist = artist.lower().replace(' ', '')
    url = f'https://www.azlyrics.com/{artist[0]}/{artist}.html'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    album_list = soup.find('div', id='listAlbum')

    if album_list is None:
        print(f"Artist '{artist}' not found on AZLyrics.")
        sys.exit(1)

    song_links = album_list.find_all('a', target='_blank')

    song_titles = []
    for link in song_links:
        song_titles.append(link.get_text())

        if limit is not None and len(song_titles) >= limit:
            break

    return song_titles



def get_lyrics(artist, song_title):
    artist = artist.lower().replace(' ', '')
    song_title = song_title.lower().replace(' ', '')
    url = f'https://www.azlyrics.com/lyrics/{artist}/{song_title}.html'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    lyrics = soup.find('div', class_='col-xs-12 col-lg-8 text-center').find('div', class_=None).get_text()
    return lyrics.strip()

def print_lyrics(artist, song_titles):
    for title in song_titles:
        try:
            lyrics = get_lyrics(artist, title)
            print(f'{title}\n{"=" * len(title)}\n{lyrics}\n\n')
        except Exception as e:
            print(f'Error fetching lyrics for "{title}": {e}')

def main():
    # Check that the correct number of arguments were passed
    if len(sys.argv) != 2:
        print('Usage: python lyrics_scraper.py <artist>')

    # Store Values
    artist = sys.argv[1]
    song_titles = get_titles(artist)

    print_lyrics(artist, song_titles)

if __name__ == '__main__':
    main()

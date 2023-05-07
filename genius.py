"""
Lyrics-Master
Created by Robert Walling 
rwalling115@gmail.com
"""

from mailbox import ExternalClashError
import scraper.config as config


def scrape(artist_name, count):
    genius = Genius(config.GENIUS_ACCESS_TOKEN)
    genius.response_format = "plain"
    genius.remove_section_headers = True
    genius.verbose = True

    try:
        artist = genius.search_artist(artist_name, max_songs=10, get_full_info=False)
        file_name = "LMDATA_" + artist_name
        # For now I'm just saving the lyrics to plain text, this may change
        artist.save_lyrics(filename=file_name, extension="txt", overwrite=True, ensure_ascii=False)
        # I'm definitely going to want to clean these lyrics aswell, maybe Regex?
        
    except Exception as e:
        print("Error: " + str(e))
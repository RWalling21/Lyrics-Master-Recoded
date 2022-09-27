"""
Lyrics-Master
Created by Robert Walling 
rwalling115@gmail.com
"""

import config

# Handles scraping the Genius API 
from lyricsgenius import Genius

def scrape(artist):
    genius = Genius(config.GENIUS_ACCESS_TOKEN)

    try:
        songs = genius.search_artist(artist)
        
    except:
        raise("Error: Could not find artist")

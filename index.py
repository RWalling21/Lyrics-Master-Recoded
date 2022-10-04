"""
Lyrics-Master
Created by Robert Walling 
rwalling115@gmail.com
"""

import Song
import genius

if __name__ == '__main__':
    print("Welcome to the Lyric Master Recoded!")
    artist_name = input("Please enter the artist you would like to use: ")
    count = 10
    genius.scrape(artist_name, count)

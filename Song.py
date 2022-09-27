"""
Lyrics-Master
Created by Robert Walling 
rwalling115@gmail.com
"""

class Song:
    # Constructor
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.verse = []
        self.chorus = []

    # Getters 
    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_verse(self):
        return self.verse
        
    def get_chorus(self):
        return self.chorus

    # Setters 
    def add_verse(self, lyric):
        # Append a lyric to the verse
        self.verse.append(lyric)

    def add_chorus(self, lyric):
        # Append a lyric to the chorus
        self.chorus.append(lyric)

    # Methods 
    def __str__(self):
        # Don't like how long this line is...
        return "Title: " + self.title + "\n".join(self.verse) + "".join(self.chorus) + "\n".join(self.verse)
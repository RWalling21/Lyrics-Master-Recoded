# Implement PyTest
import pytest
import genius

def test_get_songs():
    # This test takes forever to run due to how the lyricsGenius library works
    
    expected = 5

    actual = len(genius.scrape("Mac Demarco", 5))

    assert expected == actual
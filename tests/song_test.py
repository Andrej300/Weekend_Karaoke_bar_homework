import unittest 
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Part time lover", "Stevie Wonder", "R&B")

    def test_song_has_title(self):
        self.assertEqual("Part time lover", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Stevie Wonder",self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("R&B", self.song.genre)
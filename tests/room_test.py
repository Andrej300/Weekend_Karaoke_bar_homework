import unittest 
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        
        self.room_1 = Room("Karaoke Star", 50)
        self.room_2 = Room("Karaoke Rooms", 20)
        self.room_3 = Room("Scotland's got talent", 10)

        self.guest_1 = Guest("Arnold")
        self.guest_2 = Guest("John")
        self.guest_3 = Guest("Tamara")

        self.song_1 = Song("Hotel California", "Eagles", "rock")
        self.song_2 = Song("Viva Las Vegas", "Elvis Presley", "Rock and roll")
        self.song_3 = Song("Billie Jean", "Michael Jackson", "Pop")




    def test_room_has_name(self):
        self.assertEqual("Karaoke Star", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(50, self.room_1.capacity)

    def test_count_guests(self):
        self.assertEqual(0, self.room_1.count_guests())

    def test_guest_was_checked_in(self):
        self.room_1.check_in_guests(self.guest_1)
        self.assertEqual(1, self.room_1.count_guests())

    def test_guest_was_checked_out(self):
        self.room_1.check_out_guests(self.guest_1)
        self.assertEqual(0, self.room_1.count_guests())
        

    def test_count_songs(self):
        self.assertEqual(0, self.room_2.count_songs())

    def test_song_was_added_to_room(self):
        self.room_2.add_songs_to_rooms(self.song_2)
        self.assertEqual(1, self.room_2.count_songs())
import unittest 
from classes.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        
        self.room = Room("Karaoke Star", 50)


    def test_room_has_name(self):
        self.assertEqual("Karaoke Star", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(50, self.room.capacity)
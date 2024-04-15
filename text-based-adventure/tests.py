import unittest
from main import Player, Room, Game


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")

    def test_health(self):
        self.assertEqual(self.player.health, 100)

    def test_inventory(self):
        self.assertEqual(len(self.player.inventory), 0)


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Test Room", "This is a test room.")

    def test_description(self):
        self.assertEqual(self.room.get_description(), "This is a test room.")


if __name__ == '__main__':
    unittest.main()

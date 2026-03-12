import unittest
from resa.resa import *

class ResaUnitTests(unittest.TestCase):
    def test_petite(self):
        self.assertEqual(bookMeetingRoom(3), Room.SMALL)
    def test_moyenne(self):
        self.assertEqual(bookMeetingRoom(20), Room.MEDIUM)
    def test_grande(self):
        self.assertEqual(bookMeetingRoom(43), Room.LARGE)
    def test_trop_grand(self):
        self.assertEqual(bookMeetingRoom(52), Room.REFUSE)
    def test_erreur(self):
        self.assertRaises(ValueError, bookMeetingRoom,-2)


if __name__ == '__main__':
    unittest.main()

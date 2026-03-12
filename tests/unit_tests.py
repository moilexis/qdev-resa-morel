import unittest
from resa.resa import *

class ResaUnitTests(unittest.TestCase):
    def test_petite(self):
        self.assertEqual(bookMeetingRoom(3), "Small")
    def test_moyenne(self):
        self.assertEqual(bookMeetingRoom(20), "Medium")
    def test_grande(self):
        self.assertEqual(bookMeetingRoom(43), "Large")
    def test_trop_grand(self):
        self.assertEqual(bookMeetingRoom(52), "Refused")
    def test_erreur(self):
        self.assertEqual(bookMeetingRoom(-2), "Small")


if __name__ == '__main__':
    unittest.main()

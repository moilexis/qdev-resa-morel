import unittest
from resa.resa import *

class ResaUnitTests(unittest.TestCase):
  def test_petite(self):
    self.assertEqual(bookMeetingRoom(3), "Small")

if __name__ == '__main__':
  unittest.main()

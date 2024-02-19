from classes import *
from Project2 import *
import unittest


# Write two test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        P1 = Point(1,2)
        P2 = Point(5,3)
        self.assertEqual([1,2,3,5], create_rectangle(P1,P2))


    # Part 2
    def test_shorter_duration_than1(self):
        dur1 = Duration(5,10)
        dur2 = Duration(2,34)
        self.assertEqual(False,shorter_duration_than(dur1,dur2))

    def test_shorter_duration_than2(self):
        dur1 = Duration(5,10)
        dur2 = Duration(5,34)
        self.assertEqual(True,shorter_duration_than(dur1,dur2))

    def test_shorter_duration_than3(self):
        dur1 = Duration(2,10)
        dur2 = Duration(5,34)
        self.assertEqual(True,shorter_duration_than(dur1,dur2))

    def test_shorter_duration_than4(self):
        dur1 = Duration(3,49)
        dur2 = Duration(3,49)
        self.assertEqual(False,shorter_duration_than(dur1,dur2))

    # Part 3
    def test_songs_shorter_than1(self):
        song1 = Song('Doja Cat', 'Streets', Duration(3,46))
        song2 = Song('Plain White Ts', 'Hey There Delilah', Duration(4,57))
        song3 = Song('Taylor Swift', 'All Too Well', Duration(10,13))
        song4 = Song('Avenged Sevenfold', 'Little Piece of Heaven', Duration(6,23))
        song5 = Song('Bruno Mars', 'Grenade', Duration(3,42))
        song_list = [song1,song2,song3,song4,song5]
        self.assertEqual([song1,song2,song5],songs_shorter_than(song_list,Duration(5,10)))

    def test_songs_shorter_than2(self):
        song1 = Song('Patty Smith Hill', 'Happy Birthday Song', Duration(1,10))
        song2 = Song('The Weeknd', 'In the Night', Duration(3,56))
        song3 = Song('Black Pink', 'Shut Down', Duration(3,32))
        song4 = Song('BTS', 'Butterfly Intro', Duration(1,59))
        song5 = Song('Aespa', 'Black Mamba', Duration(4,10))
        song_list = [song1,song2,song3,song4,song5]
        self.assertEqual([song1,song4],songs_shorter_than(song_list,Duration(2,0)))

    def test_songs_shorter_than3(self):
        song_list = []
        self.assertEqual(None,songs_shorter_than(song_list, Duration(5,5)))

    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()

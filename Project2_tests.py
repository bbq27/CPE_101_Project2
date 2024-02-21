from classes import *
from Project2 import *
import unittest


# Write two test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        P1 = Point(1,2)
        P2 = Point(5,3)
        self.assertEqual(Rectangle(Point(1,3),Point(5,2)), create_rectangle(P1,P2))

    def test_create_rectangle_2(self):
        P1 = Point(-9,14)
        P2 = Point(11,37)
        self.assertEqual(Rectangle(Point(-9,37),Point(11,14)), create_rectangle(P1,P2))

    def test_create_rectangle_3(self):
        P1 = Point(2,2)
        P2 = Point(10,10)
        self.assertEqual(Rectangle(Point(2,10),Point(10,2)), create_rectangle(P1,P2))

    def test_create_rectangle_4(self):
        P1 = Point(2,4)
        P2 = Point(10,10)
        self.assertEqual(Rectangle(Point(2,10),Point(10,4)), create_rectangle(P1,P2))

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
    def test_running_time1(self):
        song1 = Song('Patty Smith Hill', 'Happy Birthday Song', Duration(1, 10))
        song2 = Song('The Weeknd', 'In the Night', Duration(3, 56))
        song_list = [song1, song2]
        playlist = []
        self.assertEqual(None, running_time(song_list,playlist))

    def test_running_time2(self):
        song_list = []
        playlist = [0,1,3]
        self.assertEqual(None, running_time(song_list,playlist))

    def test_running_time3(self):
        song1 = Song('Doja Cat', 'Streets', Duration(3, 46))
        song2 = Song('Plain White Ts', 'Hey There Delilah', Duration(4, 57))
        song3 = Song('Taylor Swift', 'All Too Well', Duration(10, 13))
        song4 = Song('Avenged Sevenfold', 'Little Piece of Heaven', Duration(6, 23))
        song5 = Song('Bruno Mars', 'Grenade', Duration(3, 42))
        song_list = [song1, song2, song3, song4, song5]
        playlist = [0,2,5,4,1,1]
        self.assertEqual(Duration(27,35),running_time(song_list,playlist))

    def test_running_time4(self):
        song1 = Song('Patty Smith Hill', 'Happy Birthday Song', Duration(1, 10))
        song2 = Song('The Weeknd', 'In the Night', Duration(3, 56))
        song3 = Song('Black Pink', 'Shut Down', Duration(3, 32))
        song4 = Song('BTS', 'Butterfly Intro', Duration(1, 59))
        song5 = Song('Aespa', 'Black Mamba', Duration(4, 10))
        song_list = [song1, song2, song3, song4, song5]
        playlist = [-1, 0, 0, 2, 17, 2]
        self.assertEqual(Duration(9, 24), running_time(song_list, playlist))

    # Part 5
    def test_validate_route1(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        routes = ['san luis obispo', 'santa margarita', 'atascadero','creston']
        self.assertEqual(True, validate_route(city_links,routes))

    def test_validate_route2(self):
        city_links = [['long beach', 'carson'],
                      ['torrance', 'carson'],
                      ['torrance', 'palos verdes'],
                      ['long beach', 'huntington beach']]
        routes = ['huntington beach', 'carson', 'torrance', 'palos verdes']
        self.assertEqual(False, validate_route(city_links,routes))

    def test_validate_route3(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        routes = ['san luis obispo']
        self.assertEqual(True, validate_route(city_links,routes))

    def test_validate_route4(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]
        routes = []
        self.assertEqual(True, validate_route(city_links,routes))

    # Part 6
    def test_max1(self):
        lst = [1,1,2,2,1,1,1,3]
        self.assertEqual(([2,2,3,1],[0,2,4,7]), max(lst))

    def test_max2(self):
        lst = []
        self.assertEqual(None, max(lst))
    def test_longest_repetition1(self):
        lst = [1,1,2,2,1,1,1,3]
        self.assertEqual(4, longest_repetition(lst))

    def test_longest_repetition2(self):
        lst = [3,3,3,3,2,2,1,1,3,3,3,4]
        self.assertEqual(0,longest_repetition(lst))

    def test_longest_repetition3(self):
        lst = [5,5,5,3,2,2,2,2,1,1,4,4,5,6,7,-1,-1,-1,-1]
        self.assertEqual(4,longest_repetition(lst))

    def test_longest_repetition4(self):
        lst = [-5,-5,-5,-5,4,4,-5,-5,2,2,2,2,1,1,3,3]
        self.assertEqual(0,longest_repetition(lst))




if __name__ == '__main__':
    unittest.main()

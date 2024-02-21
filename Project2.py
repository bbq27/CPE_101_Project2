# Name: Berfredd Quezon
# Section: 11
from classes import *
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input: two point objects
output: rectangle object
purpose: create the biggest possible rectangle object with two inputted points 
Steps:
1) check if the x coord and y coord of the first point are equal to each other or if the x coord and the y coord
of the second point are equal to each other
    1.1) if they are, return a rectangle object with the top left point being the first point's x coord and second
    point's y coord and the bottom right point being the second point's x coord and the first point's y coord
2) check if the x coord of the first point is less than the x coord of the second point
    2.1) if True
        2.1.1) set a variable left_x equal to the first point's x coord
        2.1.2) set another variable right_x equal to the second point's x coord
    2.2) if False
        2.2.1) set a variable left_x equal to the second point's x coord
        2.2.2) set another variable right_x equal to the first point's x coord
3) check if the first point's y coord is less than the second point's y coord
    3.1) if True
        3.1.1) set a variable bottom_y equal to the first point's y coord
        3.1.2) set another variable top_y equal to the second point's y cord
    3.2) if False
        3.2.1) set a variable bottom_y equal to the second point's y coord
        3.2.2) set another variable top_y equal to the first point's y coord
4) return a Rectangle object with the top left point as left_x and top_y and the bottom right point as 
right_x and bottom_y
'''
# Implementation
def create_rectangle(P1: Point, P2: Point) -> Rectangle:
    if P1.x == P1.y or P2.x == P2.y:
        return Rectangle(Point(P1.x, P2.y), Point(P2.x, P1.y))
    if P1.x < P2.x:
        left_x = P1.x
        right_x = P2.x
    else:
        left_x = P2.x
        right_x = P1.x
    if P1.y < P2.y:
        bottom_y = P1.y
        top_y = P2.y
    else:
        bottom_y = P2.y
        top_y = P1.y
    return Rectangle(Point(left_x,top_y),Point(right_x,bottom_y))

# Part 2
'''Design Recipe (Write your design recipe here!)
input: two duration objects
output: boolean
purpose: check two durations and return true if the first inputted duration is less than the second
Steps:
1) check if the first duration minutes value is less than the second duration minutes value
    1.1) if it is, return True
2) check if the first duration minutes value is equal to the second duration minutes value
    2.1) if it is, check if the first duration seconds value is less than the second duration seconds value
        2.1.1) if it is, return True
    2.2) if it isn't check if the seconds value for both directions are equal
        2.2.1) if it is, return False
    2.3) return false otherwise
3) return false otherwise
'''
# Implementation
def shorter_duration_than(dur1: Duration, dur2: Duration) -> bool:
    if dur1.minutes < dur2.minutes:
        return True
    elif dur1.minutes == dur2.minutes:
        if dur1.seconds < dur2.seconds:
            return True
        elif dur1.seconds == dur2.seconds:
            return False
        else:
            return False
    else:
        return False


# Part 3
'''Design Recipe (Write your design recipe here!)
input: list of song objects and a duration object
output: list of song objects
purpose: create a list that contains songs whose duration is less than the inputted duration 
Steps:
1) check if the list is empty
    1.1) if it is, return None
2) create a list shorter_than to store the songs shorter than the inputted duration
3) loop through each value in the list
    3.1) check if the song duration is less than the inputted duration
        3.1.1) if it is, add that song to the list shorter_than
4) return shorter_than
'''
# Implementation
def songs_shorter_than(lst: list[Song], dur: Duration) -> Optional[list[Song]]:
    if not lst:
        return None
    shorter_than = []
    for song in lst:
        if shorter_duration_than(song.duration, dur) == True:
            shorter_than.append(song)
    return shorter_than


# Part 4
'''Design Recipe (Write your design recipe here!)
input: list of song objects and list of integers
output: Duration object
purpose: create a duration object that represents the total duration of an inputted song list with determining 
indices from another list of integers
Steps:
1) check if either the inputted list of songs or list of ints are empty
    1.1) if they are, return None
2) create an empty list named final_songs
3) loop through each number in the inputted list of ints named playlist
    3.1) check if the integer in the list is greater than or equal to 0 AND is less than the length of the list 
    of songs song_list
        3.1.1) if it is, add the corresponding song in the song_list with the index from the playlist to the 
        list final_songs
4) create a duration object total_dur with minutes and seconds equal to 0
5) loop through each song in the final_songs list
    5.1) set a variable time equal to that specific songs duration attribute
    5.2) add the minutes from time to the minutes of the total_dur
    5.3) add the seconds from time to the seconds of the total_dur
    5.4) check if the seconds from the total_dur is greater than 60
        5.4.1) if True
            5.4.1.1) add one to the minutes of total_dur
            5.4.1.2) subtract 60 from the seconds of total_dur
6) return total_dur 
'''
# Implementation
def running_time(song_list:list[Song], playlist:list[int]) -> Optional[Duration]:
    if not song_list or not playlist:
        return None
    final_songs = []
    for num in playlist:
        if 0 <= num < len(song_list):
            final_songs.append(song_list[num])
    total_dur = Duration(0,0)
    for song in final_songs:
        time = song.duration
        total_dur.minutes += time.minutes
        total_dur.seconds += time.seconds
        if total_dur.seconds > 60:
            total_dur.minutes += 1
            total_dur.seconds -= 60
    return total_dur

# Part 5
'''Design Recipe (Write your design recipe here!)
input: list of list of strings and a list of strings
output: bool
purpose: determine if a route is valid based on an inputted list of valid routes
Steps:
1) check if the list of cities aka the route is empty or if there is only one route in the list
    1.1) if this is true, return True
2) create a variable to store a counter for the # of valid routes in a list named valid_route and set it equal to 0
3) loop through each value through the index in range of the length of the route list minus one
    3.1) create a list temp that stores the city of that index in the route list as the first item and the 
    city of the next index in the route list as the second item
    3.2) create a list reverse that stores the city of the next index in the route list as the first item and the
    city of that index in the route list as the second item
    3.3) check if temp or reverse is in the inputted list of links
        3.3.1) if it is, add one to valid_route
4) check if valid_route is equal to the length of the route list minus one
    4.1) if True, return True
    4.2) if False, return False
'''
# Implementation
def validate_route(city_links:list[list[str]],route:list[str]) -> bool:
    if not route or len(route) == 1:
        return True
    valid_route = 0
    for idx in range(len(route)-1):
        temp = [route[idx], route[idx + 1]]
        reverse = [route[idx+1], route[idx]]
        if temp in city_links or reverse in city_links:
            valid_route += 1
    if valid_route == len(route)-1:
        return True
    else:
        return False

# Part 6
'''Design Recipe (Write your design recipe here!)
input: list of integers
output: int
purpose: find the index of the longest contiguous repetition of a single number
Steps:
1) check if the list of integers is empty
    1.1) if it is, return None
2) create an empty list named repetitions_count to store the number of times any number is repeated in a list
3) create an empty list named dupe_idx to store the starting index of when a number changes 
4) loop through the a number less than the length of the list
    4.1) loop through an infinite loop
        4.1.1) check if the item in that index is equal to the item in the next index
            4.1.1.1) if it is, add one to the count
'''
'''Design Recipe (Write your design recipe here!)
input: list of integers
output: int
purpose: find the index of the longest contiguous repetition of a single number
Steps:
1) check if the list of integers is empty
    1.1) if it is, return None
2) create an empty list named repetitions_count to store the number of times any number is repeated in a list
3) create an empty list named dupe_idx to store the starting index of when a number changes 
4) loop through the a number less than the length of the list
    4.1) loop through an infinite loop
        4.1.1) check if the item in that index is equal to the item in the next index
            4.1.1.1) if it is, add one to the count
'''
# Implementation
def max(lst:list[int]) -> Optional[tuple]:
    if not lst:
        return None
    repetitions_count = []
    dupe_idx = []
    idx = 0
    while idx < len(lst):
        loop = 0
        count = 0
        while loop == 0:
            if idx + count < len(lst) - 1 and lst[idx + count] == lst[idx + count + 1]:
                count += 1
            else:
                count += 1
                loop += 1
        repetitions_count.append(count)
        dupe_idx.append(idx)
        idx += count
    return repetitions_count,dupe_idx


def longest_repetition(lst:list[int]) -> Optional[int]:
    if not lst:
        return None
    max_list = max(lst)
    large = max_list[0][0]
    large_idx = 0
    for n in range(len(max_list[0])):
        if max_list[0][n] > large:
            large = max_list[0][n]
            large_idx = n
    return max_list[1][large_idx]

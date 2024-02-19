# Name: Berfredd Quezon
# Section: 11
from classes import *
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input:
output:
purpose:
Steps:
1) 
'''


# Implementation
def create_rectangle(P1: Point, P2: Point) -> Rectangle:
    points = [P1.x, P1.y, P2.x, P2.y]
    points.sort(reverse=False)
    return points


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
input:
output:
purpose:
Steps:
1) 
'''
# Implementation


# Part 5
'''Design Recipe (Write your design recipe here!)
input:
output:
purpose:
Steps:
1) 
'''
# Implementation


# Part 6
'''Design Recipe (Write your design recipe here!)
input:
output:
purpose:
Steps:
1) 
'''
# Implementation

"""Dictionary Utility Functions"""

__author__ = "730762790"

def invert (dict_1: dict [str, str]) -> dict [str, str]:
    """inverts the keys and values, error if there are duplicates"""
    inverted_dict_1: dict[str,str] = {} #empty dict 
    for key, value in dict_1.items(): #goes through each key and value 
        if value in inverted_dict_1:
            raise KeyError (f"{value} is used twice")
        inverted_dict_1 [value] = key 
    return inverted_dict_1 

def favorite_color (colors: dict [str, str]) -> str:
    """returns the most shown color"""
    if not colors: 
        return ""
    color_count: dict [str, int] = {} #new dict to add onto 
    for color in colors.values(): 
        color_count [color] = color_count.get(color, 0) +1 #adds into the color count 

    max_color: str = ""
    max_count:int = -1 

    for color, count in color_count.items(): #calculates what is shown most 
        if count > max_count or (count == max_count and max_color == ""):
            max_color = color 
            max_count = count 
    return max_color 

def count (items: list [str]) -> dict[str, int]: 
    """counts the # of times each item occurs and returns the counts in a dict"""
    count_dict: dict [str, int] = {}
    for thing in items: #goes through each one to count 
        count_dict[thing] = count_dict.get(thing, 0)+1
    return count_dict 

def alphabetizer (words: list [str])-> dict [str, list[str]]:
    """sorts the word into the first letter which is the key and all the values start off with that letter"""
    result: dict [str, list[str]] = {}
    for word in words: #each word in the list is run through to see what it starts with and is added into the list 
        first_character = word[0].lower()
        result[first_character] = result.get (first_character,[]) + [word]
    return result 

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
   """updates the attendance dictionary by adding a student to the list of attendees for a given day of the week without repeating names"""
   if day in attendance:
       if student not in attendance[day]:
           attendance[day].append(student)
   else:
       attendance[day] = [student]
       
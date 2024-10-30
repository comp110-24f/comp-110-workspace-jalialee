"""housing three different functions to be tested"""

__author__ = "730762790"

def only_evens (input:list [int]) -> list:
    """returns a list with only evens"""
    i = 0 
    evens = []
    while i < len(input): #as index is less than the length of the list
        if input[i] % 2 == 0: #the list at that index as to be even (2 can go into it evenly)
            evens.append(input[i]) #the evens list would add that index value
        i += 1 
    return evens 

def sub (numinput: list[int], start: int, end: int) -> list:
    """return a subset of the input list from index start to index end"""
    if len(numinput) == 0 or start >= len(numinput) or end <= 0: #all of these should return an empty list
        return []
    if start < 0: #when start index is a negative, list would start from beginning
        start = 0 
    if end > len (numinput): #when end index is greater than length of list, end would equal length of list 
        end = len (numinput)
    return numinput [start: end]

def add_at_index (listinput: list [int], element: int, elemind: int) -> None: 
    """modify the input list to place element at the given index"""
    if elemind < 0 or elemind > len(listinput):
        raise IndexError ("Index is out of bounds for the input list")
    listinput.append(0)
    for i in range(len(listinput)-1, elemind, -1):
        listinput [i] = listinput [i - 1]
    listinput[elemind] = element 





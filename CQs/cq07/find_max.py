__author__ = "730762790"

def find_and_remove_max (input: list[int]) -> int:
    """will return the max value and also delete it from list"""
    if len(input) == 0: # if the list is empty, it will return -1
        return -1 
    max_value = input [0]
    i = 0 
    while i < len (input): #if the index is less then lenth of input
        if input [i] > max_value: #input at that index is greater than max value would be the next big value
            max_value = input [i]
        i += 1 #this while loop finds the max values

    i = 0 
    while i < len (input): # this while loop deletes those max values 
        if input [i] == max_value:
            input.pop(i) 
        i += 1
    return max_value 

   



"""Mutating functions"""

__author__ = "730762790"

def manual_append (app_int: int, int_list: list[int])-> None: 
    """add an int to the list"""
    int_list.append (app_int)

def double (mutate2: list[int])-> None: 
    """mutiply each value in the list by 2"""
    index : int = 0 #index will start at 0 to move through each index. 
    while index < len (mutate2): 
        mutate2 [index]*= 2 #adds 2 onto each index
        index += 1


list_1: list[int] = [1,2,3] 
list_2: list[int] = list_1 #setting the lists equal to each other 

double (list_2) #calls for the function 
print ("list 1: ", list_1)
print ("list 2: ", list_2)



    


"""exercise with list"""
__author__= "730762790"

def all(list: list[int], target: int) -> bool:
    """Checks if all numbers in the list are equal to indicated number."""
    if len(list) == 0:
        return False
    i: int = 0
    while i < len(list): #ensures each index is the same 
        if list[i] != target:  
            return False
        i += 1
    return True
   
def max (input: list[int]) -> int: 
    """will return the highest number in the list"""
    if len(input) == 0: #if inputted an empty list, an error would be printed
        raise ValueError ("max () arg is an empty List")
    max_value: int = input[0]
    j: int = 1 
    while j < len(input): #ensures that the max value is the highest int in the list 
        if input[j] > max_value:
            max_value = input [j]
        j+=1 
    return max_value

def is_equal (listone: list[int], listtwo: list[int]) -> bool: 
    """ensures that both list are equal to each other"""
    if len(listone) != len (listtwo): #if list are not equal to each other
        return False 
    if not listone and not listtwo: 
        return True 
    i: int = 0 
    while i< len (listone): #loops through every element in the list to ensure equality 
        if listone[i] != listtwo[i]:
            return False 
        i += 1 
    return True 

def extend (inputlist1: list[int], inputlist2: list[int]) -> None: 
    """adds the second list to the first list"""
    for d in inputlist2:
        inputlist1.append(d) #appending the values of list 2 into list 1



    

   
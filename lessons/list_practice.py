"""basic syntax of lists"""


#create an empty list 
#my_numbers: list[float] = list() #constructor 
#my_numbers: list[float] = [] #literal 
#print (my_numbers)

#adding a value to a list using the append method
#my_numbers.append(1.5)
#my_numbers.append(2.3)
#print (my_numbers)

#string analogy 
#my_name: str = "" #literal 
#my_name: str = str() #construction 

#creating a populated list 
game_points: list [int] = [102,86,94]
#print (game_points)

#practice indexing 
#print (game_points [2]) #this prints out 94 
#last_game: int = game_points[2]
#print (last_game)

#modifiying the list by indexing 
#(because lists are mutable)
game_points[1] = 72
print (game_points)
#getting the length of list 
#print (len (game_points))

#pop method to remove item 
game_points.pop(1)
print (game_points)

#practice 
def display (int_list: list[int]) -> None: 
    """displays all elements of int list"""

    index : int = 0 

    while index < len(int_list):
        print(int_list[index])
        index += 1

display (int_list=game_points)



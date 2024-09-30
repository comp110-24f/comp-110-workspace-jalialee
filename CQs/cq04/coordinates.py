__author__ = "730762790"

def get_coords (xs: str , ys: str) -> None: #this function will that has two strings but returns nothing
    """this is the main function that will print out each index of one word with each indexes of the other word"""
    i = 0 
    while i < len (xs) :  
        j=0 
        while j < len (ys) : #as the index increases, as long as the index is not greater than the length of the word, the program will continue
            print (((xs[i]), (ys[j])))
            j+= 1
        i+=1 #if the index is greater, the index of xs will increase 



    


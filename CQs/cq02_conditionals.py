"""Simple number guessing game"""

__author__ = 730762790

def guess_a_number () -> None: # this is the main function that returns none so everything is diplayed in terminal. 
    """main function"""

    secret: int = 7 # this is the variable secret that is assigned to the value 7.

    x = int (input ("Guess a number:")) # this starts off the run with a statement where you can input your own number.

    print("Your guess was " + str (x)) #this is what is returned in terminal 

    if x == secret: # if the number guessed was 7 then it is equal therefore it'll release the "you got it!" statement 
        print ("You got it!")
    elif x < secret: # if the number guessed is less than 7, it'll release the statement.
        print ("Your guess was too low! The secret number is 7")
    else: # if not either, it'll release the statement below 
        print ("Your guess was too high! The secret number is 7")

if __name__ == "__main__": #this should call the function
    guess_a_number() 


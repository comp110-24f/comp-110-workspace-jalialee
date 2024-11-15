"""File to define Bear class."""

__author__ = "730762790"

class Bear:
    """Bear attributes: init, one_day, and eat function"""
    age: int 
    hunger_score: int 

    def __init__(self, age: int = 0, hunger_score: int = 0) -> None:
        """initial"""
        self.age = age #initializing ages to be 0 
        self.hunger_score = hunger_score
      
    
    def one_day(self) -> None:
        """adds to the age and the hunger score 1 per day"""
        self.age +=1 #increases age by 1
        self.hunger_score = self.hunger_score - 1 #decreases hunger by 1 
      
    
    def eat (self, num_fish: int) -> None: 
        """increases the hunger score as the number of fishes increase"""
        self.hunger_score += num_fish 
        self.hunger_score = max(0, self.hunger_score) #ensures hunger_score doesn't go below 0 
       
    
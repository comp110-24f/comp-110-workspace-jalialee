"""File to define Fish class."""

__author__ = "730762790"

class Fish:
    """Fish attributes: init and one_day function"""

    age : int
    
    def __init__(self, age: int = 0): 
        """initial"""
        self.age = age #initializes age at 0 
        return None
    
    def one_day(self): 
        """add to the age 1"""
        self.age += 1 #self.age increases by 1 
        return None
    
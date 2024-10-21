__author__= "730762790"

from CQs.cq07.find_max import find_and_remove_max

def test_find_max_use_case () -> None:
    """returns the expected max value"""
    d: list [int] = [1,2,3,4,5,] #list of ints used
    assert find_and_remove_max (d) == 5 #the max value should be 5 

def test_remove_use_case () -> None: 
    """mutating the function the expected way by taking away the max number from list"""
    d: list [int] = [1,2,3,4,5,]
    find_and_remove_max (d)
    assert d == [1,2,3,4] #the list should return without max value
     
def test_find_remove_edge_case () -> None:
    """returns the correct value in case of an unconventional input."""
    d: list [int] = []
    assert find_and_remove_max (d)
    assert d == [] 

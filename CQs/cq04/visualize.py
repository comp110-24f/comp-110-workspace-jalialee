__author__ = "730762790" 
"""importing of two functions"""
from CQs.cq04.concatenation import concat #importation of the function concat from concatenation.py
x:str = "123"  #these are global variables 
y: str = "abc" 
print (concat(str_1=x, str_2=y))

from CQs.cq04.coordinates import get_coords #importation of get_coords from coordinates.py 

print (get_coords (xs=x, ys=y))


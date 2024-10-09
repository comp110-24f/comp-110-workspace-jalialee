"""Summing the elements of list using different loops"""
__author__ = "730762790"

def w_sum (vals: list[float]) -> float:
    index = 0 
    total = 0.0 
    while index < len (vals):
        total += vals [index]
        index += 1 
    return total 

def f_sum (vals: list[float]) -> float: 
    total = 0.0 
    for value in vals:
        total += value 
    return total

def f_range_sum (vals: list[float]) -> float: 
    total = 0.0 
    for i in range (0, len(vals)):
        total += vals[i]
    return total 

print (w_sum (vals = [1.0, 2.0, 3.0]))
print (f_sum (vals=[1.0, 2.0, 3.0]))


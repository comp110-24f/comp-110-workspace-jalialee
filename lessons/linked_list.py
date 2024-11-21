
from __future__ import annotations 

class Node:
    value: int 
    next: Node | None

    def __init__ (self, value: int, next: Node | None): 
        self.value = value 
        self.next = next 

    def __str__ (self) -> str: 
        """produce a string representation of a linked list"""
        rest: str = "TODO" # TODO: figure out the rest of the list 
        if self.next is None: 
            rest = "None"
        else: 
            rest = str(self.next)
        return f"{self.value} -> {rest}"

two: Node = Node (2, None)
one: Node = Node (1, two)
courses: Node = Node (110, Node (210, Node (301, None)))
print (one)
print (str(courses))
print (courses)

def to_str (head: Node | None) -> str:
    """represent a linked list as a str"""
    if head is None: 
        return "None"
    else: 
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"
    
print (to_str (one))
print (to_str (courses))

def last (head: Node) -> int: 
    """return the last value of a non-empty list"""
    #Base case: when head is the last node
    if head.next is None: 
        return head.value
    else:
    #recursive case:
        rest: int = last (head.next)
        return rest 

print (last (one)) #expect to print 2 
print (last(courses)) #expect to print 301

def recursive_range (start: int, end: int) -> Node | None: 
    """build a linked list recursively fromt start to end"""

    #raise an exception with string "invalid use of recusive_range" when called improperly 
    #Edge Case! 
    if start > end: 
        raise ValueError ("Invalid use of recursive_range")
    if start == end: 
        return None 
    else:
        #recursive case 
        # intuition: handle the first case based on the specific call 
        first: int = start 
        # build the rest of the list using the builder function recursively 
        rest: Node | None = recursive_range(start + 1, end)
        return Node (first, rest)

a_list: Node | None = recursive_range (110, 150)

print (a_list)
               

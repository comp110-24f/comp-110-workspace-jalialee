from __future__ import annotations 

class Node:
    "this is the Class that would be refered to"
    value: int 
    next: Node | None

    def __init__ (self, value: int, next: Node | None): 
        "initializes"
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
#print (one)
#print (str(courses))
#print (courses)

def to_str (head: Node | None) -> str:
    """represent a linked list as a str"""
    if head is None: 
        return "None"
    else: 
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"
    
#print (to_str (one))
#print (to_str (courses))

def last (head: Node) -> int: 
    """return the last value of a non-empty list"""
    #Base case: when head is the last node
    if head.next is None: 
        return head.value
    else:
    #recursive case:
        rest: int = last (head.next)
        return rest 

#print (last (one)) #expect to print 2 
#print (last(courses)) #expect to print 301

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

#print (a_list)

def value_at (head: Node | None, index: int) -> int:
    "Raises an error if there is no data or returns it at given index"
    if head is None: #if head has no values
        raise IndexError ("Index is out of bounds on the list")
    if index == 0: #if value doesn't exist 
        return head.value
    else: #recursion 
        rest: int = value_at(head.next, index -1) #removes 1 from the index
    return rest

def max (head: Node | None) -> int: 
    "returns max value or raises a value error if empty"
    if head is None: #if head has no values 
        raise ValueError ("Cannot call max with None")
    if head.next is None: #if the value doesn't exist 
        return head.value 
    rest: int = max (head.next) 
    rest_max: int = head.value
    if rest_max < rest:
        rest_max = rest
    return rest_max #returns max value 

def linkify (items: list [int]) -> Node| None: 
    "Returns linked list with list values in same order"
    if len(items)== 0: #returns none if empty list, base case 
        return None 
    head = Node (items [0], linkify(items[1:])) #head is created using Node
    return head 

def scale (head: Node | None, factor: int) -> Node| None: 
    "returns new linked list with values multipled"
    if head is None: #head has none, returns none
        return None 
    else: 
        new_value = factor * head.value #multiplies head.value by factor
        new_head = Node (new_value, None) #replaces head.value with new head value
        new_head.next = scale (head.next, factor) #calls
        return new_head 


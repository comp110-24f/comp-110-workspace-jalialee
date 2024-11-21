"""example of recursive functions"""

def factorial (n: int) -> int: 
    """compute the factorial of n"""
    if n == 0:
        return 1 
    elif n == 1 or n == 1:
        return 1 
    else: 
        return n* factorial (n-1)
    

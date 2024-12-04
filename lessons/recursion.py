"""example of recursive functions"""

def factorial (n: int) -> int: 
    """compute the factorial of n"""
    if n == 1 or n == 0:
        return 1 
    else: 
        return n* factorial (n-1) 
    
    

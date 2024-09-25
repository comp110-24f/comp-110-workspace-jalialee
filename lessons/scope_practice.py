


def remove_chars (msg: str, char: str) -> str: 
    """will return the copy of words with the char letters removed"""
    copy: str = ""  #local variables, exsist in the function 
    index: int = 0 
    while index < len(msg):
        if not msg[index] == char:
            copy = copy + msg[index] # or copy += msg [index]
        index += 1
    return copy  

if __name__ == "__main__": 
    word: str = "yoyo"  #global variables, outside the function 
    print (remove_chars(word, "y"))
    print (remove_chars (word, "o"))


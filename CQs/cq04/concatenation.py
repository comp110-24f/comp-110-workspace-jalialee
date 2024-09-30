__author__ = "730762790"


def concat (str_1 : str, str_2 : str) -> str: # this will add the two words together 
    """this is the main function"""
    return str_1 + str_2 #will return the strings connected 

if __name__ == "__main__": #stops the inputs here from showing when imported 
    word1: str = "happy"
    word2: str = "tuesday"
    print (concat(str_1=word1,str_2=word2))


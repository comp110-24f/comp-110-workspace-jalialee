"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730762790" 

def input_word () -> str: 
    """Takes the inputted word and ensures that it's 5 characters"""
    word_input: str = str(input("Enter a 5-character word: ")) #where you can enter a 5 charactered word 
    if len(word_input) < 5 or len(word_input) > 5: 
        print ("Error: Word must contain 5 characters.")
        exit ()
    return word_input 

def input_letter () -> str: 
    """Takes the inputted letter and ensures it is one letter"""
    letter_input: str = str(input("Enter a single character:")) #where you can enter one letter 
    if len(letter_input) < 1 or len(letter_input) > 1: 
        print ("Error: Character must be a single character.") 
        exit ()
    return letter_input 

def contains_char(word: str, letter: str) -> None: #this function moves throughout the word to check over the characters 
   """Ensures the inputted character matches any of the characters in the inputted word. States the amount of times that specific letter is found."""
   print("Searching for " + letter + " in " + word)
   count_match: int = 0
   if word[0] == letter: #checks if the character at index 0 matches the inputted character, this goes the same for the rest of body of the function. 
       print(letter + " found at index 0")
       count_match += 1 # lets you go through the words to see how many instances it occurs 
   if word[1] == letter:
       print(letter + " found at index 1")
       count_match += 1
   if word[2] == letter:
       print(letter + " found at index 2")
       count_match += 1
   if word[3] == letter:
       print(letter + " found at index 3")
       count_match += 1
   if word[4] == letter:
       print(letter + " found at index 4")
       count_match += 1
   if count_match == 0:
       print("No instances of " + letter + " found in " + word)
   elif count_match == 1:
       print("1 instance of " + letter + " found in " + word)
   else:
       print(str(count_match) + " instances of " + letter + " found in " + word)

def main() -> None:
   contains_char(word=input_word(), letter=input_letter())

if __name__ == "__main__":
    main()
    
#this program will tell you which letter you specified and how many times it appears in the word you inputted along with where index wise

__author__ = "730762790"

def input_guess (lenword: int) -> str:
    """prompts the user to enter the correct length."""
    guess: str = str(input(f"Enter a {lenword} character word: "))
    guess_len: int = len (guess)
    while guess_len != lenword: #loop if the is not equal
        guess = str(input(f"That wasn't {lenword} chars! Try again: "))
        guess_len = len (guess)
    return guess 

def contains_char (word: str, character: str) -> bool: 
    """Checks over the characters of the string with true or false"""
    assert len (character) == 1 
    count: int = 0
    while count < len(word): #this will loop through each character in the string
        if word [count] == character:
            return True 
        count += 1
    return False 

def emojified (guess: str, secret: str) -> str:
    """Compare the two strings of equal length and will provide emojis based on accuracy"""
    assert len (guess) == len (secret) #makes sure that both lengths are equal
    WHITE_BOX: str = "\U00002B1C" #these are the emoji colors 
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    contains_char (WHITE_BOX, "B")
    emoji: str = ""
    count: int = 0 
    while count < len(guess):
        if guess[count] == secret[count]:
            emoji = f"{emoji}{GREEN_BOX}"
        else:
            location: bool = False
            i: int = 0
            while location is not True and i < len(guess):
                if guess[count] == secret[i]:
                    location = True
                else:
                    i += 1
            if location is True:
                emoji = f"{emoji}{YELLOW_BOX}"
            else:
                emoji = f"{emoji}{WHITE_BOX}"
        count += 1
    return emoji  # returns emoji with the different colors

def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # variables being defined 
    win: bool = False
    while turns <= 6 and win is False: # loop to indict the amount of turns and if the word matches the secret 
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        emoji: str = emojified(guess, secret)
        print(emoji)
        if guess == secret:
            win = True
        else:
            turns += 1
    if win is True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret="codes")
    
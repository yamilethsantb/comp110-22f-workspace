"""One-Shot Wordle - Loops!"""
__author__ = "730361444"

secret_word: str = "python"

guess: str = str(input("What is your 6 letter guess? "))

while len(guess) != len(secret_word):
    guess = str(input("That was not 6 letters! Try again: "))
    if len(guess) == len(secret_word) and guess != secret_word:
        print("Not quite. Play again soon!")
if len(guess) == len(secret_word) and guess != secret_word:
    i: int = 0
    s: str = ""
    while i < len(secret_word): 
        if guess[i] == secret_word[i]:
            s = s + "\U0001F7E9"
        if guess[i] != secret_word[i]:
            frequency: int = 0 
            g: bool = False 
            while g != True and frequency < len(secret_word):
                if guess[i] == secret_word[frequency]:
                    g = True
                    s = s + "\U0001F7E8"
                frequency += 1
        if len(s) <= i:
            s = s + "\U00002B1C" 
        i = i + 1
    print(s)
    print("Not quite. Play again soon!")

if guess == secret_word:
    print("\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9")
    print("Woo! You got it!")

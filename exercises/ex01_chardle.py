"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730361444"


choosen_word: str = str(input("Enter a 5-character word: "))
if len(choosen_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(choosen_word) == 0:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = str(input("Enter a single character: "))
if len(letter) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(letter) == 0:
    print("Error: Character must be a single character.")
    exit()
    
print("Searching for " + letter + " in " + choosen_word)
frequency: int = 0
if letter == choosen_word[0]:
    frequency = frequency + 1
    print(letter + " found at index " + "0")
if letter == choosen_word[1]:
    frequency = frequency + 1
    print(letter + " found at index " + "1")
if letter == choosen_word[2]:
    frequency = frequency + 1
    print(letter + " found at index " + "2")
if letter == choosen_word[3]:
    frequency = frequency + 1
    print(letter + " found at index " + "3")
if letter == choosen_word[4]:
    frequency = frequency + 1
    print(letter + " found at index " + "4")
if frequency == 1:
    print("1 instance of " + letter + " found in " + choosen_word)
if frequency == 0:
    print("No instances of " + letter + " found in " + choosen_word)
if frequency == 2: 
    print("2 instances of " + letter + " found in " + choosen_word)
if frequency == 3:
    print("3 instances of " + letter + " found in " + choosen_word)
if frequency == 4: 
    print("4 instances of " + letter + " found in " + choosen_word)
if frequency == 5:
    print("5 instances of " + letter + " found in " + choosen_word)
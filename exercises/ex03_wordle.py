"""Structured Wordle Exercise."""
__author__ = "730361444"


def contains_char(phrase: str, character: str) -> bool:
    """Searches for the character in phrase."""
    assert len(character) == 1
    i: int = 0
    while i < len(phrase):
        if character == phrase[i]:
            return True
        i = i + 1 
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Checks for indices in guess and secret word and provides corresponding emoji."""
    assert len(guess) == len(secret_word)
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    white: str = "\U00002B1C"
    string_boxes: str = ""
    count: int = 0
    while count < len(secret_word):
        if guess[count] == secret_word[count]:
            string_boxes += green
        else:
            if contains_char(secret_word, guess[count]):
                string_boxes += yellow
            else:
                string_boxes += white
        count += 1
    return string_boxes


def input_guess(expected_length: int) -> str:
    """Checks to ensure input is correct length."""
    word: str = str(input("Enter a " + str(expected_length) + " character word: "))
    g = False
    while g != True:  
        if len(word) == expected_length:
            g = True 
        else:
            word = (input("That wasn\'t " + str(expected_length) + " chars! Try again: "))     
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n = 1 
    secret_word: str = "codes"
    the_guess: str = ""
    failure: str = ("X/6 - Sorry, try again tommorow!")
    while n < 7:
        print("=== Turn " + str(n) + "/6" + " ===")
        the_guess += (input_guess(5))
        print(emojified(the_guess, secret_word))
        if the_guess == secret_word:
            return print("You won in " + str(n) + "/6" + " turns!")
        n += 1
        the_guess = "" 
    return print(failure)


if __name__ == "__main__":
    main()
"""Choose your own adventure game."""
___author___ = "730361444"

points: int = 100
player: str = ()


def main() -> None:
    """Game of the Battle Against the Monsters."""
    print("Welcome to Battle Against the Monsters.")
    greet()
    CONSTANT: int = 0 
    print(f"{player}, proceed to choose your weapon.")
    print("A. Sword")
    print("B. Magic Wand")
    print("C. Plz I do not want to fight anymore")
    choice: str = str(input("Choose one [A, B, C]: "))
    assert choice == "A" or "B" or "C"
    global points
    if choice == "A":
        sword_fight()
    if choice == "B":
        points = magic_fight(points)
    if choice == "C":
        print("You surrendered")
        print(f"Points accumulated in battle : {points}")
        exit()
    while points >= CONSTANT:
        EMOJI: str = ("\U0001F7E5")
        print(f"{EMOJI} HEALTH: {points} {EMOJI}")
        print(f"{player}, proceed to choose a different/same weapon.")
        print("A. Sword")
        print("B. Magic Wand")
        print("C. Plz I do not want to fight anymore. Put me out of my misery")
        choice: str = str(input("Choose one [A, B, C]: "))
        assert choice == "A" or "B" or "C"
        if choice == "A":
            sword_fight()
        if choice == "B":
            points = magic_fight(points)
        if choice == "C":
            print("You surrendered")
            print(f"Points accumulated in battle : {points}")
            exit()

    if points <= CONSTANT:
        choice_2: str = str(input("You have lost the battle would you like to play again? Y/N: "))
        assert choice_2 == "Y" or "N"
        if choice_2 == "N":
            print("Thank you for playing. Goodbye")
        else: 
            main()

    
def greet() -> None:
    """Greeting funtion."""
    print("In this game you have to battle a monster. Your health begins at 100 and once reaching 0 you have lost")
    global player 
    player = str(input("What is your name?: "))


def sword_fight() -> None:
    """Sword fight scenerio."""
    import random
    z = random.randint(1, 100)
    CONSTANT_2: int = 0
    MAX: int = 100
    print("You choose the sword")
    print("The ogre is approaching you....Do you")
    print("A. Aim for the ogre's eye")
    print("B. Aim for the ogre's heart")
    choice: str = str(input("Choose one [A or B]: "))
    assert choice == "A" or "B"
    dice: int = random.randint(1, 2)
    global points
    if dice == 1: 
        i_1: int = CONSTANT_2
        i_1 = z
        print(f"The Ogre has been hurt, you have gained points in health: {i_1}")
        if points < MAX:
            points += i_1
    else: 
        i_2: int = CONSTANT_2
        i_2 = z
        print(f"The Ogre gets mad and inflicts damage, you have suffered a loss in points: {i_2}")
        points -= i_2


def magic_fight(x: int) -> int: 
    """Magic fight scenerio."""
    import random
    z = random.randint(1, 100)
    CONSTANT_2: int = 0
    print("You choose the wand")
    print("The ogre is approaching you....Do you")
    print("A. Cast a spell directed at ogre's eyes")
    print("B. Cast a spell directed at ogre's heart")
    dice: int = random.randint(1, 2)
    if dice == 1: 
        i_1: int = CONSTANT_2
        i_1 = z
        print(f"The Ogre has been hurt, you have gained points in health: {i_1}")
        if x < 100:
            x += i_1
    else: 
        i_2: int = CONSTANT_2
        i_2 = z
        print(f"The Ogre gets mad and inflicts damage, you have suffered a loss in points: {i_2}")
        x -= i_2
    return x 


if __name__ == "__main__":
    main()
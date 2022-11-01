"""Choose your own adventure game."""
___author___ = "730361444"


player: str = () 
points: int = 0

def main() -> None:
    CONSTANT: int = 0
    i: bool = False
    r: int = 0
    greet()
    while i != True: 
        global points
        game_one()
        recieved = game_two(points)
        points = recieved
        if points == CONSTANT:
            print("You failed in helping the chicken cross the road would you like to play again? Y/N: ")
            if choice == "Y":
                i = False 
            else:
                i = True 
        else:
            choice: str = str (input("Congratulations! You kept the chicken alive would you like to play again? Y/N: "))
            assert choice == ("Y") or ("N")
            if choice == "Y":
                i = False 
            else:
                i = True 
        r += 1
        print(f"Turns played: {r}")
    print(f"Thank you for playing {player}!")
    exit()







def greet() -> None:
    """Greets the player and requests name."""
    print("Welcome player! This chicken needs help crossing the road!")
    CHICKEN_CONSTANT: str = str("\U0001f414")
    print (CHICKEN_CONSTANT)
    answer: str = str(input("Will you help the chicken cross the road? Y/N:"))
    assert answer == "Y" or "N"
    if answer == "Y":
        global player
        wyn: str = str (input("What is your name player? "))
        player = wyn 
    else: 
        DISAPPOINTMENT: str = str("\U0001F61E")
        print(f"The chicken died crossing the road {DISAPPOINTMENT}")
        print("Goodbye")
        exit ()

def game_one() -> None:
    """First game scenerio."""
    global points 
    points = 0
    POINTS_AWARDED: int = 2
    print(f"{player}! Quick! A snake is approaching the chicken!")
    print("Do you....")
    print("A. Distract the snake")
    print("B. Push the chicken out of the way")
    choice: str = str(input("Choose A or B: "))
    assert choice == "A" or "B"
    print (choice)
    if choice == "A":
        print("While distracting the snake... the chicken stepped onto the road while a car sped by. The chicken's feathers were only ruffled. ")
        points += POINTS_AWARDED
        print("The chicken then decides to sit on the road...and lays an egg then proceeds to continue crossing while a truck approaches")
        print("Do you....")
        print("A. Follow the chicken to ensure safe travels")
        print("B. Grab the egg and let the chicken continue walking")
        choice: str = str(input("Choose A or B: "))
        assert choice == "A" or "B"
        if choice == "A":
            print("You followed the chicken however, at the sound of the egg cracking under the wheels of the truck the chicken turns around returns to orginal edge of road.")
            points += POINTS_AWARDED
        else:
            print("You grabbed the egg however, and right at the moment the chicken crosses the road it turns around at full speed towards you. It starts pecking your feet.")
            points += POINTS_AWARDED
    else:
        print("Congrulations! you pushed the chicken out of the snakes way... only to push it towards a stampede of jogging college frat bros...")
        points += POINTS_AWARDED
        print("Do you....")
        print("A. Yell out to the stampede to stop")
        print("B. Run to get the chicken")
        choice_two: str = str(input("Choose A or B: "))
        assert choice_two == "A" or "B"
        print (choice_two)
        if choice_two == "A":
            print("Whew, shockingly they heard you and they jogged around the chicken")
            points += POINTS_AWARDED
        else: 
            print("Along with the chicken you also get trampled... however you kept the chicken safe. Eventhough you suffered major bruises.")
            points += POINTS_AWARDED


def game_two(x: int) -> int: 
    global player
    print(f"{player}, you've helped the chicken avoid grave injuries so far however you still haven't helped the chicken cross the road..")
    print("That is the objective of the game afterall but thanks for keeping the chicken alive.")
    print("You spot a crossing guard just ahead...")
    print("Do you....")
    print("A. Ask to borrow the crossing guard's stop sign")
    print("B. Jaywalk across the street with the chicken in your hand")
    choice_three: str = str(input("Choose A or B: "))
    assert choice_three == "A" or "B"
    print (choice_three)
    if choice_three == "A":
        print("The crossing guard thinks you're covering their shift for them. So, now you have to help the children cross the street instead")
        print("Do you....")
        print("A. Ask a child to carry the chicken across the street")
        print("B. Carry chicken across yourself")
        if choice_three == "A":
            print("The chicken pecks the child's hand midway crossing the road. The child screams scaring the chicken. The chicken crosses the road")
            return x
        else:
            print("You decide to carry the chicken yourself when there are no pedestrians waiting to be crossed. However, the chicken runs from you onto the street. The chicken is then picked up by an eagle.")
            x = 0
            return x 
    else: 
        print("You twist your ankle running over the pothole in the middle of the road. The chicken flys out your hand and lands a few away .")
        print("You spot a farmer walking on the side of the road")
        print("Do you....")
        print("A. Ask for help")
        print("B. Crawl to the chicken to grab them and cross the road")
        choice_four: str = str(input("Choose A or B: "))
        assert choice_four == "A" or "B"
        print (choice_four)
        if choice_four == "A":
            print("The farmer doesn't hear your cry for help. Turns out he had airpods in. However, he picks up the chicken and places it on the sidewalk.However, leaves you on the middle of the street. ")
            return x
        else: 
            print("You attempt to crawl but an eagle beats you and takes the chicken away.")
            x = 0 
            return x 



if __name__ == "__main__":
    main()
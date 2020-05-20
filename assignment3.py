def rock_paper_scissors():
    import random

    comp_choice = random.choice(("r", "p", "s"))
    your_choice = input("Choose rock (r), paper (p) or scissors (s): ")

    if your_choice != "r" and your_choice != "p" and your_choice != "s":
        print("This was not a valid choice")
        exit()
    print(comp_choice)

    if (comp_choice == "r" and your_choice == "p") \
            or (comp_choice == "p" and your_choice == "s")\
            or (comp_choice == "s" and your_choice == "r"):
        print("You lost!")
    else:
        print("You won!")


def guess_a_number():
    import random

    number = random.randint(1, 100)
    guess = int(input("Guess a number: "))

    while True:
        if guess == number:
            print("Correct!")
            break
        elif guess < number:
            guess = int(input("Your number is too small. Guess again: "))
        else:
            guess = int(input("Your number is too large. Guess again: "))



while True:
    game = int(input("What game do you want to play?\n - 'Guess a number (1)'\n - 'Rock, Paper, Scissors (2)'\n - "))

    if game == 1:
        while True:
            guess_a_number()
            again = input("Do you want to play another round? (y/n): ")
            if again == "n":
                break
            elif again != "n" and again != "y":
                print("Well, I'll take that as a no")
                break
    elif game == 2:
        while True:
            rock_paper_scissors()
            again = input("Do you want to play another round? (y/n): ")
            if again == "n":
                break
            elif again != "n" and again != "y":
                print("Well, I'll take that as a 'no'")
                break
    else:
        print("Invalid Argument")
        break

    another_game = input("Do you want to play another game? (y/n): ")
    if another_game == "n":
        break
    elif another_game != "y" and another_game != "n":
        print("I'll take that as a 'no'")



from random import randint

player_life = 3
computer_life = 3
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
print("Computer chooses: ", computer)
print("You have only", player_life, "lives!")
print("And Computer have only", computer_life, "lives!")

while player is False:
    print("Choose your wapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses:", player)

    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
            player_life -= 1
            print("You have lost 1 life! Now you have: ", player_life, "lives!")
        else:
            print("You win!", player, "smashes", computer)
            computer_life -= 1
            print("Computer has lost 1 life! Now computer has: ", computer_life, "lives!")

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            player_life -= 1
            print("You have lost 1 life! Now you have: ", player_life, "lives!")
        else:
            print("You win!", player, "covers", computer)
            computer_life -= 1
            print("Computer has lost 1 life! Now computer has: ", computer_life, "lives!")

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            player_life -= 1
            print("You have lost 1 life! Now you have: ", player_life, "lives!")
        else:
            print("You win!", player, "cuts", computer)
            computer_life -= 1
            print("Computer has lost 1 life! Now computer has: ", computer_life, "lives!")

    elif player == "Quit":
        exit()

    else:
        print("Not a valid optin. Chack again, and check your spelling!\n")

    # calculate the lifes
    if player_life == 0:
        print("-----You lose all your lifes! Game is over!-----")
        game_again = input("Do you want to play the game again? (Y/N): ")
        if game_again == "Y":
            continue
        else:
            exit()

    elif computer_life == 0:
        print("-----The computer lose all his lifes! Game is over!-----")
        game_again = input("Do you want to play the game again? (Y/N): ")
        if game_again == "Y":
            continue
        else:
            exit()

    player = False
    computer = choices[randint(0, 2)]
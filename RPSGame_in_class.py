from random import randint

player_lives = 5
computer_lives = 5

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# define a win and lose in function

def winorlose(status):
    print("Called the win or loser function")
    print("**********************************")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N: ")

    if choice == "Y" or choice == "y":
        # reset the game
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice == "n":
        print("You chose to quit")
        exit()


while player is False:
    print("=====================================================")
    print("Player Lives: ", player_lives, "/5")
    print("Computer Lives: ", computer_lives, "/5")
    print("=====================================================")
    print("Choose your wapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    # print("Player chooses:", player)

    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player, "\n")
            player_lives -= 1

        else:
            print("You win!", player, "smashes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player, "\n")
            player_lives -= 1

        else:
            print("You win!", player, "covers", computer, "\n")
            computer_lives -= 1


    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player, "\n")
            player_lives -= 1

        else:
            print("You win!", player, "cuts", computer, "\n")
            computer_lives -= 1


    elif player == "Quit":
        exit()

    else:
        print("Not a valid optin. Chack again, and check your spelling!\n")

    if player_lives is 0:
        winorlose("lost")

    elif computer_lives is 0:
        winorlose("won") 

        # handle win and lose
    # if player_lives is 0:
    #     print("*****************************************************")
    #     print("You lost! Would you like to play again?")
    #     choice = input("Y / N?")
    #     print(choice)

    #     if choice == "Y" or choice == "y":
    #         player_lives = 5
    #         computer_lives = 5
    #         player = False
    #         computer = choices[randint(0, 2)]
    #     if choice == "n" or choice == "N":
    #         print("you quit!")
    #         print("**************************************************")
    #         exit()

    # elif computer_lives is 0:
    #     print("*****************************************************")
    #     print("You won! Would you like to play again?")
    #     choice = input("Y / N?")
    #     print(choice)

    #     if choice == "Y" or choice == "y":
    #         player_lives = 5
    #         computer_lives = 5
    #         player = False
    #         computer = choices[randint(0, 2)]
    #     if choice == "n" or choice == "N":
    #         print("you quit!")
    #         print("**************************************************")
    #         exit()

    player = False
    computer = choices[randint(0, 2)]
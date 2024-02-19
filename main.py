import game


ask = ""
while ask != "N":
    ask = input("Would you like to play a game? Y/N ")

    if ask == "Y":
        name1 = input("Insert player 1's name: ")
        name2 = input("Insert player 2's name: ")
        howLong = int(input("How many seconds do you need per round? "))
        game1 = game.game(name1, name2, howLong)
        game1.playGame()

    elif ask == "N":
        print("Maybe next time...")
    else:
        print("Please enter Y/N")


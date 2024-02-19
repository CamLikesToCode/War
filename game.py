import player
import time

class game:
    def __init__(self, name1, name2, sleep):
        print('Game is starting!')
        self.sleep = sleep
        self.p1 = name1
        self.p2 = name2
        self.player1 = player.Player()
        self.player1.playerDeck.Shuffle()
        self.player2 = player.Player()
        self.player2.playerDeck.Shuffle()



    def War(self):
        warCards = []
        warCards2 = []
        for i in range (4):
            if len(self.player1.playerDeck.cards) >= 2:
                warCards.append(self.player1.getTopCard())
                self.player1.playerDeck.cards.pop(0)

        for i in range (4):
            if len(self.player2.playerDeck.cards) >= 2:
                warCards2.append(self.player2.getTopCard())
                self.player2.playerDeck.cards.pop(0)
        winner = self.Compare()


        if winner == 1:
            print(self.p1 + " got " + str(warCards) + " and " + str(warCards2))
            for i in warCards:
                self.player1.playerDeck.cards.append(i)
            for i in warCards2:
                self.player1.playerDeck.cards.append(i)
            return 1

        elif winner == 2:
            print(self.p2 + " got " + str(warCards) + " and " + str(warCards2))
            for i in warCards:
                self.player2.playerDeck.cards.append(i)
            for i in warCards2:
                self.player2.playerDeck.cards.append(i)
            return 2

    # Comparing top cards
    def Compare(self):
        topCard = self.player1.getTopCard()
        print("")
        print(self.p1 + "'s card is: "+ str(topCard) + ".")
        topCard2 = self.player2.getTopCard()
        print("")
        print(self.p2 + "'s card is: " + str(topCard2) + ".")



        if topCard > topCard2:
            self.player1.playerDeck.cards.append(topCard2)
            self.player1.playerDeck.cards.append(topCard)
            print("")
            print(self.p1 + ' won!')
            self.player2.playerDeck.cards.pop(0)
            self.player1.playerDeck.cards.pop(0)


            return 1


        elif topCard2 > topCard:
            self.player2.playerDeck.cards.append(topCard)
            self.player2.playerDeck.cards.append(topCard2)
            print(self.p2 + ' won!')
            self.player2.playerDeck.cards.pop(0)
            self.player1.playerDeck.cards.pop(0)


            return 2

        else:
            print("War")
            return self.War()



    def printCardCount(self):
        print("")
        print(str(len(self.player1.playerDeck.cards)) + " cards in " + self.p1 + "'s deck")

    def playGame(self):
        while len(self.player1.playerDeck.cards) != 0 and len(self.player2.playerDeck.cards) != 0:
            time.sleep(self.sleep)
            self.Compare()
            self.printCardCount()

        if len(self.player1.playerDeck.cards) == 0 and  len(self.player2.playerDeck.cards) != 0:
            print(self.p2 + " won!")
            print("")

        else:
            print(self.p1 + " won!")
            print()
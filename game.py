import player
import time


class game:
    def __init__(self):
        print('Game is starting!')
        self.player1 = player.Player()
        self.player1.playerDeck.Shuffle()
        self.player2 = player.Player()
        self.player2.playerDeck.Shuffle()



    def War(self):
        warCards = []
        warCards2 = []
        for i in range (4):
            warCards.append(self.player1.getTopCard())

            self.player1.playerDeck.cards.pop(0)
        for i in range (4):
            warCards2.append(self.player2.getTopCard())
            self.player2.playerDeck.cards.pop(0)
        winner = self.Compare()

        if winner == 1:
            print("Player 1 got " + str(warCards) + " and " + str(warCards2))
            for i in warCards:
                self.player1.playerDeck.cards.append(i)
            for i in warCards2:
                self.player1.playerDeck.cards.append(i)
            return 1
                            #FIXME ungroup gained cards
        elif winner == 2:
            print("Player 2 got " + str(warCards) + " and " + str(warCards2))
            for i in warCards:
                self.player2.playerDeck.cards.append(i)
            for i in warCards2:
                self.player2.playerDeck.cards.append(i)
            return 2

    # Comparing top cards
    def Compare(self):
        topCard = self.player1.getTopCard()
        print("Player 1s' card is: "+ str(topCard) + ".")
        topCard2 = self.player2.getTopCard()
        print("Player 2s' card is: " + str(topCard2) + ".")



        if topCard > topCard2:
            self.player1.playerDeck.cards.append(topCard2)
            self.player1.playerDeck.cards.append(topCard)
            print('Player 1 won!')
            self.player2.playerDeck.cards.pop(0)
            self.player1.playerDeck.cards.pop(0)


            return 1


        elif topCard2 > topCard:
            self.player2.playerDeck.cards.append(topCard)
            self.player2.playerDeck.cards.append(topCard2)
            print('Player 2 won!')
            self.player2.playerDeck.cards.pop(0)
            self.player1.playerDeck.cards.pop(0)


            return 2

        else:
            print("War")
            return self.War()



    def printCardCount(self):
        print(str(len(self.player1.playerDeck.cards)) + " cards in Player 1s' deck")
        print(str(len(self.player2.playerDeck.cards)) + " cards in Player 2s' deck")




game1 = game()
game1.Compare()
game1.printCardCount()
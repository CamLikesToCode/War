import player
import time


class game:
    def __init__(self):
        print('Game is starting!')
        self.player1 = player.Player()
        self.player1.playerDeck.Shuffle()
        self.player2 = player.Player()
        self.player2.playerDeck.Shuffle()


    #Comparing top cards
    def Compare(self):

        topCard = self.player1.getTopCard()
        print("Player 1s' card is: "+ str(topCard) + ".")
        topCard2 = self.player2.getTopCard()
        print("Player 2s' card is: " + str(topCard2) + ".")

        if topCard > topCard2:
            self.player1.playerDeck.cards.append(topCard2)
            self.player1.playerDeck.cards.append(topCard)
            print('Player 1 won!')


        elif topCard2 > topCard:
            self.player2.playerDeck.cards.append(topCard)
            self.player2.playerDeck.cards.append(topCard2)
            print('Player 2 won!')


        else:

            print("War")


        self.player2.playerDeck.cards.pop(0)
        self.player1.playerDeck.cards.pop(0)

    def War(self):
        warCards = []
        for i in range (3):
            warCards.append(self.player1.getTopCard())

        first1 = self.player1.getTopCard(self)
        second1 = self.pla


game1 = game()
game1.Compare()
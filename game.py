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
        for i in range (3):
            warCards.append(self.player1.getTopCard())
            self.player1.playerDeck.cards.pop(0)
        for i in range (3):
            warCards2.append(self.player2.getTopCard())
            self.player2.playerDeck.cards.pop(0)
        self.Compare()
        # FIXME We don't know where to give the six war cards to

    # Comparing top cards
    def Compare(self):
        topCard = self.player1.getTopCard()
        print("Player 1s' card is: "+ str(topCard) + ".")
        topCard2 = self.player2.getTopCard()
        print("Player 2s' card is: " + str(topCard2) + ".")
        self.War()

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
            #self.War()
            # FIXME War is called before popping, the final card after war will be
            # FIXME the same as the card that cause war.

        self.player2.playerDeck.cards.pop(0)
        self.player1.playerDeck.cards.pop(0)


game1 = game()
game1.Compare()
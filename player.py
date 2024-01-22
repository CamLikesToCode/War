import deck

class Player:
    def __init__(self):
        self.playerDeck = deck.deck()

    def getTopCard(self):
        return self.playerDeck.cards[0]


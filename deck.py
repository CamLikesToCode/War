import card
import random
class deck:
    def __init__(self):
        self.cards = []
        for i in range(4): #Suits: Club, Spade, Heart, Diamond
            for j in range(13): #Numbers
                #print("i: " + str(i) + "  j: " + str(j))

                self.cards.append(card.card(i, j))

    def Shuffle(self):
        random.shuffle(self.cards)

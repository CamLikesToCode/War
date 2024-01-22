class card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        suitStr = ""
        if self.suit == 0:
            suitStr = "Hearts"
        if self.suit == 1:
            suitStr = "Spades"
        if self.suit == 2:
            suitStr =  "Diamonds"
        if self.suit == 3:
            suitStr = "Clubs"


        return str(self.number) + " of " + suitStr


    def __lt__(self, other):
        return self.number < other.number

# self = left side #other = right side
    def __gt__(self, other):
        return self.number > other.number

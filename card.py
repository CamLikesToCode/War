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

        if self.number < 11:
            return str(self.number) + " of " + suitStr

        elif self.number == 11:
            return "Jack of " + suitStr

        elif self.number == 12:
            return "Queen of " + suitStr

        elif self.number == 13:
            return "King of " + suitStr

        else:
            return "Ace of " + suitStr


    def __lt__(self, other):
        return self.number < other.number

# self = left side #other = right side
    def __gt__(self, other):
        return self.number > other.number

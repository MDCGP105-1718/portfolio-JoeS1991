import random

class Card(object):

    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return Card.values[self.value] + " of " + Card.suits[self.suit]

testcard = Card(0, 6)
print(testcard)

class Deck(object):

    def __init__(self):
        self.deck = []

        for suits in range(4):
            for values in range(13):
                self.deck.append(Card(suits, values))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_hand(self):
        print(self.deck[:5])
        del self.deck[:5]

deck = Deck()

card = deck.deck[random.randint(0,51)]
print(card)


class Hand(Deck):

    def __init__(self):
        self.hand = []

        for i in range(5):
            self.hand.append(Deck())


    def __str__(self):
        return str(self.hand)

hand = Hand()

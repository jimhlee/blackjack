import random

print('War. War never changes.')

# Making a deck class
class Deck(object):
    suits = ['Hearts','Spades','Clubs','Diamonds']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10,'Jack','Queen','King','Ace']

    def __init__(self):
        self.cardlist = []
        for suit in self.suits:
            for value in self.values:
                self.cardlist.append(Card(suit,value))
        self.shuffle()

    def draw_card(self):
        return self.cardlist.pop()

    def shuffle(self):
        random.shuffle(self.cardlist)

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.str_value = str(value)
        self.num_value = self.converter(value)

    def __repr__(self):
        return self.str_value + self.suit

# I could hard code this it would be a series of if statements... but it seems shitty to do so
    def converter(self, value):
        if value in ['Jack', 'Queen', 'King', 'Ace']:
            return 10

class Player(object):
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def clear_hnd(self):
        self.hand = []

    def score_hnd(self):
        score = 0
        for card in self.hand:
            score += card.num_value
        return score

class Game(object):
    def __init__(self, player):
        self.player = player
        self.opponent = opponent
        self.deck = Deck()

    def start(self):

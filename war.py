import random

print('This is Blackjack')

# Making a deck class
class Deck(object):
    suits = ['H','S','C','D']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A']

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

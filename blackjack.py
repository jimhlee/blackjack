# Blackjack

print 'This is Blackjack'

# Making a deck class
class Deck(object):
    suits = ['H','S','C','D']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A']


    def __init__(self):
        self.cardlist = []
        for suit in self.suits:
            for value in self.values:
                self.cardlist.append(Card(suit,value))

        self.shuffle

    def __repr__(self):
        return 'More like my DICK'

    def shuffle(self):
        pass

    # def converter(self):
    #     if self.value == 'J' or 'Q' or 'K':
    #         return 10
    #
    #     elif self.value == 'A'
    #         return 11

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.str_value = str(value)
        self.num_value = self.converter(value)

    def __repr__(self):
        return self.str_value + self.suit

    def converter(self, value):
        if value in ['J', 'Q', 'K']:
            return 10
        elif value == 'A':
            return 11
        else:
            return value

class Player(object):

    def __init__(self, money):
        self.hand = []

    def draw(self, hand):
        pass

    def clear_hnd(self, hand):
        pass

    def score_hnd(self, hand):
        pass

# class Dealer(Player):
#     def __init__(self):
#         super().__init__(0)
#
#

        # if player.score < 21:
        #     print ('You\'re at' + {player.score} + '.')
        #     #  Prompt if they haven't busted
        #
        # elif player.score == 21:
        #     return "Blackjack, you win!"
        #     # Prompt if you win
        #
        # elif player.score > 21 and hand.card.value == 11
        #     return 1
        #     # Solving the Ace problem?
        #
        # else
        #     return "Bust, you lose!"
        #     # Prompt if you lose



class Game(object):
    # player goes first
    # dealer win ties
    # score compare
    # play game

    def __init__(self, player):
        pass

    def play_game(self):
        pass

    def play_round(self):
        pass




#
# if __name__ == '__main__':
#     my_deck = Deck()

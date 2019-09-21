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


    def __repr__(self):
        pass
        # This is how we show people their cards
    def get_hand(self):
        for card in hand:
            print(card)

    def shuffle(self):
        random.shuffle(deck)
        # Not sure the random method that should be used here, but this is where the deck can be shuffled


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
            # This is where the hand lies

    def draw(self, hand):
        pass
        # This appends to the hand

    def clear_hnd(self, hand):
        return self.hand = []
        pass

    def score_hnd(self, hand):
        # This is where the hand values get added up
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



playing_game = True

class Game(object):
    while playing_game:

    # player goes first
    # Is player.input a thing? or is it player(input)?
    # dealer win ties
        if player.score == dealer.score:
            print('Tie! Dealer Wins!')
            return
    # score compare
    # play game
        # Play again?

    def __init__(self, player):
        pass

    def play_game(self):
        # is this where the while game_playing is true should be?
        pass

    def play_round(self):
        pass




#
# if __name__ == '__main__':
#     my_deck = Deck()

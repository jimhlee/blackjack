# Blackjack

print 'This is Blackjack'

# Making a deck class
class Deck(object):
    # Gives a deck attributes
    suits = ['H','S','C','D']
            # a deck has these values
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K','A']

    def Converter(self):
        if self.value == 'J' or 'Q' or 'K':
            return 10

        elif self.value == 'A'
            return 11

# boop
    def __init__(self):
        # a deck has these suits
        # self.suits = ['H','S','C','D']
        # # a deck has these values
        # self.values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        # #
#        self.make_deck()

#    def make_deck(self):
        self.cardlist = []
        for suit in self.suits:
            for value in self.values:
                self.cardlist.append(Card(suit,value))

        self.shuffle

    def __repr__(self):
        return 'More like my DICK'

    def shuffle(self):
        pass

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + self.suit



class Player
    def __init__(self, hand, score, bet)

        def hand(self, cards)
            cards = []
                if

        if player.score < 21:
            print ('You\'re at' + {player.score} + '.')
            #  Prompt if they haven't busted

        elif player.score == 21:
            return "Blackjack, you win!"
            # Prompt if you win

        elif player.score > 21 and hand.card.value == 11
            return 1
            # Solving the Ace problem?

        else
            return "Bust, you lose!"
            # Prompt if you lose

            if player_in:
        response = int(raw_input('Hit or stay? (Hit = 1, Stay = 0)'))
        # If the player asks to be hit, take the first card from the top of
        # deck and add it to their hand. If they ask to stay, change
        # player_in to false, and move on to the dealer's hand.
        if response:
            player_in = True
            new_player_card = deck.pop()
            player_hand.append(new_player_card)
            print 'You draw %s' % new_player_card
        else:
            player_in = False

# Class Game
#
# if __name__ == '__main__':
#     my_deck = Deck()

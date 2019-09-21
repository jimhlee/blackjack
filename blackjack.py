# Blackjack
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

    def __repr__(self):
        pass
        # This is how we show people their cards

    # def get_hand(self):
    #     for card in hand:
    #         print(card)
    # Moved for clarity

    def shuffle(self):
        random.shuffle(self.cardlist)
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
        self.money = money

    def dollaz(self, bet):
        self.money -= bet

    def draw(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def get_hand(self):
        for card in hand:
            print(card)

    def clear_hnd(self):
        self.hand = []

    def score_hnd(self):
        score = 0
        for card in self.hand:
            score += card.num_value
        return score

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
    def __init__(self, player):
        self.player = player
        self.deck = Deck()
        self.dealer = Player(0)

    def play_game(self):
        playing_game = True
        while playing_game:
            self.play_round()
            keep_playing = input('Would you like to keep playing? (y/n)')
            playing_game = keep_playing == 'y'
        # if deck.len < 10:
    def bet_prompt(self):
        ante = 10
        while True:
            bet = int(input('How much money would you like to bet?'))
            if bet > self.player.money:
                print('Money fail', self.player.money, bet)
                continue
            if bet < ante:
                print(f'Ante fail, you bet {bet}, you must bet at least {ante}')
                continue
            break

        self.player.dollaz(bet)
        print(f'You bet {bet}, you have {self.player.money} left')
        return bet
            # if bet > money
            # if bet < ante
            #
        # while self.player.bet > self.player.money:
        #     print('Can\'t bet that much, you only have f.()')


    def play_round(self):
        # repeat for dealer
        # determine winner
        # reapportion money
        # clear hand
        # play again?
        bet = self.bet_prompt()
        for i in range(2):
            self.player.draw(self.deck)
        print(f'You have {self.player.hand}')
        for i in range(2):
            self.dealer.draw(self.deck)
        print(f'The dealer is showing {self.dealer.hand[0]}')

        while True:
            score = self.player.score_hnd()
            if score >= 21:
                break
            is_hit = input('Would you like to hit? (y/n)')
            if is_hit == 'n':
                break
            self.player.draw(self.deck)










if __name__ == '__main__':
    my_deck = Deck()
    my_player = Player(100)
    play = Game(my_player)

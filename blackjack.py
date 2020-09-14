# Blackjack
import time
# This will import just BlackjackDeck
from cardstuff import BlackjackDeck
# import cardstuff <- this will import the entire module
# and you call it with cardstuff.BlackjackDeck
# do not do this -> from cardstuff import *

print('This is Blackjack')

class Player(object):
    def __init__(self, money):
        self.hand = []
        self.money = money

    def dollaz(self, bet):
        self.money -= bet

    def draw(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def clear_hnd(self):
        self.hand = []

    # self.hand is being called from the player class, but card.num_value is being called from the card instance THROUGH
    # the player class. It has acces because a hand(player attribute) is full of cards.
    def score_hnd(self):
        score = 0
        for card in self.hand:
            score += card.num_value
        # The below is the same thing as the block of code which comes after, just better and shorter
        # n_aces = sum([1 if card.num_value == 11 else 0 for card in self.hand])
        if score <= 21:
            return score

        n_aces = sum([1 for card in self.hand if card.num_value == 11])

        # This is literally saying <if n_aces == 0> do nothing
        if not n_aces:
            return score

        for _ in range(n_aces):
            score -= 10
            if score <= 21:
                return score

        # is_ace_lst = []
        # for card in self.hand:
        #     if card.num_value == 11:
        #         is_ace = 1
        #     else:
        #         is_ace = 0
        #     is_ace_lst.append(is_ace)
        #     print(self.hand, is_ace_lst)
        # n_aces = sum(is_ace_lst)
        return score

    # def ace_changer(self):
    #     self.player.player_score -= 10

class Game(object):
    def __init__(self, player):
        self.player = player
        self.deck = BlackjackDeck()
        self.dealer = Player(0)
        print(f'Ring-a-ding-ding baby! Welcome to the Tops, here\'s {player.money} caps courtesy of the chairmen! Have a good time!')
        self.play_game()

    def play_game(self):
        while True:
            if self.player.money < 10:
                print('You don\'t have enough caps to play! Get out you vagrant!')
                return
            self.play_round()
            print(f'You currently have {self.player.money} caps')
            keep_playing = input('Would you like to keep playing? (y/n)')
            if keep_playing != 'y':
                print('Come back to the Tops anytime!')
                return

    def bet_prompt(self):
        ante = 10
        while True:
            bet = int(input('How much money would you like to bet?'))
            if bet > self.player.money:
                print('Money fail', self.player.money, bet)
                continue
            if bet < ante:
                print(f'Ante fail, you bet {bet} caps, you must bet at least {ante} caps')
                continue
            break

        self.player.dollaz(bet)
        print(f'You bet {bet} dollars, you have {self.player.money} caps left')
        return bet

    def play_round(self):
        bet = self.bet_prompt()
        for i in range(2):
            self.player.draw(self.deck)
        print(f'You have {self.player.hand}')
        for i in range(2):
            self.dealer.draw(self.deck)
        print(f'The dealer is showing {self.dealer.hand[0]}')

        # This while loop has explicit break conditions.
        while True:
            player_score = self.player.score_hnd()
            if player_score >= 21:
                break
            print(f'You are at {player_score}, you have {self.player.hand} in your hand')
            is_hit = input('Would you like to hit? (y/n)')
            if is_hit == 'n':
                break
            self.player.draw(self.deck)

        # FOR BUSTERS ONLY
        if player_score > 21:
            # if card.suit == 'A' in self.player.hand:
            #     ace_changer()
            # else:
            print(f'You\'re a loser! You had {self.player.hand} and it was bad!')
            self.clean_up()
            return

        # This is the loop for the dealer
        while True:
            dealer_score = self.dealer.score_hnd()
            if dealer_score >= 17:
                break
            print(f'The dealer is at {dealer_score}, and has {self.dealer.hand} in their hand')
            time.sleep(2)
            self.dealer.draw(self.deck)

        if dealer_score > 21:
            print(f'The dealer has busted! Gross! They had {self.dealer.hand} and their total was {dealer_score}')
            self.clean_up()
            #  The += operator adds the second quantity to the first(a = a + b => a += b)
            self.player.money += bet * 2
            return

        print(f'The dealer is at {dealer_score} and has {self.dealer.hand}')
        print(f'You are at {player_score} and have {self.player.hand}')

        if dealer_score >= player_score:
            print('Dealer wins!')
        else:
            print(f"You win {bet * 2} dollars! You're such a stud")
            self.player.money += bet * 2
        self.clean_up()
        return

    def clean_up(self):
        self.deck.check_deck()
        self.player.clear_hnd()
        self.dealer.clear_hnd()

# Below is an alternate way to construct while loops with implicit break conditions
        # keep_playing = True
        #
        # while keep_playing:
        #     player_score = self.player.score_hnd()
        #     if player_score >= 21:
        #         keep_playing = False
        #     print(f'You are at {player_score}')
        #     is_hit = input('Would you like to hit? (y/n)')
        #     if is_hit == 'n':
        #         keep_playing = False
        #     self.player.draw(self.deck)


if __name__ == '__main__':
    my_player = Player(100)
    play = Game(my_player)

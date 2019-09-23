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
        self.deck = Deck()
        self.dealer = Player(0)
        print(f'Welcome you big stud, here\'s {player.money} dollars! Don\'t blow it!')

    def play_game(self):
        while True:
            if self.player.money < 10:
                print('You don\'t have enough money to play! Get out you vagrant!')
                return
            self.play_round()
            print(f'You currently have {self.player.money} dollars')
            keep_playing = input('Would you like to keep playing? (y/n)')
            if keep_playing != 'y':
                print('Come back to the Tops anytime!')
                return
        # if deck.len < 10:
    def bet_prompt(self):
        ante = 10
        while True:
            bet = int(input('How much money would you like to bet?'))
            if bet > self.player.money:
                print('Money fail', self.player.money, bet)
                continue
            if bet < ante:
                print(f'Ante fail, you bet {bet} dollars, you must bet at least {ante} dollars')
                continue
            break

        self.player.dollaz(bet)
        print(f'You bet {bet} dollars, you have {self.player.money} dollars left')
        return bet
            # if bet > money
            # if bet < ante
            #
        # while self.player.bet > self.player.money:
        #     print('Can\'t bet that much, you only have f.()')


    def play_round(self):
        # determine winner
        # reapportion money
        # play again?
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
            print(f'You a loser! You had {self.player.hand} and it was bad!')
            self.clean_up()
            return

        # This is the loop for the dealer
        while True:
            dealer_score = self.dealer.score_hnd()
            if dealer_score >= 17:
                break
            print(f'The dealer is at {dealer_score}, and has {self.dealer.hand} in their hand')
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
        # possibly create a new deck here too
        self.player.clear_hnd()
        self.dealer.clear_hnd()

        # if player.score > dealer.score:
        #     input('You win! would you like to play again? (y/n)')
        #
        # else:
        #     input('You lose! Would you like to play again (y/n)')


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
    my_deck = Deck()
    my_player = Player(100)
    play = Game(my_player)

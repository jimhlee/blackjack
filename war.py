import random
from cardstuff import WarDeck

print('War. War never changes.')

class WarPlayerDeck(object):
    '''
    This is the war player deck
    '''
    def __init__(self):
        self.drawpile, self.spoils = [], []

    @property
    def n_cards(self):
        return len(self.drawpile) + len(self.spoils)

    def draw_card(self):
        # If you have no cards do this
        if self.n_cards == 0:
            # every return implicitly returns a none, it just works that way
            return None
        # This assumes you have cards in your spoils
        if len(self.drawpile) == 0:
            self.drawpile = self.spoils
            self.shuffle()
            self.spoils = []
        return self.drawpile.pop()

    def shuffle(self):
        random.shuffle(self.drawpile)

    def add_to_spoils(self, cards):
        if isinstance(cards, list):
            self.spoils.extend(cards)
        else:
            self.spoils.append(cards)
        

class Game(object):
    def __init__(self):
        new_war_deck = WarDeck()
        self.player_deck = WarPlayerDeck()
        self.opponent_deck = WarPlayerDeck()
        # enumerate is used almost exclusively in for loops
        for i, card in enumerate(new_war_deck.cardlist):
            if i % 2:
                self.player_deck.add_to_spoils(card)
            else:
                self.opponent_deck.add_to_spoils(card)
    # player_deck = WarPlayerDeck(my_war_deck.cardlist[:26])
    # opponent_deck = WarPlayerDeck(my_war_deck.cardlist[26:])

    def start_game(self):
        # TODO:Make this part work!
        #  print(The Romans waged war to gather slaves and wealth.
        #  Spain built an empire from its lust for gold and territory.
        #  Hitler shaped a battered Germany into an economic superpower.
        #
        #  But war never changes.
        #
        #  In the 21st century, war was still waged over the resources that could be acquired.
        #  Only this time, the spoils of war were also its weapons: Cards.)
        begin_play = input('Would you like to play War? (y/n)')
        if begin_play != 'y':
            print('The courier rode off into the sunset, his war unfinished.')
            return

        while True:
            print(f'The deck sizes are: {self.player_deck.n_cards}, & \
                 {self.opponent_deck.n_cards}.')
            if  self.player_deck.n_cards > 0 and self.opponent_deck.n_cards > 0:
                self.play_round()
            else:
                # TODO: print who the winnner is here
                print('Game Over')
                break

    def play_round(self):
        player_hand, opponent_hand = [],[]
        player_hand.append(self.player_deck.draw_card())
        opponent_hand.append(self.opponent_deck.draw_card())
        print(player_hand, opponent_hand)
        # this part handles the actual wars
        while True:
            if player_hand[-1] < opponent_hand[-1]:
                self.opponent_deck.add_to_spoils(player_hand + opponent_hand)
                return
            elif player_hand[-1] > opponent_hand[-1]:
                self.player_deck.add_to_spoils(player_hand + opponent_hand)
                return
            elif player_hand[-1] == opponent_hand[-1]:
                for card in range(4):
                    player_card = self.player_deck.draw_card()
                    opponent_card = self.opponent_deck.draw_card()
                    if player_card is not None:
                        player_hand.append(player_card)
                    if opponent_card is not None:
                        opponent_hand.append(opponent_card)
                print(f'\n\n\n This is the player hand: {player_hand}.')
                print(f'...and this is the opponent hand: {opponent_hand}.\n\n\n')

if __name__ == "__main__":
    player_deck = WarPlayerDeck()
    my_game = Game()
    my_game.start_game()
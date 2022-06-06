from Deck import Deck
from Hand import Hand
from Player import Player
from Dealer import Dealer

class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        
    def place_bet(self):
        while True:
            bet = float(input("Please place your bet:"))
            
            if bet > self.player.balance:
                print(f"Over your balance ${self.player.balance} please re-enter your bet")
            elif bet < self.MINIMUM_BET:
                print(f"Mininum bet is {self.MINIMUM_BET}")
            else:
                self.bet = bet
                self.player.balance -= bet
                break
    
    def get_player_hit_or_stay(self):
        while True:
            hit_or_stay = input("Do you want to hit or stay?: ").lower()

            if hit_or_stay in ["hit", "stay"]:
                break

            print("Invalid respond hit or stay")

        return hit_or_stay == "hit"
    
    def player_turn(self):
        while True:
            hit = self.get_player_hit_or_stay()

            if not hit:
                break
            
            new_card = self.deck.deal(1)[0]
            self.player.hit(new_card)

            print("You are dealt with:" + str(new_card))
            print("You now have:" + str(self.player.hand.get_value()))

            if self.player.hand.get_value() > 21:
                return True
        return False

    def deal_starting_cards(self):
        self.player.hand = Hand(self.deck.deal(2))
        self.dealer.hand = Hand(self.deck.deal(2))
        self.dealer.hand.cards[1].hidden = True
        print(f'Dealer:{str(self.dealer.hand)}')

        print(f'Player: {self.player.hand.get_value()}, {str(self.player.hand)}')

    def dealer_turn(self):
        self.dealer.hand.cards[1].hidden = False
        print(f'{self.dealer.hand.get_value()}')

        while self.dealer.hand.get_value() <= 16:
            new_card = self.deck.deal(1)[0]

            self.dealer.hit(new_card)

            print("Dealer dealt with:" + str(new_card))
            print(f'Dealer: {self.dealer.hand.get_value()}, {str(self.dealer.hand)}')

        if self.dealer.hand.get_value() > 21:
            return True
        
        return False
    




if __name__ == "__main__":
    ali = Dealer()
    ken = Player(100)

    g1 = Game(ken, ali)

    g1.deal_starting_cards()
    g1.dealer_turn()
    


        
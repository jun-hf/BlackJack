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
        self.bet = Deck()
        
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


if __name__ == "__main__":
    ali = Dealer()
    ken = Player(100)

    g1 = Game(ken, ali)

    g1.place_bet()
    print(g1.player.balance)
    print(g1.get_player_hit_or_stay())
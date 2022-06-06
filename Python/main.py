from Player import Player
from Dealer import Dealer
from Game import Game

STARTING_BALANCE = 500

player = Player(STARTING_BALANCE)
dealer = Dealer()
game = Game(player, dealer)

print("Welcome to Blackjack")
game.start_game()
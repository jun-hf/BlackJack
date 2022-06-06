# Design a BlackJack game 

## Specification
1. One player 
2. One Dealer
3. Player has balance, when balance is over the game is over
4. Dealer has unlimited money to give
5. A game can have mutliple rounds of Blackjack, until the player balance is zero

### Dealer
- Instance variable
    - hand (class)

- Instance method
    - get_hand (method that return the hand of the dealer)
    - hit(card) (allows the dealer to add one card to their hand) -> accept card variable

### Player << Dealer
- Instance variable
    - inherit from the dealer class
    - has an additional method that is balance

### Card
- Class Variable
    - suit -> a dictionary of suit
    - value -> a dictionary of card value from A to K
- Instance Variable
    - suit
    - value
    - hidden (boolean)

- Instance Method
    - str (dunder)
        - it return the str of the card suit and value
        - if hidden is true, return unkown

### Deck
- Instance Variable
    - cards []-> a list of card

- Instance Method
    - shuffle -> import random.shuffle that allows you to shuffle an array which is our cards variable

    - create -> create a full deck 

    - deal(num_cards) -> with num_cards it will throw out the amount of cards from the top of the deck

- __init__
    - create self.cards = [] to store your card
    - call create
    - call shuffle

### Hand
- Instance Variable
    - cards -> array of class Card

- Instance Method
    - get_value -> is an method that return all your value in your cards [array]instance
    - add -> allows you to add card to self.card
    
    - str(dunder)
        - return all your str cards in self.cards  

### Game
- Class Variable
    - MINIMUM_BET = 1
- Instance Variable
    - player
    - dealer
    - bet amount
    - deck

- Initialize 
    1. player
    2. dealer
    3. bet 
    4. deck


- Instance Method
    - place_bet
        - Use a while loop to keep prompting the users
        - Ask player to place the bet
        - Check if the player's balance 
        - Check for minimum bet also
        - if everything is fine, minus the player's balance and update the self.bet

    - get_player_hit_or_stay (true if player want to hit)
        - while loop to keep asking player
        - ask players if they want to hit or not
        - break the while loop if the respond is hit or stay
        - respond input not valid if the respond is not (hit or stay)
        - return true if the respond is hit
    - deal_starting_cards
        - create deal two cards and put it into Hand class
        - set one of the dealre's hand card to unknown
        - print the dealer and the player's card
    - player_turn
        - in this method, when the player's turn they get to hit or stay
        - when they players hit and over 21 return true (lost)
        - when players under 21 and stay return false
        - while true to keep protmpt
        - invoke the get_player_stay_or_hit method
        - if is hit then we give a card to players and show the updated value
        - if the value is > 21 return true
    - dealer_turn
        - set the dealer's unkown card to false
        - show the players the dealer hand
        - as long as the dealer has less then = 16
            - give the dealer a card
            - print the new card
            - add the card and show the value to the players
        - if the value is more then 21 return true if not return false
    - handle_blackjack
        - if the players has no black jack return false
        - if the dealer has blackjack and u too  then return the bet and print statemewnt saying you bopth win
        - add the player's balance times 2.5 
        - print you win!!
        - return true
    - reset_round
        - create a new deck 
        - set the player and dealer's hand to none and also the bet
    - determine_winner
        - store the player's and dealer's value
        - three situations
            - you have more then dealer, you win
            - dealer have more then you dealer win
            - else return bet no one's win
    - confirm_start
        - prompt the users if they want to start win the bet
    - start_round
        - prompt to place bet
        - deal card
        - if blackjack return
        - if player.turn()
        - lost

        - determine_winner()
        - reset_round()
    - start_game
        - as long as the player has more then the balance 0 then ask player's if they want to play
        - if no play then tell them they left the game if how much money
        - break the while loop
        - start round again
        
        - if balance less then 0 then print the player loss the game.

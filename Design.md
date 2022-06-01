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

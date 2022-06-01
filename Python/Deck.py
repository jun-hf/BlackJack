from random import shuffle
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create()
        self.shuffle()

    def create(self):
        """
        - To create one card, Card(1, 8) heart 8

        - Two for loop, the first one goes until 3 for the suit, second one is for value

        - Then append it to self.cards
        
        """
        for i in range(4):
            for j in range(1, 15):
                new_card = Card(i, j)
                self.cards.append(new_card)

    def shuffle(self):
        pass

    def deal(self):
        pass


if __name__ == "__main__":
    deck_01 = Deck()
    print(deck_01.cards[0])
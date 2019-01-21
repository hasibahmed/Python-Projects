""" Contains type card, suit, deck, multiple decks
"""

import random


class Card():

    """ Creates a card with its rank and value
        Attributes:
            rank (str): rank of the card
            value (int): value associated with the rank
    """

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):

        return f"{self.suit}-{self.rank}({self.value})"


class Suit(Card):

    """ Contains a collection of cards of different rank that belong to a suite.
    """

    default_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                      'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, ranks, values=default_values):
        self.suit = suit
        self.ranks = ranks
        self.values = values
        self.cards = []
        for rank in self.ranks:
            self.cards.append(Card(self.suit, rank, self.values[rank]))
            # self.cards.append(super().__init__(rank, Suit.values[rank]))

    def __str__(self):

        __cards = [card.__str__() for card in self.cards]
        return ', '.join(__cards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):

        if self.index < len(self.cards):
            __card = self.cards[self.index]
            self.index += 1
            return __card
        else:
            raise StopIteration()


class Deck(Suit):

    """ Contains 4 different suites
    """
    suits = ('Diamonds', 'Hearts', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    default_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                      'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, values=default_values):
        self.values = values
        self.deck = []
        for suit in Deck.suits:
            __cards = Suit(suit, self.ranks, self.values)
            for __card in __cards:
                self.deck.append(__card)

    def __str__(self):
        __cards = [suit.__str__() for suit in self.deck]
        return ', '.join(__cards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.deck):
            __card = self.deck[self.index]
            self.index += 1
            return __card
        else:
            raise StopIteration()

    def shuffle(self):
        """ Randomly shuffles the position of the cards in the deck
        """

        random.shuffle(self.deck)


if __name__ == "__main__":

    print(f"{'*'*20}")
    ace = Card('Spades', 'A', 11)
    print(ace)
    print(f"{'*'*20}")

    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
              'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    spades = Suit('Spades', ranks, values)
    print(spades)
    print(f"{'*'*20}")
    for card in spades:
        print(card)
    print(f"{'*'*20}")

    cards = Deck()
    for card in cards:
        print(card)
    print(f"{'*'*20}")
    print(cards)
    print(f"{'*'*20}")
    cards.shuffle()
    print(f'after shuffle: {cards}')
    print(f"{'*'*20}")

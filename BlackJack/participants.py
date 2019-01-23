""" Contains participants in black jack
"""


class Participant():
    """ Participants in black jack
    """

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        """ Adds card to the hand from the deck
        """
        self.hand.append(card)

    def score(self):
        """Returns participants score adjusting for the Aces
        """

        score = 0
        nAce = 0
        for __card in self.hand:
            if __card.rank != 'Ace':
                score += __card.value
            else:
                nAce += 1
        for _ in range(nAce):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1

        return score

    def busts(self):
        """ Returns True if a participants hand
            exceeds 21
        """

        return True if self.score() > 21 else False

    def __str__(self):
        __cards = [__card.__str__() for __card in self.hand]
        return f"{self.name}'s hand :" + ', '.join(__cards)

    def show_hand(self):
        """ Shows participants full hand 
        """
        print(self)


class Player(Participant):

    """ Class for players 
    """

    def __init__(self, name, bet, balance=100):
        self.balance = balance
        self.bet = bet
        super().__init__(name)

    def win_bet(self):
        """ Return players blanance after a win
        """

        self.balance += 2 * self.bet
        return self.balance

    def lose_bet(self):
        """ Return players balance after a loss
        """

        self.balance -= self.bet
        return self.balance


class Dealer(Participant):

    """ Class for dealer
    """

    def __init__(self):
        super().__init__('Dealer')

    def show_hand(self, hole=False):
        """ introduce hole card for dealer
            only display the first card if 
            hole is True
        """
        if hole:
            print(f"{self.name}'s hand: {self.hand[0]}")
        else:
            super().show_hand()

    def hit(self):
        """ Decides when the dealer stops drawing cards
        """
        return True if self.score() <= 17 else False


if __name__ == "__main__":

    p1 = Player('Dylan', 10)
    print(p1)

    import cards

    deck = cards.Deck()
    deck.shuffle()
    p1.add_card(deck.draw())
    p1.add_card(deck.draw())
    print(f'{p1.score()}')

    p1.show_hand()

    dealer = Dealer()
    dealer.add_card(deck.draw())
    dealer.add_card(deck.draw())

    dealer.show_hand(hole=True)
    dealer.show_hand()

    print(dealer.hit())

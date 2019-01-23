""" A game of simplified blackjack
    between a player and a dealer
"""
import cards
import participants


def add_card_to_hand(participant, deck, number=2):
    """ adds number of cards to either player's or dealer's hand
        from deck
    """
    for _ in range(number):
        participant.add_card(deck.draw())


def get_bool(prompt):
    """ returns input as boolean
    """
    while True:
        try:
            return {'y': True, 'n': False}[input(prompt).lower()]
        except KeyError:
            print('Invalid input. Please enter Y/N ')


def check_win_loss(player, dealer):
    if player.score() > 21:
        return True
    elif dealer.score() > 21:
        return True
    elif player.score() == dealer.score():
        print('Its a tie!')
        return True
    elif player.score() > dealer.score():
        print(f'{player.name} wins!')
        return True
    elif player.score() < dealer.score():
        print(f'{dealer.name} wins!')
        return True
    else:
        return False


def main():

    while True:
        print('Welcome to BlackJack!')
        player_name = input('Enter the name of the player: ')
        player_bet = input('Enter the amount you wish to bet: ')
        player = participants.Player(player_name, player_bet)
        dealer = participants.Dealer()
        print('Will use only a single deck of cards. Shuffling...')
        deck = cards.Deck()
        deck.shuffle()
        print('Done.')

        # deal 2 cards to the player
        add_card_to_hand(player, deck, 2)

        # deal 2 cards to the dealer
        add_card_to_hand(dealer, deck, 2)

        # display players hand
        player.show_hand()
        # display dealers hand but not the hole card
        dealer.show_hand(hole=True)

        # if play wants to hit deal a card
        while True:
            hit = get_bool('Hit or Stay (Y/N) ? ')
            if not hit:
                break
            add_card_to_hand(player, deck, 1)
            player.show_hand()
            if player.busts():
                print(f'{player.name} busts!')
                break

        # Dealers turn:
        # show the hole card
        dealer.show_hand()

        # dealer hits till score > 17
        if not player.busts():
            while dealer.hit():
                add_card_to_hand(dealer, deck, 1)
                dealer.show_hand()
                if dealer.busts():
                    print(f'{dealer.name} busts!')
                    break
        check_win_loss(player, dealer)
        if not get_bool('Want to play again ? (Y/N): '):
            break


if __name__ == "__main__":
    main()

#!/usr/bin/env python
import random


def display_board(board=[str(i) for i in range(0, 10)]):

    print('\n'*5)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')


def player_input(player1, player2):
    markers = {}
    marker1 = ''
    while not marker1 == 'X' and not marker1 == 'O':
        marker1 = input(
            "Player {}: please choose 'X' or 'O' ? ".format(player1))

    marker2 = 'O' if marker1 is 'X' else 'X'
    print('Player {} marker: {}  Player {} marker: {}'.format(
        player1, marker1, player2, marker2))
    markers[player1] = marker1
    markers[player2] = marker2
    return markers


def place_marker(board, marker, position):
    board[int(position)] = marker
    return board


def win_check(board, mark):
    ''' create the winning combination
        and check if there is one 
    '''
    h = [board[i:3+i] for i in [1, 4, 7]]
    v = [board[i:7+i:3] for i in [1, 2, 3]]
    d1 = [board[1:10:4]]
    d2 = [board[3:8:2]]

    win_combinations = h+v+d1+d2

    for i in range(0, len(win_combinations)):
        if len(set(win_combinations[i])) <= 1:
            if win_combinations[i][0] == mark:
                return True
    return False


def choose_first():
    first = random.randint(1, 2)
    return first


def space_check(board, position):
    position = int(position)
    return not (board[position] == 'X' or board[position] == 'O')


def full_board_check(board):
    for i in range(1, len(board)):
        if space_check(board, i):
            return False
    return True


test_board = [0, 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'X']
full_board_check(test_board)


def player_choice(board, player):

    next_play = input('{} : What is your move ? '.format(player))
    while not space_check(board, int(next_play)):
        next_play = input(
            'That position is already taken. Please choose a different move: ')
    return int(next_play)


def replay():
    play = input('Choose Y to play, N to exit ')
    return True if play.lower() == 'y' else False


def main():
    ''' Game of tic tac toe '''

    print('Welcome to Tic Tac Toe!')
    print('Instructions:\n Choose the corresponding key to pick your position on the board\n\t')
    display = display_board()
    print(display)
    play = replay()
    pass

    while play:
        # Set the game up here
        player1 = input('Enter first player name: ')
        player2 = input('Enter second player name: ')
        if choose_first() == 2:
            player1, player2 = player2, player1
        print('Player {} goes first!'.format(player1))
        markers = player_input(player1, player2)
        board = [str(i) for i in range(0, 10)]

        full_board = False
        winner1 = False
        winner2 = False

        while not winner1 and not winner2 and not full_board:
            # Player 1 Turn
            move1 = player_choice(board, player1)
            board = place_marker(board, markers[player1], move1)
            display_board(board)

            full_board = full_board_check(board)
            winner1 = win_check(board, markers[player1])
            winner2 = win_check(board, markers[player2])

            if winner1 or winner2 or full_board:
                break

            # Player2's turn.
            move2 = player_choice(board, player2)
            board = place_marker(board, markers[player2], move2)
            display_board(board)

            full_board = full_board_check(board)
            winner1 = win_check(board, markers[player1])
            winner2 = win_check(board, markers[player2])

        if full_board and not winner1 and not winner2:
            print('\n\t Evenly matched! its a draw.')
        elif winner1:
            print('\n\t {} is the winner! CONGRATULATIONS!!'.format(player1))
        elif winner2:
            print('\n\t {} is the winner! CONGRATULATIONS!!'.format(player2))

        if not replay():
            break


if __name__ == "__main__":
    main()

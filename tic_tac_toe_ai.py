from tic_tac_toe import *


def tic_tac_ai(a_board):
    found_a_move = False
    for i in range(3):
        for j in range(3):
            if a_board.board[i][j] == '-':
                found_a_move = True
                a_board.add_token('O', i, j)
                break
        if found_a_move:
            break
    if not found_a_move:
        raise Exception('No legal move exists')


if __name__ == '__main__':
    a_board = Board()
    while (True):
        a_board.human_move()
        a_board.print_board()
        if a_board.is_board_full():
            break
        tic_tac_ai(a_board)
        a_board.print_board()
        if a_board.is_board_full():
            break

class Board:
    BOARD_SIZE = 3

    def __init__(self):
        self.board = [['-' for i in range(3)] for j in range(3)]

    def add_token(self, token, x, y):
        self.board[x][y] = token

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end='')
                if j < 2:
                    print('|', end='')
            print()
        print()

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    def human_move(self):
        while (True):
            data = [int(i) for i in input().strip().split()]
            if self.board[data[0]][data[1]] != '-':
                print("please input again")
            else:
                break
        self.add_token('X', data[0], data[1])


if __name__ == '__main__':
    a_board = Board()
    a_board.print_board()
    a_board.add_token('X', 0, 1)
    a_board.print_board()

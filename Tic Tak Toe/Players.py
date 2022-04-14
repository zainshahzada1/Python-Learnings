import random
import math


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.curreny_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')

    def print_board_nums(self):
        number_board = [[str(i)for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')

    def availible_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #                           ==
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot==' ':
        #         moves.append(i)
        # return moves

    def empty_square(self):
        return ' ' in self.board

    def num_empty_square(self):
        return len(self.board.count(' '))

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.curreny_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagnal1 = [self.board[i]for i in [0, 4, 8]]
            if all([spot == letter for spot in diagnal1]):
                return True
            diagnal2 = [self.board[i]for i in [2, 4, 6]]
            if all([spot == letter for spot in diagnal2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        TicTacToe.print_board_nums(game)
    letter = 'X'
    while game.empty_square(game):
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.getmove(game)
    if game.make_move(square, letter):
        if print_game:
            print(letter + f'makes a move to square{square}')
            game.print_board()
            print('')
            if game.current_winner():
                if print_game:
                    print(letter + 'wins!')
                return letter
        letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print("it's a tie!")



class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move():
        pass


class randomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move():
        square=random.choice(TicTacToe.availible_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter + 'turn.Input move(1,9)')
            try:
                val=int(square)
                if val not in TicTacToe.availible_moves():
                    raise ValueError
            except ValueError:
                print('Invalid Square.Try Again!')
        return val


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = randomComputerPlayer('O')
    t = TicTacToe
    play(t, x_player, o_player, print_game=True)

from user import HumanPlayer, RandomComputerPlayer
from colorama import Fore


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # list to rep board
        self.current_winner = None  # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod  # which number corresponds with each box
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print(('| ' + ' | '.join(row) + ' |'))

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):  # if valid move make move
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):  # check winner

        row_ind = square // 3  # check row
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3  # check col
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:  # check diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:  # return winner
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():  # iterate while empty square
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + Fore.GREEN + f' make a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'o' if letter == 'X' else 'X'  # alter letter after move

    if print_game:
        print('It\'s a tie!')


def main_tic():

    while True:
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('o')
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)
        break

    play_again_option = input(
        'Would you like to play again? (Y/N)\n').strip().upper()
    if play_again_option == 'Y':
        main_tic()
    elif play_again_option == 'N':

        print(Fore.GREEN + 'Thanks for playing! \n')
    else:
        print('Invalid choice \n')

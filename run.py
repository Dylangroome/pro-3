class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3:(1+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')
    @staticmethod
    def print_board_nums():
        number_board = [[strg(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(('| ' + ' | '.join(row) + ' |'))

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

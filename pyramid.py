# Group: Irvin Rafael, Joshua Villareal
# CPSC481-02
# June 26, 2023
# Project 2 Pyramid TicTacToe
from games import *

class Pyramid(TicTacToe):
    """Play Pyramid TicTacToe, with Max (first player) playing 'X'.
    A state has the player to mo(ve, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""
    def __init__(self, h=3, v=5, k=3):
        super().__init__(h, v, k)
        moves = [(x, y) for x in range(1, h + 1)
                for y in range(x, (v-(x-1))+ 1)]
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

    def compute_utility(self, board, move, player):
        """If player wins with this move with less moves in board, then it has a higher/lower utility"""
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return (100-len(board)) if player == 'X' else (-100+len(board))
        else:
            return 0

if __name__ == "__main__":
    pyramid = Pyramid()  # Creating the game instance
    print(pyramid.initial.moves) # must be [(1,1), (1,2), (1,3), (1,4), ...]
    utility = pyramid.play_game(minmax_player, query_player) # computer moves first 
    if (utility == 0):
        print("TIED game")
    elif (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
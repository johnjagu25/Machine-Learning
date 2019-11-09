# Design a Tic-Tac-Toe game played between two players on an n x n grid. 
# A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid. 
# A player who succeeds in placing n of their marks in a horizontal, diagonal, or 
# vertical row wins the game. Once a winning condition is reached, the game ends and 
# no more moves are allowed. Below is an example game which ends in a winning condition:
import numpy as np
class TicTacToe(object):
    def show(self):
        print(self.board)

    def __init__(self, n):
        self.fill_length = 0
        self.n = n
        self.anyWinner = False
        self.board = np.array([['-' for col in range(n)] for row in range(n)])
        # Fill this in.

    def move(self, row, col, player):
        self.fill_length += 1
        self.board[row,col] = player
        if self.fill_length > 4:
            win_count = 0
            row_win = 0
            col_win = 0
            diag_win = 0
            for r in range(self.n):
                if self.board[r,col] == str(player):
                    row_win += 1
                if self.board[row,r] == str(player):
                    col_win +=1
                if self.board[r,r] == str(player):
                    diag_win += 1
            if row_win == self.n or col_win == self.n or diag_win == self.n:
                self.anyWinner = True
                print("player {} wins at {} turn".format(player,self.fill_length))
        if self.fill_length == self.n * self.n and not self.anyWinner:
            print("Game is draw.")

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(2, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
board.move(0, 1, 1)
board.move(1, 2, 2)
board.move(1, 1, 1)
board.show()

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(1, 2, 2)
board.move(0, 1, 1)
board.move(2, 1, 2)
board.move(0, 2, 1)
board.show()

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 1, 2)
board.move(0, 2, 1)
board.move(1, 1, 2)
board.move(1, 2, 1)
board.move(2 , 1, 2)
board.show()
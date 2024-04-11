import os

from const import *
from board import Board
from piece import *
from square import Square


class fenBuilder:
    def __init__(self):
        self.fen = []
        self.empty_squares = 0
        
    def write_fen(self, board):
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col].has_piece():
                    piece = board.squares[row][col].piece
                    self.fen.append(piece.fenLetter)
                if self.fen[-1] in range(0, 8):
                    self.empty_squares += 1
                    self.fen.append(str(self.empty_squares))
        self.fen = '/'.join(self.fen)
        print(self.fen)
import os

class Piece:
    
    def __init__(self, name, color, value, fenLetter=None, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        if color == 'white':
            if name == 'pawn':
                self.fenLetter = 'P'
            if name == 'rook':
                self.fenLetter = 'R'
            if name == 'bishop':
                self.fenLetter = 'B'
            if name == 'knight':
                self.fenLetter = 'N'
            if name == 'queen':
                self.fenLetter = 'Q'
            if name == 'king':
                self.fenLetter = 'K'
        else:
            if name == 'pawn':
                self.fenLetter = 'p'
            if name == 'rook':
                self.fenLetter = 'r'
            if name == 'bishop':
                self.fenLetter = 'b'
            if name == 'knight':
                self.fenLetter = 'n'
            if name == 'queen':
                self.fenLetter = 'q'
            if name == 'king':
                self.fenLetter = 'k'
        
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )
        
    def add_move(self, move):
        self.moves.append(move)
    
    def clear_moves(self):
        self.moves = []
        
class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        self.turn_where_set_true = None
        super().__init__('pawn', color, 10)
        
class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 30)
        
class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 32)
        
class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 50)
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 90)

class King(Piece):
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 900)
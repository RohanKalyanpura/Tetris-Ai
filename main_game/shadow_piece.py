from piece import Piece
from helpers import valid_space

class ShadowPiece(Piece):
    def __init__(self, piece):
        super().__init__(piece.x, piece.y, piece.shape)
        self.color = (128, 128, 128)  # Shadow color

    def update_position(self, grid):
        while valid_space(self, grid):
            self.y += 1
        self.y -= 1

from enum import Enum


class PieceType(Enum):
  PAWN = "P"
  KNIGHT = "N"
  BISHOP = "B"
  ROOK = "R"
  QUEEN = "Q"
  KING = "K"


class Side(Enum):
  WHITE = 1
  BLACK = 2


POINTS = {
  PieceType.PAWN: 1,
  PieceType.KNIGHT: 3,
  PieceType.BISHOP: 3,
  PieceType.ROOK: 5,
  PieceType.QUEEN: 9,
  PieceType.KING: 1000,
}

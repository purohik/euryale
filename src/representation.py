from constants import PieceType, Side


class Piece:
	def __init__(self, piece_type=None, side=None) -> None:
			self.type = piece_type
			self.side = side


class Board:
	"""
	We use the square-centric chess board representation.
	"""

	def __init__(self) -> None:
		self.board = [
			[
				Piece(PieceType.ROOK, Side.BLACK),
				Piece(PieceType.KNIGHT, Side.BLACK),
				Piece(PieceType.BISHOP, Side.BLACK),
				Piece(PieceType.QUEEN, Side.BLACK),
				Piece(PieceType.KING, Side.BLACK),
				Piece(PieceType.BISHOP, Side.BLACK),
				Piece(PieceType.KNIGHT, Side.BLACK),
				Piece(PieceType.ROOK, Side.BLACK),
			],
			[
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
				Piece(PieceType.PAWN, Side.BLACK),
			],
			[Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
			[Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
			[Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
			[Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
						[
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
				Piece(PieceType.PAWN, Side.WHITE),
			],
			[
				Piece(PieceType.ROOK, Side.WHITE),
				Piece(PieceType.KNIGHT, Side.WHITE),
				Piece(PieceType.BISHOP, Side.WHITE),
				Piece(PieceType.QUEEN, Side.WHITE),
				Piece(PieceType.KING, Side.WHITE),
				Piece(PieceType.BISHOP, Side.WHITE),
				Piece(PieceType.KNIGHT, Side.WHITE),
				Piece(PieceType.ROOK, Side.WHITE),
			],
    ]
	
	def display(self) -> None:
		for rank in self.board:
			for piece in rank:
				if piece.type:
					text = piece.type.value if piece.side == Side.WHITE else piece.type.value.lower()
					print(text, end=' ')
				else:
					print('.', end=' ')
			print()
	
	def posiition_to_index(self, pos: str) -> tuple[int, int]:
		'''
		Given a chess-notation position, returns the index on the board.
		'''
		pass
	
	def index_to_position(self, pos: tuple[int, int]) -> str:
		'''
		Given the index on the board, returns the chess-notation position.
		'''
		pass


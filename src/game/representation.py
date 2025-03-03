from constants import PieceType, Side


class Piece:
	def __init__(self, piece_type: PieceType=None, side: Side=None) -> None:
			self.type = piece_type
			self.side = side

DEBUG_PIECE = Piece(PieceType.DEBUG, Side.DEBUG)
EMPTY = Piece()

class Board:
	"""
	We use the square-centric chess board representation.
	"""

	def __init__(self) -> None:
		'''
		The board is arranged in the format where black pieces are on the thop and white pieces are on the bottom. In terms of index, first two rows of the board are black pieces and last two rows are white.
		'''
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
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
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
	
	def position_to_index(self, pos: str) -> tuple[int, int]:
		'''
		Given a chess-notation position, returns the index on the board.
		'''
		col = int(ord(pos[0]) - ord('a'))
		row = 8 - int(pos[1])
		return (row, col)
	
	def index_to_position(self, pos: tuple[int, int]) -> str:
		'''
		Given the index on the board, returns the chess-notation position.
		'''
		rank = chr(ord('a') + pos[1])
		file = str(8 - pos[0])
		return rank + file
	
	def move_piece(self, start: str, end: str) -> bool:
		start_row, start_col = self.position_to_index(start)
		end_row, end_col = self.position_to_index(end)
		piece = self.board[start_row][start_col]
		if piece == EMPTY:
			print('Invalid move:', start, 'to', end)
			return False
		
		self.board[end_row][end_col] = piece
		self.board[start_row][start_col] = EMPTY
		return True


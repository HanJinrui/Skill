from itertools import product
WHITE = -1
BLACK = 1
FREE = 0
SIZE = 4
EMPTY = (FREE, -1)

def within_bounds(y, x):
	return 0 <= y < 4 and 0 <= x < 4
COORDINATES = tuple(product(range(4), repeat=2))
DIRECTIONS = {'Q': [(y, x) for (y, x) in product([-1, 0, 1], repeat=2) if y or x], 'N': [(y, x) for (y, x) in product([-2, -1, 1, 2], repeat=2) if (y + x) % 2], 'B': list(product([-1, 1], repeat=2)), 'R': [(y, x) for (y, x) in product([-1, 0, 1], repeat=2) if (y + x) % 2]}

def generate_moves():
	board = [[None] * 4 for _ in range(4)]
	for (y, x) in COORDINATES:
		d = {}
		for (piece, directions) in DIRECTIONS.items():
			piece_moves = []
			for (dy, dx) in directions:
				(ny, nx) = (y, x)
				piece_directions = []
				for _ in range(3):
					ny += dy
					nx += dx
					if not within_bounds(ny, nx):
						break
					piece_directions.append((ny, nx))
				piece_moves.append(piece_directions)
			d[piece] = piece_moves
		board[y][x] = d
	return board
MOVES = generate_moves()

def sequential_moves(player, piece, y, x, board):
	for direction in MOVES[y][x][piece]:
		for (y, x) in direction:
			owner = board[y][x][0]
			if owner == player:
				break
			yield (piece, y, x)
			if owner != FREE:
				break

def pawn_moves(player, other, y, x, board):
	y += player
	if y % 3:
		if x > 0 and board[y][x - 1][0] == other:
			yield ('P', y, x - 1)
		if x < 3 and board[y][x + 1][0] == other:
			yield ('P', y, x + 1)
		if board[y][x] == EMPTY:
			yield ('P', y, x)
	else:
		if x > 0 and board[y][x - 1][0] == other:
			yield ('R', y, x - 1)
			yield ('B', y, x - 1)
			yield ('N', y, x - 1)
		if x < 3 and board[y][x + 1][0] == other:
			yield ('R', y, x + 1)
			yield ('B', y, x + 1)
			yield ('N', y, x + 1)
		if board[y][x] == EMPTY:
			yield ('R', y, x)
			yield ('B', y, x)
			yield ('N', y, x)

def play(player, player_locations, other, other_locations, board, turns_left):
	for (y, x) in player_locations:
		(_, src_piece) = board[y][x]
		if src_piece == 'P':
			gen = pawn_moves(player, other, y, x, board)
		else:
			gen = sequential_moves(player, src_piece, y, x, board)
		for (to_piece, to_y, to_x) in gen:
			existing = board[to_y][to_x]
			if existing[1] == 'Q':
				return player == WHITE
			if turns_left == 1:
				continue
			board[to_y][to_x] = (player, to_piece)
			board[y][x] = EMPTY
			to_loc = {(to_y, to_x)}
			res = play(other, other_locations - to_loc, player, player_locations - {(y, x)} | to_loc, board, turns_left - 1)
			board[to_y][to_x] = existing
			board[y][x] = (player, src_piece)
			if res and player == WHITE:
				return True
			elif not res and player == BLACK:
				return False
	return player == BLACK

def read_pieces(owner, board, n):
	locations = set()
	for _ in range(n):
		(t, x, y) = input().split()
		x = ord(x) - ord('A')
		y = abs(int(y) - 4)
		board[y][x] = (owner, t)
		locations.add((y, x))
	return locations
for i in range(int(input())):
	(w, b, m) = (int(x) for x in input().split())
	board = [[EMPTY] * 4 for _ in range(4)]
	white_locations = read_pieces(WHITE, board, w)
	black_locations = read_pieces(BLACK, board, b)
	m = m - (m % 2 == 0)
	print('YES' if play(WHITE, white_locations, BLACK, black_locations, board, m) else 'NO')

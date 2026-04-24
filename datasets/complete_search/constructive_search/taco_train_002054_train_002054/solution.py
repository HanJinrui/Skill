import random
N = 8
t = int(input())

def under_attack(i, j):
	global queen_x, queen_y
	return i == queen_x or j == queen_y or i + j == queen_x + queen_y or (i - j == queen_x - queen_y)

def str_to_move(s: str):
	(x, y) = (0, 0)
	if s.endswith('Right'):
		y += 1
	elif s.endswith('Left'):
		y -= 1
	if s.startswith('Down'):
		x += 1
	elif s.startswith('Up'):
		x -= 1
	return (x, y)

def get_next_king_move():
	return str_to_move(input())
while t > 0:
	t -= 1
	(queen_x, queen_y) = (0, 0)
	(king_x, king_y) = (0, 0)
	possible_king_positions = [[True] * N for i in range(N)]
	knock_out = False
	while True:
		print(queen_x + 1, queen_y + 1, flush=True)
		(mx, my) = get_next_king_move()
		if mx == my == 0:
			knock_out = True
			break
		king_x += mx
		king_y += my
		possible_next_move = []
		for i in range(N):
			for j in range(N):
				if under_attack(i, j) and (i != queen_x or j != queen_y):
					possible_next_move += [[i, j]]
		for i in range(N):
			for j in range(N):
				(x, y) = (i + king_x, j + king_y)
				possible_king_positions[i][j] &= 0 <= x < N and 0 <= y < N and (not under_attack(x, y))
		if sum((sum(row) for row in possible_king_positions)) == 1:
			for i in range(N):
				for j in range(N):
					if possible_king_positions[i][j]:
						king_x += i
						king_y += j
			break
		(queen_x, queen_y) = random.choice(possible_next_move)
	if not knock_out:
		assert queen_x != king_x
		queen_x = king_x
		while True:
			print(queen_x + 1, queen_y + 1, flush=True)
			(mx, my) = get_next_king_move()
			if mx == my == 0:
				break
			king_x += mx
			king_y += my
			queen_x += mx
			queen_y += 1 if queen_y < king_y else -1

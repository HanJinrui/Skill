def memoize(func):
	pool = {}

	def wrapper(*arg):
		if arg not in pool:
			pool[arg] = func(*arg)
		return pool[arg]
	return wrapper
mod = 1000000007
for case in range(int(input())):
	(Y, X) = map(int, input().split())
	mx = [int(''.join(('0' if c == '.' else '1' for c in input().rstrip())), 2) for i in range(Y)]
	full = (1 << X) - 1

	def is_wall(x, y):
		return mx[y] & 1 << x != 0 if 0 <= x < X and 0 <= y < Y else True

	def get_free(mx):
		y = 0
		while y < Y and mx[y] == full:
			y += 1
		if y == Y:
			return (None, None)
		free = 0
		while mx[y] & 1 << free != 0:
			free += 1
		if free >= X:
			return (None, None)
		return (free, y)

	def place_queen(x, y, mx):
		nmx = list(mx)
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				if dx == 0 and dy == 0:
					continue
				(cx, cy) = (x, y)
				while not is_wall(cx, cy):
					nmx[cy] |= 1 << cx
					(cx, cy) = (cx + dx, cy + dy)
		return tuple(nmx)

	@memoize
	def rec(mx):
		(free_x, free_y) = get_free(mx)
		if free_x == None:
			return 0
		imx = list(mx)
		imx[free_y] |= 1 << free_x
		ans = rec(tuple(imx))
		nmx = place_queen(free_x, free_y, mx)
		ans += 1
		(free_x, free_y) = get_free(nmx)
		if free_x != None:
			ans += rec(nmx)
		return ans % mod
	print(rec(tuple(mx)))

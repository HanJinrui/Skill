def memoize(func):
	pool = {}

	def naveen(*arg):
		if arg not in pool:
			pool[arg] = func(*arg)
		return pool[arg]
	return naveen
mod = 1000000007
shapes = (((1, 0), (2, 0), (2, 1)), ((0, 1), (0, 2), (-1, 2)), ((0, 1), (1, 1), (2, 1)), ((1, 0), (0, 1), (0, 2)), ((0, 1), (-1, 1), (-2, 1)), ((0, 1), (0, 2), (1, 2)), ((1, 0), (2, 0), (0, 1)), ((1, 0), (1, 1), (1, 2)))
for case in range(int(input())):
	(M, N) = map(int, input().split())
	mx = [int(''.join(('0' if c == '.' else '1' for c in input().rstrip())), 2) for i in range(M)]
	mx = mx + 3 * [0]
	full = (1 << N) - 1

	@memoize
	def rec(n, first, second, third):
		if n == M:
			return 1 if first == second and second == third and (third == 0) else 0
		if first == full:
			return rec(n + 1, second, third, mx[n + 3])

		def can_fit(rows, shape, m_offset):
			res = rows[:]
			for (m, n) in shape:
				m += m_offset
				if m < 0 or m >= N or n < 0 or (n >= M):
					return None
				if res[n] & 1 << m != 0:
					return None
				res[n] |= 1 << m
			return res
		free = 0
		while first & 1 << free != 0:
			free += 1
		rows = [first | 1 << free, second, third]
		ans = 0
		for shape in shapes:
			nrows = can_fit(rows, shape, free)
			if nrows != None:
				ans = (ans + rec(n, *nrows)) % mod
		return ans
	print(rec(0, mx[0], mx[1], mx[2]))

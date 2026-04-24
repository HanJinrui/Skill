for n in [*map(int, open(0))][1:]:
	b = n >> 1
	print(*[b * 3, -1, b][bool(n & 1 or n & b)::2])

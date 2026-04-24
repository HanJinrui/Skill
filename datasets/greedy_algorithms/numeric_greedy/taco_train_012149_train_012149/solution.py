for m in map(int, [*open(0)][1:]):
	print(*[(m - i - 1) // 2 + 1 + i % 2 * (m // 2 + m % 2) for i in range(m)])

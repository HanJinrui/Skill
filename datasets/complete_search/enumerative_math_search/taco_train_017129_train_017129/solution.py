for _ in range(int(input())):
	m = 0
	for __ in range(int(input())):
		(a, b, c) = map(int, input().split())
		m = max(m, b // (a + 1) * c)
	print(m)

for _ in range(int(input())):
	(n, a, b, x, c) = (int(input()), list(map(int, input().split(' '))), list(map(int, input().split(' '))), 0, [])
	for i in a:
		x ^= i
	for i in b:
		x ^= i
	for i in a:
		c.append(i ^ x)
	print(*c) if sorted(c) == sorted(b) else print(-1)

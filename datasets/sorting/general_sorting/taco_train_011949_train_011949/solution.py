t = int(input())
for _ in range(t):
	(n, m, a, b) = [int(e) for e in input().split()]
	if a > b:
		(a, b) = (n - a + 1, n - b + 1)
	s = sorted([int(e) for e in input().split()])[:b - a - 1]
	c = 0
	j = 0
	for i in range(len(s) - 1, -1, -1):
		if s[i] + j + 1 < b:
			c = c + 1
			j = j + 1
	print(c)

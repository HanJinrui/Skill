t = int(input())
for _ in range(t):
	n = int(input())
	ar = [int(x) for x in input().split()]
	s = 0
	m = 0
	for x in ar[::-1]:
		s += max(0, m - x)
		m = max(m, x)
	print(s)

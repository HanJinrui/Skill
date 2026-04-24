t = int(input())
for _ in range(t):
	n = int(input())
	h = sorted((int(x) for x in input().split()))
	s = m = sum(h)
	for (i, hp) in enumerate(h, 2):
		s -= hp
		m = max(m, s * i)
	print(m)

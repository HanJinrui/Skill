from bisect import bisect_left
I = input
t = int(I())
for _ in range(t):
	(a, b, s) = ([], [], [])
	d = {}
	for (i, x) in enumerate(I(), 1):
		if x == '(':
			a.append(i)
			b.append(-1)
			s.append(i)
		elif s:
			b[bisect_left(a, s.pop())] = i
	b.append(-1)
	I()
	for t in map(int, I().split()):
		print(b[bisect_left(a, t)])

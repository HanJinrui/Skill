def f(ar):
	res = []
	s = 0
	for i in range(3):
		s += ar[~i]
		res.append(s)
	for i in range(3, len(ar)):
		s += ar[~i]
		m = min(res)
		res[i % 3] = s - m
	return res[(len(ar) - 1) % 3]
for t in [1] * int(input()):
	input()
	ar = tuple(map(int, input().split()))
	print(f(ar))

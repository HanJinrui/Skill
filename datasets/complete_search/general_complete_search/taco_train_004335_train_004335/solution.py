from itertools import permutations
R = lambda : map(int, input().split())
t = int(input())
for _ in range(t):
	(n, k) = R()
	a = list(R())
	l = [i for (i, x) in enumerate(a) if not x]
	s = 0
	for c in permutations(set(range(1, n + 1)) - set(a)):
		for (i, x) in zip(l, c):
			a[i] = x
		s += sum((a[i] > a[i - 1] for i in range(1, n))) == k
	print(s)

from bisect import bisect_left
(n, k) = map(int, input().split())
q = 'abcdefghijklmnopqrstuvwxyz'
a = {i: [] for i in q}
for (key, value) in enumerate(input()):
	a[value].append(key)

def g(t):
	return [(t[i] + t[i - 1]) // 2 for i in range(1, len(t))]
c = {i: g(a[i]) for i in q}
for _ in range(n):
	(s, t) = (0, input())
	lt = len(t)
	for (key, value) in enumerate(t):
		if a[value]:
			if c[value]:
				s += abs(key - a[value][bisect_left(c[value], key)])
			else:
				s += abs(key - a[value][0])
		else:
			s += lt
	print(s)

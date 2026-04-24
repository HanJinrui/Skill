R = lambda : map(int, input().split())
(n, m) = R()

def f():
	a = [()] * (n + m)
	for i in range(n):
		for x in R():
			a[i] += (x,)
			i += 1
	return [*map(sorted, a)]
print('YNEOS'[f() != f()::2])

(q, f) = (lambda : list(map(int, input().split())), lambda x: sorted(zip(x, x[::-1])))
for _ in range(q()[0]):
	(q(), print('yneos'[f(q()) != f(q())::2]))

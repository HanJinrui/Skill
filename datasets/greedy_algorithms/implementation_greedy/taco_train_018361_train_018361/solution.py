X = [0, -1, 0, 1, 0]
Y = [0, 1, 1, 1, 2]
(n, *a) = [*open(0)]
n = int(n)
a = [list(x) for x in a]
for r in range(n - 2):
	for c in range(1, n - 1):
		if all((a[r + y][c + x] == '.' for (y, x) in zip(Y, X))):
			for (y, x) in zip(Y, X):
				a[r + y][c + x] = '#'
print('YNEOS'[any(('.' in x for x in a))::2])

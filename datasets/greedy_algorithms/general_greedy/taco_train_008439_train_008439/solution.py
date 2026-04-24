from itertools import accumulate
(n, k, q) = map(int, input().split(' '))
T = [[0] for i in range(k)]
for _ in range(n):
	(s, t) = map(int, input().split(' '))
	T[t - 1].append(s)
T = list(map(lambda x: list(accumulate(sorted(x))), T))
for _ in range(q):
	(c, x, y) = map(int, input().split(' '))
	if c == 1:
		T[y - 1].append(T[y - 1][-1] + x)
	else:
		X = T[x - 1]
		Y = T[y - 1]
		Xl = len(X)
		Yl = len(Y)
		while 1:
			if X[Xl - 1] >= Y[Yl - 1]:
				print(x)
				break
			Yl -= X[Xl - 1] - X[Xl - 2]
			if Yl <= 1:
				print(x)
				break
			if Y[Yl - 1] >= X[Xl - 1]:
				print(y)
				break
			Xl -= Y[Yl - 1] - Y[Yl - 2]
			if Xl <= 1:
				print(y)
				break

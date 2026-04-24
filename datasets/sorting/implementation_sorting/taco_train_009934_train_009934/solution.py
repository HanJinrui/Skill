import numpy as np
import copy
for _ in range(int(input())):
	(N, M) = map(int, input().split())
	R = np.array(list(map(int, input().split())))
	C = np.array([list(map(int, input().split())) for i in range(N)])
	C[:, 0] += R
	C = C.cumsum(axis=1)
	Y = C.argmax(axis=1)
	X = np.empty((N, M), dtype=int)
	for i in range(M):
		m = C[:, i].copy()
		m.sort()
		X[:, i] = np.searchsorted(m, C[:, i], side='right')
	X = X.argmax(axis=1)
	print(N - (X == Y).sum())

from itertools import combinations_with_replacement as cwr
for _ in range(int(input())):
	(N, K) = map(int, input().split())
	L = sorted(map(int, input().split()))
	(R, D) = ([L[0] // K], {})
	for i in L[1:]:
		if D.setdefault(i, 0) > 0:
			D[i] -= 1
		else:
			D[i] -= 1
			V = i - R[0] * (K - 1)
			for j in range(K):
				for C in map(lambda x: (K - j) * V + sum(x), cwr(R, j)):
					D[C] = D.get(C, 0) + 1
			R.append(V)
	print(*R)

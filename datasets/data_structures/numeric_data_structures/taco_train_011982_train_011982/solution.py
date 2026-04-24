from collections import Counter

def getMaxandMinProduct(A, Q, N, M):
	(s, m) = (Counter(A), max(A))
	ans = [0] * len(Q)
	for (i, e) in enumerate(Q):
		if e != 0:
			for k in range(e, m + 1, e):
				ans[i] += s.get(k, 0)
	return ans

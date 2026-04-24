class Solution:

	def lexicographicallySmallest(ob, S, K):
		N = len(S)
		K = K * 2 if N & N - 1 else K // 2
		if K >= N:
			return -1
		(st, rem) = ('', 0)
		for c in S:
			while st and rem < K and (st[-1] > c):
				st = st[:-1]
				rem += 1
			st += c
		return st[:N - K]

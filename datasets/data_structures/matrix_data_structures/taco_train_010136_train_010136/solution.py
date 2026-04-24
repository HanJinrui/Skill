class Solution:

	def findK(self, a, n, m, k):
		sp = []
		j = 0
		while len(sp) < k:
			for i in range(j, m - j):
				sp.append(a[j][i])
			for i in range(1 + j, n - j - 1):
				sp.append(a[i][-j - 1])
			for i in range(j, m - j):
				sp.append(a[-j - 1][-i - 1])
			for i in range(1 + j, n - j - 1):
				sp.append(a[-i - 1][j])
			j += 1
		return sp[k - 1]

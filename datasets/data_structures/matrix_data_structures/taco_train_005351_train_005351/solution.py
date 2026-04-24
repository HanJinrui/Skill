class Solution:

	def Maximum_Sum(self, mat, N, K):
		if K > N:
			return 0
		tl = []
		max_sum = 0
		i = 0
		while i < N:
			j = 0
			while j < N - K + 1:
				x = i
				t = sum(mat[i][j:j + K])
				tl.append(t)
				j += 1
			i += 1
		f = []
		for l in range(0, (N - K + 1) * (N - K + 1)):
			f.append(sum(tl[l:l + (N - K + 1) * K:N - K + 1]))
		return max(f)

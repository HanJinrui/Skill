class Solution:

	def maxDiffIndex(self, A, N):
		d = {}
		mx = 0
		for i in range(N):
			if A[i] in d:
				mx = max(abs(d[A[i]] - i), mx)
			else:
				d[A[i]] = i
		return mx

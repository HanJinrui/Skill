class Solution:

	def isBrightened(self, n, k, A):
		prev = 0
		for i in range(n):
			if A[i] == 1:
				if i - k > prev:
					return 0
				prev = i + k + 1
		return 1 if prev >= n else 0

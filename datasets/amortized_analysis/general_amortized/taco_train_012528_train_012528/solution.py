class Solution:

	def maxCandy(self, A, N):
		ans = 0
		(i, j) = (0, N - 1)
		while j - i > 1:
			ans = max(ans, (j - i - 1) * min(A[i], A[j]))
			if A[i] <= A[j]:
				i += 1
			else:
				j -= 1
		return ans

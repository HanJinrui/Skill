class Solution:

	def balancedNumber(self, N):
		l = [int(i) for i in str(N)]
		m = len(l) // 2
		if sum(l[:m]) == sum(l[m + 1:]):
			return 1
		return 0

class Solution:

	def find_min(self, a, n, k):
		if k > sum((x // 2 for x in a)):
			return -1
		m = sum(((x - 1) // 2 for x in a))
		return n + k * 2 - 1 if m >= k else n + m + k

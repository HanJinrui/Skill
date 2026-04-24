class Solution:

	def maxNumbers(self, n, k, a):
		sm = 0
		cnt = 0
		i = 0
		while sm < k:
			i += 1
			if i not in a:
				cnt += 1
				sm += i
		return cnt - 1

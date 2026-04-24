class Solution:

	def countPairs(self, a, n, k):
		a.sort()
		output = 0
		j = 0
		for i in range(n):
			while a[i] - a[j] >= k:
				j += 1
			output += i - j
		return output

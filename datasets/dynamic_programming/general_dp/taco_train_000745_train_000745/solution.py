class Solution:

	def countWays(self, arr, n, s):
		count = [0 for i in range(s + 1)]
		count[0] = 1
		for j in range(1, s + 1):
			for e in arr:
				if j >= e:
					count[j] += count[j - e]
		return count[s] % (pow(10, 9) + 7)

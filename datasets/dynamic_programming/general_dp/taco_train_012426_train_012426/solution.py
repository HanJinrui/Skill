class Solution:

	def max_sum(self, a, k):
		n = len(a)
		best = a.copy()
		for t in range(1, k):
			temp = [-float('inf')] * n
			for i in range(n):
				for j in range(i):
					if a[j] <= a[i] and best[j] + a[i] > temp[i]:
						temp[i] = best[j] + a[i]
			best = temp
		res = max(best)
		return res if res > 0 else -1

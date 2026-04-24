class Solution:

	def countSpecialNumbers(self, N, arr):
		m = max(arr)
		res = [0] * (m + 1)
		for a in arr:
			if res[a] <= 1:
				for b in range(a, m + 1, a):
					res[b] += 1
		return sum((res[a] > 1 for a in arr))

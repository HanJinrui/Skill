class Solution:

	def findLongestConseqSubseq(self, arr, N):
		S = set(arr)
		ans = 0
		for x in arr:
			if x - 1 not in S:
				y = x + 1
				while y in S:
					y += 1
				ans = max(ans, y - x)
		return ans

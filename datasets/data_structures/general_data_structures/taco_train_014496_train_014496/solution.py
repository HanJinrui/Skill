class Solution:

	def maxInstance(self, S):
		count = [0] * 26
		for c in S:
			count[ord(c) - ord('a')] += 1
		return min(count[1], count[0], count[11] // 2, count[14] // 2, count[13])

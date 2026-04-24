class Solution:

	def minValue(self, S, K):
		result = 0
		counts = [S.count(i) for i in set(S)]
		for i in range(K):
			if max(counts):
				counts[counts.index(max(counts))] -= 1
		for i in counts:
			result += i ** 2
		return result

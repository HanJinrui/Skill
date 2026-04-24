from collections import Counter

class Solution:

	def solveQueries(self, arr, query, k):
		return [sum((1 for y in dict(Counter(arr[x[0] - 1:x[1]])).values() if y >= k)) for x in query]

from collections import Counter

class Solution:

	def isPossible(self, N, arr, K):
		return 1 if K * 2 >= Counter(arr).most_common()[0][1] else 0

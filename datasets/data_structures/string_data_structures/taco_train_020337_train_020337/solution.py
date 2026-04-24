class Solution:

	def firstRepeated(self, arr, n):
		from collections import Counter
		d = Counter(arr)
		for i in range(n):
			if d[arr[i]] > 1:
				return i + 1
		return -1

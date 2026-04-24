from collections import Counter

class Solution:

	def biGraph(self, arr, n, e):
		if n == 2 and e == 1:
			return 1
		arr = Counter(arr)
		for i in arr:
			if arr[i] < 2:
				return 0
		return 1

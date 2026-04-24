class Solution:

	def firstElement(self, A, n, k):
		from collections import Counter
		d = Counter(A)
		for i in A:
			if d[i] == k:
				return i
		return -1

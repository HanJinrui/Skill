class Solution:

	def Kclosest(self, arr, n, x, k):
		d = sorted(((abs(x - i), i) for i in arr))
		return sorted(map(lambda x: x[1], d[:k]))

class Solution:

	def findTwoElement(self, arr, n):
		t = n * (n + 1) // 2
		s1 = sum(set(arr))
		s2 = sum(arr)
		k = s2 - s1
		p = t - s1
		return (k, p)

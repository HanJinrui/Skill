class Solution:

	def nextLargerElement(self, arr, n):
		s = []
		a = [-1] * n
		for i in range(n - 1):
			s.append(i)
			while s and arr[i + 1] > arr[s[-1]]:
				a[s[-1]] = arr[i + 1]
				s.pop()
		return a

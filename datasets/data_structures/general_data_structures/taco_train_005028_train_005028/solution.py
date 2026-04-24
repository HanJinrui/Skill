class Solution:

	def help_classmate(self, arr, n):
		s = []
		x = [-1] * n
		for i in range(n):
			while len(s) > 0 and arr[s[-1]] > arr[i]:
				x[s[-1]] = arr[i]
				s.pop()
			s.append(i)
		return x

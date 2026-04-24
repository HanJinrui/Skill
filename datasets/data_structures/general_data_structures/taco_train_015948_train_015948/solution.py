class Solution:

	def maxWater(self, arr, n):
		left = [0] * n
		right = [0] * n
		l = 0
		r = 0
		for i in range(n):
			l = max(l, arr[i])
			left[i] = l
			j = n - 1 - i
			r = max(r, arr[j])
			right[j] = r
		s = 0
		for i in range(n):
			s += min(left[i], right[i]) - arr[i]
		return s

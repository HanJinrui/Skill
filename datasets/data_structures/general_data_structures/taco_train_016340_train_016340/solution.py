class Solution:

	def max_val(self, arr, n):
		j = n - 1
		s = 0
		i = 0
		while i < j:
			s = max(abs(j - i) * min(arr[j], arr[i]), s)
			if arr[i] < arr[j]:
				i += 1
			else:
				j -= 1
		return s

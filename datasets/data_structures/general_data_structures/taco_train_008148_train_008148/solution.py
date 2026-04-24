class Solution:

	def rearrange(self, arr, n):
		m = arr.copy()
		k = -1
		for i in range(0, len(arr), 2):
			arr[i] = m[k]
			k -= 1
			l = 0
		for i in range(1, len(arr), 2):
			arr[i] = m[l]
			l += 1

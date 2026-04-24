from collections import Counter

class Solution:

	def print_next_greater_freq(self, arr, n):
		c = Counter(arr)
		stack = []
		result = [-1] * n
		for i in range(n):
			while stack and c[arr[i]] > stack[-1][1]:
				result[stack.pop()[0]] = arr[i]
			stack.append((i, c[arr[i]]))
		return result

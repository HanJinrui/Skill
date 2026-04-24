class Solution:

	def valid(self, arr, n):
		zero_count = 0
		stack = []
		for item in arr:
			if item == 0:
				zero_count += 1
			elif stack and stack[-1] == item:
				stack[-1] *= 2
				zero_count += 1
			else:
				stack.append(item)
		return stack + [0] * zero_count

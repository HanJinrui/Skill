class Solution:

	def remove3ConsecutiveDuplicates(self, S):
		stack = []
		for i in S:
			if len(stack) > 1 and stack[-1] == stack[-2] == i:
				stack.pop()
				stack.pop()
			else:
				stack.append(i)
		if len(stack) >= 1:
			return ''.join(stack)
		else:
			return -1

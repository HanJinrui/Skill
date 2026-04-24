class Solution:

	def valid(self, s):
		c = dict(('()', '[]', '{}'))
		stack = []
		for i in s:
			if i in '([{':
				stack.append(i)
			elif len(stack) == 0 or i != c[stack.pop()]:
				return 0
		return len(stack) == 0

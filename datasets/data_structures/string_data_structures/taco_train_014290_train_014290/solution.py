class Solution:

	def maxDepth(self, s):
		mx = 0
		k = 0
		for i in s:
			if i == '(':
				k += 1
			elif i == ')':
				k -= 1
			mx = max(mx, k)
		return mx

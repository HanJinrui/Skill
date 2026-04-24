class Solution:

	def leaders(self, A, N):
		stack = []
		for n in A[::-1]:
			if stack == [] or stack[-1] <= n:
				stack.append(n)
		return stack[::-1]

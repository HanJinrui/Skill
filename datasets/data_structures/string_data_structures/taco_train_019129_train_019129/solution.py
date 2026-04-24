class Solution:

	def countSubstring(self, S):
		n = len(S)
		c = 0
		for i in range(n):
			f = 0
			for j in range(i, n):
				if S[j].islower():
					f -= 1
				else:
					f += 1
				if f == 0:
					c += 1
		return c

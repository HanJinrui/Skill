class Solution:

	def nxtHighUsingAtMostOneSwap(self, n):
		l = list(str(n))
		x = len(l)
		i = x - 1
		while i > 0 and l[i] <= l[i - 1]:
			i -= 1
		if i == 0:
			return -1
		else:
			i -= 1
			j = x - 1
			while i < j and l[i] >= l[j]:
				j -= 1
			while l[j - 1] == l[j]:
				j -= 1
			(l[i], l[j]) = (l[j], l[i])
			return ''.join(l)

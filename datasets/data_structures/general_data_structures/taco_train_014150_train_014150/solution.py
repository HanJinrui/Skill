class Solution:

	def compress(self, s):
		n = len(s)
		pi = [0] * n
		j = 0
		for i in range(1, n):
			while j and s[i] != s[j]:
				j = pi[j - 1]
			if s[i] == s[j]:
				j += 1
			pi[i] = j
		res = []
		i = n - 1
		while i >= 0:
			if i % 2 and pi[i] >= (i + 1) // 2 and ((i + 1) % (2 * (i + 1 - pi[i])) == 0):
				res.append('*')
				i = (i + 1) // 2
			else:
				res.append(s[i])
			i -= 1
		return ''.join(res[::-1])

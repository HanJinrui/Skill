class Solution:

	def CountSpecialPalindrome(self, S):
		m = []
		f = []
		i = 0
		a = 0
		while i < len(S):
			j = i
			while i < len(S) and S[i] == S[j]:
				i += 1
			m.append(S[j])
			f.append(i - j)
		for i in range(len(m)):
			if f[i] > 1:
				x = f[i] - 1
				a += x * (x + 1) // 2
			elif i > 0 and i < len(m) - 1 and (m[i - 1] == m[i + 1]):
				a += min(f[i - 1], f[i + 1])
		return a

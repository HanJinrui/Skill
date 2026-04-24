class Solution:

	def matrixGame(self, S):
		n = len(S)
		k = int(n ** 0.5)
		t = ''
		for i in range(k):
			j = i
			s = {}
			while j < n:
				if S[j] not in s:
					s[S[j]] = 1
				else:
					s[S[j]] += 1
				j += k
			j = i
			c = []
			while j < n:
				if s[S[j]] == 1:
					c.append(S[j])
				j = j + k
			h = 0
			p = len(c) - 1
			while h <= p:
				t += c[h]
				h += 1
				if h > p:
					break
				t += c[p]
				p -= 1
		if len(t) == 0:
			return '0'
		return t

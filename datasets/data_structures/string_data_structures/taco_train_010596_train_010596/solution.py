class Solution:

	def rearrange(self, S, N):
		VOWEL = ['a', 'e', 'i', 'o', 'u']
		v = [c for c in S if c in VOWEL]
		v.sort()
		c = [c for c in S if c not in VOWEL]
		c.sort()
		if abs(len(c) - len(v)) > 1:
			return -1
		if len(c) == len(v) and c[0] < v[0]:
			(c, v) = (v, c)
		elif len(c) > len(v):
			(c, v) = (v, c)
		z = ''
		for i in range(len(v)):
			z = z + v[i]
			if i < len(c):
				z = z + c[i]
		return z

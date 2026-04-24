class Solution:

	def countOfSubstringWithKOnes(self, S, K):
		freq = dict()
		sm = 0
		c = 0
		for i in S:
			if i == '1':
				sm += 1
			if sm == K:
				c = c + 1
			if sm - K in freq:
				c = c + freq[sm - K]
			freq[sm] = freq.get(sm, 0) + 1
		return c

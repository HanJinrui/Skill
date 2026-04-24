class Solution:

	def ExtractNumber(self, S):
		m = -1
		for i in S.split():
			if i.isdigit() and '9' not in i:
				m = max(m, int(i))
		return m

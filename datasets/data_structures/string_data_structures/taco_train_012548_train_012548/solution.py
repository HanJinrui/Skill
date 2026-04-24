class Solution:

	def printSequence(self, s):
		p = ''
		dic = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
		for i in s:
			if i == ' ':
				p += '0'
				continue
			for (j, k) in dic.items():
				if i in k:
					p += (k.index(i) + 1) * str(j)
		return p

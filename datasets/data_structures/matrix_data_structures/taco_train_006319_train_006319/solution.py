import math

class Solution:

	def encryptString(self, S):
		col = math.ceil(math.sqrt(len(S)))
		st = ''
		for i in range(col):
			for j in range(i, len(S), col):
				st += S[j]
			st += ' '
		return st

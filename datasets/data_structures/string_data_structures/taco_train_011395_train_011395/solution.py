class Solution:

	def hashString(self, S):
		sum = 0
		l = S.split(' ')
		X = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		for i in l:
			for j in range(len(i)):
				sum += j + X.index(i[j])
		return len(l) * sum

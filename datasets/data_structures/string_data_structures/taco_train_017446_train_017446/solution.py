class Solution:

	def kthCharacter(self, m, n, k):
		d1 = {'1': '10', '0': '01'}
		res = str(bin(m).replace('0b', ''))
		while n:
			res = ''.join([d1[i] for i in res])
			n -= 1
		return res[k - 1]

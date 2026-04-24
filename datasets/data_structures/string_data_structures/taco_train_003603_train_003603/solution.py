class Solution:

	def firstAlphabet(self, S):
		res = next(zip(*S.split()))
		return ''.join(res)

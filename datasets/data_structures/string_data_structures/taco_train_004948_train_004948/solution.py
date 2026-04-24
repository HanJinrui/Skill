class Solution:

	def magicalString(ob, S):
		return ''.join([chr(122 - (ord(x) - 97)) for x in S])

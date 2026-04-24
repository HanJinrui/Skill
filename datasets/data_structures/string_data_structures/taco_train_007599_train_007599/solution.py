import re

class Solution:

	def reverseEqn(self, s):
		rev = ''
		s = re.split('(\\D)', s)
		return ''.join(s[::-1])

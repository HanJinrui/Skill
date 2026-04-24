class Solution:

	def is_common(self, s, t):
		return 'CHANGE' if set(s).intersection(set(t)) else 'BEHAPPY'

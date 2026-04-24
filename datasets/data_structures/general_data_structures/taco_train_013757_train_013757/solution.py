class Solution:

	def common_String(self, s1, s2):
		r = ''.join(sorted(list(set([s for s in s1 if s in s2]))))
		return r if r != '' else 'nil'

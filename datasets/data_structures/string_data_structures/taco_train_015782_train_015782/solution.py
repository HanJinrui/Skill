class Solution:

	def sequence(self, st):
		s = ''
		for i in range(0, len(st)):
			if len(st[i:3 + i]) < 3:
				s += st[i]
			elif len(set(st[i:3 + i])) != 1:
				s += st[i]
		return s

class Solution:

	def arrangeString(self, s):
		ss = 0
		r = ''
		for i in s:
			if i.isdigit():
				ss += int(i)
			else:
				r += i
		r = ''.join(sorted(r)) + (str(ss) if ss else '')
		return r

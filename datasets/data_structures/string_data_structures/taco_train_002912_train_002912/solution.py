class Solution:

	def sameFreq(self, s):
		d = {}
		l = []
		for i in s:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		for (k, v) in d.items():
			l.append(v)
		l.sort()
		if l[0] == l[-1]:
			return 1
		elif l[-1] - 1 == l[0]:
			return 1
		elif l[0] - 1 == 0 and l[1] == l[-1]:
			return 1

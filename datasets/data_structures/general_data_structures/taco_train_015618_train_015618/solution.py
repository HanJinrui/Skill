class Solution:

	def arrangeOddAndEven(self, arr, n):
		l = []
		l1 = []
		p = []
		for i in arr:
			if i % 2 == 0:
				l.append(i)
			else:
				l1.append(i)
		while l or l1:
			if len(l):
				p.append(l.pop(0))
			if len(l1):
				p.append(l1.pop(0))
		return p

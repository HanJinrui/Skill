class Solution:

	def compute(self, arr, n):
		d = {}
		l = []
		for i in arr:
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		for i in d:
			if d[i] > n // 3:
				l.append(i)
		l.sort()
		return l

class Solution:

	def maxSum(self, w, x, b, n):
		c = {i: j for (i, j) in zip(x, b)}
		t = 0
		m = -10 ** 9
		s = ''
		ts = ''
		for i in w:
			ts += i
			if i in c:
				t += c[i]
			else:
				t += ord(i)
			if m < t:
				s = ts
				m = t
			if t < 0:
				t = 0
				ts = ''
		return s

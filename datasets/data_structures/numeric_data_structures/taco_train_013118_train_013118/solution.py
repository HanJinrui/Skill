class Solution:

	def winner(self, x, m, n, arr):
		ra = ro = 0
		for i in arr:
			if i % m == 0:
				ra += 1
			elif i % n == 0:
				ro += 1
		if ra > ro:
			return 'Ram'
		elif ro > ra:
			return 'Rohan'
		else:
			return 'Both'

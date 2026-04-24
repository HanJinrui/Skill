class Solution:

	def absDifOne(self, X):
		l = []
		for i in range(1, 10):

			def numbers(k):
				if k > X:
					return
				if k > 9:
					l.append(k)
				d = k % 10
				if d != 0:
					numbers(k * 10 + d - 1)
				if d != 9:
					numbers(k * 10 + d + 1)
			numbers(i)
		l.sort()
		return l

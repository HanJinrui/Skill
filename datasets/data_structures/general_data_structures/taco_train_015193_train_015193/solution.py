from collections import defaultdict as dd

class Solution:

	def sameOccurrence(self, arr, n, x, y):
		d = dd(lambda : 0)
		d[0] = 1
		count = 0
		output = 0
		for item in arr:
			count += item == x
			count -= item == y
			output += d[count]
			d[count] += 1
		return output

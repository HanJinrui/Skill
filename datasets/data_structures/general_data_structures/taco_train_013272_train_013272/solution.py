class Solution:

	def calculateSpan(self, a, n):
		out = [0]
		for i in range(len(a)):
			j = i - 1
			c = 1
			while j > -1 and a[j] <= a[i]:
				c += out[j + 1]
				j -= out[j + 1]
			out.append(c)
		return out[1:]

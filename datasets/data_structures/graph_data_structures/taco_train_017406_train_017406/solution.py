class Solution:

	def countOfNodes(self, x, n):
		d = [0, 0]

		def f(i, p=-1, c=0):
			d[c] += 1
			for j in x[i]:
				if p != j:
					f(j, i, 1 - c)
		f(1)
		return max(0, d[0] * (d[0] - 1) // 2) + max(0, d[1] * (d[1] - 1) // 2)

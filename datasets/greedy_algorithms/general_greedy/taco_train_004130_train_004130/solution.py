class Solution:

	def chooseandswap(self, A):
		d = {}
		for i in A:
			d[i] = True
		for i in A:
			for j in [chr(m) for m in range(ord('a'), ord(i))]:
				if j in d and d[j]:
					A = A.replace(i, '*')
					A = A.replace(j, i)
					A = A.replace('*', j)
					return A
			d[i] = False
		return A

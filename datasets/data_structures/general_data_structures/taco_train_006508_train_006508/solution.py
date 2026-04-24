class Solution:

	def Rearrange(self, a, n, answer):
		a.sort()
		arr = []
		for i in range(n):
			arr.append(a[i])
			arr.append(a[-(i + 1)])
		answer[:] = arr[:n]
		return answer

class Solution:

	def gfSeries(self, N: int) -> None:
		a = [0, 1]
		for i in range(1, N - 1):
			a.append(a[i - 1] ** 2 - a[i])
		print(*a, sep=' ')

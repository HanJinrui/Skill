class Solution:

	def maxSumBitonicSubArr(self, a, n):
		a = list(map(int, a))
		maxi = a[0]
		i = 0
		while i < n - 1:
			if a[i] == a[i + 1]:
				i += 1
			summa = a[i]
			while i < n - 1 and a[i] < a[i + 1]:
				i += 1
				summa += a[i]
			while i < n - 1 and a[i] > a[i + 1]:
				i += 1
				summa += a[i]
			maxi = max(maxi, summa)
		return maxi

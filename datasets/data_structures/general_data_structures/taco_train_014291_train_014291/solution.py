class Solution:

	def duplicates(self, arr, n):
		a = [0] * (n + 1)
		b = []
		for i in arr:
			a[i] += 1
			if a[i] == 2:
				b.append(i)
		return [-1] if len(b) == 0 else sorted(b)

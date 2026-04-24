class Solution:

	def fn(self, a, val, n):
		ans = 0
		for k in range(n - 2):
			i = k + 1
			j = n - 1
			while i < j:
				su = a[i] + a[j] + a[k]
				if su > val:
					j -= 1
				else:
					ans += j - i
					i += 1
		return ans

	def countTriplets(self, a, n, l, r):
		a.sort()
		return self.fn(a, r, n) - self.fn(a, l - 1, n)

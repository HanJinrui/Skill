class Solution:

	def returnMaxSum(self, a, b, n):
		s = set()
		l = 0
		sum1 = 0
		ans = 0
		for r in range(n):
			sum1 += b[r]
			while a[r] in s and l <= r:
				sum1 -= b[l]
				s.remove(a[l])
				l += 1
			ans = max(ans, sum1)
			s.add(a[r])
		return ans

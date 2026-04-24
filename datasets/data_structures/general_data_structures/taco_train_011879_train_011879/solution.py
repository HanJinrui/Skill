class Solution:

	def maxSumPath(self, a, b, m, n):
		sum1 = 0
		sum2 = 0
		ans = 0
		i = j = 0
		while i < m and j < n:
			if a[i] < b[j]:
				sum1 += a[i]
				i += 1
			elif a[i] > b[j]:
				sum2 += b[j]
				j += 1
			else:
				ans += a[i] + max(sum1, sum2)
				sum1 = sum2 = 0
				i += 1
				j += 1
		sum1 += sum(a[i:])
		sum2 += sum(b[j:])
		ans += max(sum1, sum2)
		return ans

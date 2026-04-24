class Solution(object):

	def findKthNumber(self, m, n, k):
		l = 1
		h = m * n
		while l <= h:
			mid = l + (h - l) // 2
			cnt = 0
			for i in range(1, m + 1):
				cnt += min(n, mid // i)
			if cnt >= k:
				h = mid - 1
			else:
				l = mid + 1
		return l

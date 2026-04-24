class Solution:

	def solve(self, n, k, stalls):
		l = 0
		r = max(stalls) - min(stalls)
		stalls.sort()
		prev = -99999999999
		while l <= r:
			count = 0
			mid = (l + r) // 2
			for i in range(n):
				if abs(stalls[i] - prev) >= mid:
					count += 1
					prev = stalls[i]
			if count < k:
				r = mid - 1
			else:
				l = mid + 1
		return r

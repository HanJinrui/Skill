import heapq as hq

class Solution:

	def smallestRange(self, A, n, k):
		mnh = []
		mx = float('-inf')
		for (r, a) in enumerate(A):
			mx = max(mx, a[0])
			hq.heappush(mnh, (a[0], r, 0))
		ans = [mnh[0][0], mx]
		while mnh:
			(v, r, c) = hq.heappop(mnh)
			if mx - v < ans[1] - ans[0]:
				ans = [v, mx]
			if c + 1 == n:
				return ans
			mx = max(mx, A[r][c + 1])
			hq.heappush(mnh, (A[r][c + 1], r, c + 1))
		return ans

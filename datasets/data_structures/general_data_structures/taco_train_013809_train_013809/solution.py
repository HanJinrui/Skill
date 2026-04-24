import heapq as h

class Solution:

	def maxAmount(self, N, K, A):
		hp = []
		h.heapify(hp)
		for i in range(N):
			h.heappush(hp, -1 * A[i])
		ans = 0
		for i in range(K):
			x = h.heappop(hp)
			ans += -1 * x
			h.heappush(hp, x + 1)
		return ans % 1000000007

class Solution:

	def minCostClimbingStairs(self, cost, N):
		for i in range(2, N):
			cost[i] += min(cost[i - 1], cost[i - 2])
		return min(cost[-1], cost[-2])

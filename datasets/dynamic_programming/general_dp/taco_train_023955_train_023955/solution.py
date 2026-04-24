class Solution:

	def minCost(self, costs):
		N = len(costs)
		K = len(costs[0])
		if K == 1:
			if N == 1:
				return costs[0][0]
			else:
				return -1
		(m1, m2) = sorted(costs[0])[0:2]
		for i in range(1, N):
			for j in range(K):
				if m1 == costs[i - 1][j]:
					costs[i][j] += m2
				else:
					costs[i][j] += m1
			(m1, m2) = sorted(costs[i])[0:2]
		return min(costs[-1])

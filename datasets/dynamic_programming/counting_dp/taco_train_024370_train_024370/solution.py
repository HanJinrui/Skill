MAX = 101
dp = [[[[-1] * 4 for i in range(MAX)] for j in range(MAX)] for k in range(MAX)]

def countWayss(p, q, r, last):
	if p < 0 or q < 0 or r < 0:
		return 0
	if p == 1 and q == 0 and (r == 0) and (last == 0):
		return 1
	if p == 0 and q == 1 and (r == 0) and (last == 1):
		return 1
	if p == 0 and q == 0 and (r == 1) and (last == 2):
		return 1
	if dp[p][q][r][last] != -1:
		return dp[p][q][r][last]
	if last == 0:
		dp[p][q][r][last] = countWayss(p - 1, q, r, 1) + countWayss(p - 1, q, r, 2)
	elif last == 1:
		dp[p][q][r][last] = countWayss(p, q - 1, r, 0) + countWayss(p, q - 1, r, 2)
	else:
		dp[p][q][r][last] = countWayss(p, q, r - 1, 0) + countWayss(p, q, r - 1, 1)
	return dp[p][q][r][last]

def countUtil(p, q, r):
	return countWayss(p, q, r, 0) + countWayss(p, q, r, 1) + countWayss(p, q, r, 2)

class Solution:

	def CountWays(self, p, q, r):
		return countUtil(p, q, r) % int(1000000000.0 + 7)

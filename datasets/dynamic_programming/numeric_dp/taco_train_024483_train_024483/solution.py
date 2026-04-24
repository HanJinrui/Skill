from math import gcd
from sys import stdin
input = stdin.readline

def solve(N, A):
	k = 10
	dp = [None] * N
	dp[0] = {j: 2 ** abs(j) for j in range(-k, k + 1)}
	for i in range(1, N):
		dp[i] = {j: float('inf') for j in range(-k, k + 1)}
		for j1 in range(-k, k + 1):
			cost = 2 ** abs(j1)
			for j2 in range(-k, k + 1):
				if gcd(A[i - 1] + j2, A[i] + j1) == 1:
					dp[i][j1] = min(dp[i][j1], dp[i - 1][j2] + cost)
	return min((dp[N - 1][j] for j in range(-k, k + 1)))
T = int(input().strip())
for problem in range(1, T + 1):
	N = int(input().strip())
	A = [int(x) for x in input().strip().split()]
	print(solve(N, A))

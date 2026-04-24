import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
C = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
Q = int(input())
x = int(input())
P = 10 ** 9 + 7
dp = [[0] * 20100 for _ in range(N + 1)]
dp[0][0] = 1
ans = 0
s = x
t = s
for i in range(N):
	for j in range(20050, t - 1, -1):
		if j < 0:
			break
		dp[i + 1][j] = (dp[i + 1][j + 1] + dp[i][max(j - C[i], 0)] - dp[i][j + 1]) % P
	for j in range(min(t - 1, 20050), -1, -1):
		dp[i + 1][j] = dp[i + 1][j + 1]
	if i < N - 1:
		s += B[i]
		t += s
print(dp[-1][0] % P)

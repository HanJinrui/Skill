import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(2 * 10 ** 5 + 10)
write = lambda x: sys.stdout.write(x + '\n')
debug = lambda x: sys.stderr.write(x + '\n')
writef = lambda x: print('{:.12f}'.format(x))
n = int(input())
a = list(map(int, input().split()))
m = sum(a)
M = 10 ** 9 + 7
dp = [0] * (2 * m + 1)
ans = 0
dp[m] = 1
val = 0
for i in range(n):
	v = a[i]
	ndp = [0] * (2 * m + 1)
	for j in range(2 * m + 1):
		if j - v >= 0:
			ndp[j - v] += dp[j]
			if ndp[j - v] > M:
				ndp[j - v] -= M
		if j + v <= 2 * m:
			ndp[j + v] += dp[j]
			if ndp[j + v] > M:
				ndp[j + v] -= M
	dp = ndp
	ans += dp[m]
	ans %= M
	dp[m] += 1
	val += v
print(ans % M)

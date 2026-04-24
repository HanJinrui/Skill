read = lambda : map(int, input().split())
(n, k) = read()
c = list(read())
dp = [0] * (k + 1)
dp[0] = 1
for x in c:
	ndp = dp[:]
	for i in range(k, x - 1, -1):
		ndp[i] |= dp[i - x] | dp[i - x] << x
	dp = ndp
b = bin(dp[-1])
ans = [i for i in range(k + 1) if b[-i - 1] == '1']
print(len(ans))
print(*ans)

n = int(input())
(*a,) = map(int, input().split())
a.sort()
ans = sum((a[2 * n - i - 1] - a[i] for i in range(n)))
m = 998244353
for i in range(n):
	ans *= 2 * n - i
	ans *= pow(i + 1, m - 2, m)
	ans %= m
print(ans)

import math

def snek(a, n, k):
	ans = [-math.inf] * (n - k)
	c = 0
	for x in range(n - k):
		c += a[x]
		if c < a[x]:
			c = a[x]
		ans[x] = max(c, ans[x - 1])
	return ans
t = int(input())
for i in range(t):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	k += 1
	l = snek(a, n, k)
	r = snek(a[::-1], n, k)[::-1]
	ans = -math.inf
	for j in range(n - k):
		m = l[j] + r[j]
		if m > ans:
			ans = m
	print(ans)

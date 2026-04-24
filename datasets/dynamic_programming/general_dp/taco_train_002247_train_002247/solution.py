mod = 1000000007

def mul(a, n, mod):
	ans = 1
	while n > 0:
		ans = ans * a % mod
		n -= 1
	return ans
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	aa = list()
	for i in range(n):
		aa.append([a[i], i])
	aa.append([n + 1, -1])
	aa.sort()
	ans = 1
	l = 0
	r = 1
	while r <= n:
		while aa[r - 1][1] < aa[r][1]:
			r += 1
		ans = ((ans + mul(2, r - l, mod)) % mod - 1 + mod) % mod
		l = r
		r += 1
	print(ans)

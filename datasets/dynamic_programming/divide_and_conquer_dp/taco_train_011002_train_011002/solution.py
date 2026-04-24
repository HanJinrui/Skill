import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
a = [0] + list(map(int, input().split()))
buc = [0] * (n + 1)
dp_p = [n * (n - 1) // 2] * (n + 1)
dp_c = [0] * (n + 1)
dp_p[0] = 0
buc[a[1]] = 1
L = R = 1
ans = 0

def cal(l, r):
	global L, R, ans
	while L < l:
		ans += 1 - buc[a[L]]
		buc[a[L]] -= 1
		L += 1
	while L > l:
		L -= 1
		ans += buc[a[L]]
		buc[a[L]] += 1
	while R < r:
		R += 1
		ans += buc[a[R]]
		buc[a[R]] += 1
	while R > r:
		ans += 1 - buc[a[R]]
		buc[a[R]] -= 1
		R -= 1

def solve(lb, rb, l, r):
	global ans, L
	if lb > rb or l > r:
		return
	mid = (l + r) // 2
	d = 0
	res = 9223372036854775807
	cal(lb, mid)
	for i in range(lb, rb + 1):
		ans += 1 - buc[a[L]]
		buc[a[L]] -= 1
		L += 1
		if res > dp_p[i] + ans:
			res = dp_p[i] + ans
			d = i
	dp_c[mid] = res
	solve(lb, d, l, mid - 1)
	solve(d, rb, mid + 1, r)
for cur in range(1, m + 1):
	solve(0, n - 1, 1, n)
	(dp_p, dp_c) = (dp_c, dp_p)
print(dp_p[n])

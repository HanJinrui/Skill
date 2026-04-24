from bisect import bisect_left

def lis(a):
	l = [0] * len(a)
	mx = 0
	ans = []
	for i in range(len(a)):
		x = bisect_left(ans, a[i])
		if x >= len(ans):
			ans.append(a[i])
		else:
			ans[x] = a[i]
		mx = max(mx, x)
		l[i] = mx
	return l
t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	lis1 = lis(a)
	lis2 = list(map(lambda x: -x, a))[::-1]
	lis2 = lis(lis2)[::-1]
	ans = 1
	for i in range(n - 1):
		ans = max(ans, lis1[i] + lis2[i + 1] + 2)
	print(ans)

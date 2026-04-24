t = int(input())
while t > 0:
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	c = a[0]
	for i in range(1, n):
		ans = ans | c & a[i]
		c |= a[i]
	print(ans)
	t -= 1

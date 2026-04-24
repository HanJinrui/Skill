from bisect import bisect
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))[::-1]
	b = list(map(int, input().split()))[::-1]
	c = []
	for i in range(n):
		x = bisect(a, b[i])
		if x > 0:
			c.append(x - i-1)
	if len(c):
		print(max(c))
	else:
		print(0)

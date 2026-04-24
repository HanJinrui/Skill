t = int(input())
for j in range(t):
	a = []
	b = []
	c = []
	d = []
	n = int(input())
	for k in range(n):
		(x, y) = map(int, input().split())
		a.append(x + y)
		b.append(-x + y)
	a.sort()
	b.sort()
	for i in range(n - 1):
		c.append((a[i + 1] - a[i]) / 2)
		d.append((b[i + 1] - b[i]) / 2)
	print(min(min(c), min(d)))

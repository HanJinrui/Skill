(n, m) = map(int, input().split())
d = []
for i in range(n):
	(a, b) = map(int, input().split())
	while a < m:
		a += b
	d.append(a)
print(d.index(min(d)) + 1)

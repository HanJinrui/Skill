(n, x, y) = map(int, input().split(' '))
l = [0.0] * (n + 1)
for i in range(1, n + 1):
	l[i] = min(l[i - 1] + x, l[(i + 1) // 2] + y + x * (i & 1))
print(int(l[n]))

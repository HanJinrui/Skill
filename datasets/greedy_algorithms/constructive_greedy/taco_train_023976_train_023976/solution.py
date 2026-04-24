(n, x) = map(int, input().split())
a = list(map(int, input().split()))
m = min(a)
a = [i - m for i in a]
x = x - 1
d = m * n
while a[x] > 0:
	d += 1
	a[x] -= 1
	x -= 1
	if x < 0:
		x = n - 1
a[x] = d
print(*a)

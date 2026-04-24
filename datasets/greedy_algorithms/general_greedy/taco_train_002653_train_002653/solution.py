n = int(input())
a = [*map(int, input().split())]
s = 0
for i in range(n - 1):
	p = 1
	while i + (p << 1) < n:
		p <<= 1
	a[i + p] += a[i]
	print(s + a[i])
	s += a[i]

(n, m) = map(int, input().split())
a = [0 for i in range(0, n + 1)]
b = [0 for i in range(0, n + 1)]
for i in range(0, m):
	(x, y) = map(int, input().split())
	a[x] = b[y] = 1
s = 0
for i in range(2, n):
	if a[i] == 0:
		s += 1
	if b[i] == 0:
		s += 1
if n % 2 and a[n // 2 + 1] == 0 and (b[n // 2 + 1] == 0):
	s -= 1
print(s)

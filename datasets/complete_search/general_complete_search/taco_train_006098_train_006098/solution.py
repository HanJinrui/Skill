(n, m) = map(int, input().split())
c = 0
for i in range(n + 1):
	c += int(i ** 2 + (n - i) ** 0.5 == m)
print(c)

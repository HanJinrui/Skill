(a, b, n) = map(int, input().split())
for i in range(2, n):
	(a, b) = (b, b ** 2 + a)
print(b)

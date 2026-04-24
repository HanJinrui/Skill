n = int(input())
p = list(map(int, input().split()))
a = [0] * n
b = [0] * n
for i in range(n - 1):
	if p[i] < p[i + 1]:
		a[i + 1] = a[i] + 1
for i in range(n - 1, 0, -1):
	if p[i - 1] > p[i]:
		b[i - 1] = b[i] + 1
x = max(max(a), max(b))
k = sum((x == i or x == j for (i, j) in zip(a, b)))
s = sum((x == i and x == j for (i, j) in zip(a, b)))
if k > 1 or s == 0 or x % 2:
	print(0)
else:
	print(1)

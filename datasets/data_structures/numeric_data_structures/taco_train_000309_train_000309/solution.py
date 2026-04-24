(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = 0
z = n - k + 1
for i in range(n):
	s += a[i] * min(z, k, i + 1, n - i)
print(s / z)

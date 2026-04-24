def mi():
	return map(int, input().split())
(n, v) = mi()
a = list(mi())
b = list(mi())
x = 100000
for i in range(n):
	x = min(x, b[i] / a[i])
print(min(sum(a) * x, v))

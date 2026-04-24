b = 10 ** 5

def f(t, x, k):
	if t == 1:
		return (x + k * b + b - 1) // b
	else:
		return (x * k + b - 1) // b
(n, m) = map(int, input().split())
res = [-1] * (m + 1)
res[0] = 0
for i in range(1, n + 1):
	(t, x, y) = map(int, input().split())
	for k in range(m + 1):
		if res[k] in (-1, i):
			continue
		for _ in range(y):
			k = f(t, x, k)
			if k > m or res[k] > -1:
				break
			res[k] = i
res.pop(0)
print(*res)

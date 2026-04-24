I = input
t = int(I())
for _ in range(t):
	(n, k) = map(int, I().split())
	a = [*map(int, I())] + [0] * k
	a = [a[i] and (not (a[i - k] or a[i + k])) for i in range(n)]
	k *= 2
	for i in range(k, n):
		a[i] &= ~a[i - k]
	print(sum(a))

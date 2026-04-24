def func(n, k, toggle):
	if k == 2 ** n - 1:
		return n * 2 ** (n - 1) - (toggle ^ 1) * k * 1
	if n == 1:
		return toggle
	if k <= 2 ** n // 2:
		return toggle * k * 1 + func(n - 1, k - 1, 0)
	else:
		return toggle * k * 1 + func(n - 1, 2 ** (n - 1) - 1, 0) + func(n - 1, k - 2 ** n // 2, 1)
for case in range(int(input())):
	(N, K) = map(int, input().split())
	print(func(N, K, 1))

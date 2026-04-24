(n, ans) = (int(input()), 1000000)
for i in range(1, n + 1):
	(k, a, b) = (0, n, i)
	while b > 1:
		k += a // b
		(a, b) = (b, a % b)
	if b != 0:
		ans = min(ans, a - 1 + k)
print(ans)

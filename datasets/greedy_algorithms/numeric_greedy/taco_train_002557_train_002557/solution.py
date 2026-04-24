for _ in range(int(input())):
	n = int(input())
	a = [1 for i in range(0, 30)]
	i = 2
	while i * i <= n:
		j = 0
		while n % i == 0:
			a[j] *= i
			n //= i
			j += 1
		if i == 2:
			i += 1
		else:
			i += 2
	a[0] *= n
	ans = 0
	for i in range(0, 30):
		if a[i] > 1:
			ans += a[i]
	print(ans)

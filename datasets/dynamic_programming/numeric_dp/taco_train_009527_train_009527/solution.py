t = int(input())
for each_t in range(t):
	(n, m, q) = input().split()
	(n, m, q) = (int(n), int(m), int(q))
	a = [0] * (n + 1)
	if n % 2 == 0:
		mid = n // 2
		a[mid] = mid + 1
		b = mid
		c = mid + 2
	else:
		mid = n // 2 + 1
		a[mid] = 1
		b = mid
		c = mid + 1
	x = mid - 1
	while x >= 1:
		a[x] = a[x + 1] % m * b % m * c % m % m
		b -= 1
		c += 1
		x -= 1
	a[0] = 1
	for i in range(1, mid + 1):
		a[i] = a[i - 1] * a[i] % m
	for each_q in range(q):
		r = int(input())
		r = min(r, n - r)
		print(a[r] % m)

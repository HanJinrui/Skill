def c(x, y):
	ans = 1
	for i in range(x, x + y):
		ans *= i
	for i in range(1, y + 1):
		ans //= i
	return ans
t = int(input())
mod = 10 ** 9 + 7
for q in range(t):
	a = list(map(int, input().split()))
	s = int(input())
	d = [0 for i in range(s + 1)]
	d[0] = 1
	for i in range(1, s + 1):
		for j in range(s, -1, -1):
			k = 1
			while k * i + j <= s:
				d[k * i + j] = (d[k * i + j] + d[j] * c(a[0] + i * a[1] + i ** 2 * a[2] + i ** 3 * a[3], k)) % mod
				k += 1
	print(d[s])

p = 1000000007
fac = [0] * 150001
fac[0] = 1
for i in range(1, 150001):
	fac[i] = fac[i - 1] * i % p
t = int(input())
for _ in range(t):
	ans = 0
	n = int(input())
	a = input()
	b = input()
	c1 = a.count('1')
	c2 = b.count('1')
	if n < c1 + c2:
		Max = 2 * n - c1 - c2
	else:
		Max = c1 + c2
	Min = abs(c1 - c2)
	for j in range(Min, Max + 1, 2):
		ans += fac[n] * pow(fac[j], p - 2, p) * pow(fac[n - j], p - 2, p) % p
		ans = ans % p
	print(ans)

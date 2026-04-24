def main():
	n = int(input())
	mod = 998244353
	if n == 1:
		return 1
	if n == 2:
		return 4
	if n == 3:
		return 10
	a = 10 * pow(2, n - 2, mod) + 2
	b = 2 * pow(2, (n + 1) // 2, mod)
	c = 2 * pow(2, n // 2, mod)
	return (a - b - c) % mod
for _ in range(int(input())):
	print(main())

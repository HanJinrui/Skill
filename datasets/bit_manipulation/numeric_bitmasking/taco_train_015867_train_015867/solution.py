mod = int(1000000000.0 + 7)
for _ in range(int(input())):
	n = int(input())
	print(n if n < 3 else pow(2, len(bin(n)) - 2, mod) if n & n - 1 else (2 * n - 1) % mod)

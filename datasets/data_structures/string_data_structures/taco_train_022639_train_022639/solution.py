M = 10 ** 9 + 7
for _ in range(int(input())):
	n = int(input())
	ans = 52 * (pow(26, n // 2, M) - 1) * pow(25, M - 2, M)
	if n % 2 == 1:
		ans += pow(26, n // 2 + 1, M)
	print(ans % M)

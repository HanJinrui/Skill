for _ in range(int(input())):
	(n, m) = map(int, input().split())
	sums = 0
	for i in range(31):
		sums += pow((m // (1 << i + 1) << i) + max(0, m % (1 << i + 1) - (1 << i) + 1), n, 998244353) << i
	print(sums % 998244353)

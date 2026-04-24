for _ in range(int(input())):
	n = int(input())
	a = [int(i) for i in input().split()]
	k = sum(a)
	st = sum(a[-k:])
	ans = sum((n * (n - 1) // 2 * pow(k - i, -2, 998244353) for i in range(st, k))) % 998244353
	print(ans)

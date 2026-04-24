for _ in range(int(input())):
	n = int(input())
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]
	k1 = max(max(a), max(b))
	k2 = [min(a[k], b[k]) for k in range(n)]
	print(k1 * max(k2))

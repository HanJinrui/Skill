for i in range(int(input())):
	(n, m) = map(int, input().split())
	a = [int(j) for j in input().split()]
	a.sort(reverse=True)
	print(max(sum(a[:m * 2:2]), sum(a[1:m * 2:2]) + a[m * 2]))

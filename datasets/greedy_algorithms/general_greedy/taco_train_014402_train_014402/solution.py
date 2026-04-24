for t in range(int(input())):
	a = list(map(int, input().split()))
	k = int(input())
	i = 10
	while sum(a[i - 1:10]) <= k:
		i -= 1
	print(i)

for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = [*map(int, input().split())]
	print(sum((a[i] > k for i in range(k))))

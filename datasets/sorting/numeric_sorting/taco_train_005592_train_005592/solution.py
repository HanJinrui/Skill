for i in range(int(input())):
	(n, k) = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort()
	print(sum(l[k:n - k]) * 1.0 / (n - 2 * k))

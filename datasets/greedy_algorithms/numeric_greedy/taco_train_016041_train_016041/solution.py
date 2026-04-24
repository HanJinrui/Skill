for _ in range(int(input())):
	(n, k) = map(int, input().split())
	l = set(map(int, input().split()))
	if len(l) == 1:
		print(1)
	elif k == 1:
		print(-1)
	else:
		print((len(l) - 2 + (k - 1)) // (k - 1))

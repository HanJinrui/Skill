for i in range(int(input())):
	(N, X) = map(int, input().split())
	l = list(map(int, input().split()))
	a = 0
	for i in range(N):
		if X > l[i]:
			a = i + 1
	print(a)

for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	print(sum([n - k for (k, v) in enumerate(l) if v <= k + 1]))

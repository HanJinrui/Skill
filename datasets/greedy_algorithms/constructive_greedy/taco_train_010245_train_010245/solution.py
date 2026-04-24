for t in range(int(input())):
	(n, k) = map(int, input().split())
	arr = [i for i in range((k + 1) // 2, n + 1) if i != k]
	print(len(arr))
	print(*arr)

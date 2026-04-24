for _ in range(int(input())):
	(n, m) = map(int, input().split())
	arr = [i for i in range(n)]
	if n == 4 and m == 3:
		print(-1)
		continue
	if n == m + 1:
		(arr[0], arr[m - 1]) = (arr[m - 1], arr[0])
		(arr[1], arr[n - 4]) = (arr[n - 4], arr[1])
	else:
		(arr[0], arr[m]) = (arr[m], arr[0])
	for i in range(n // 2):
		print(arr[i], arr[n - 1 - i])

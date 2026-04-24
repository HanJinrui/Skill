for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr2 = arr.copy()
	arr.sort(reverse=True)
	mid = n // 2
	(arr[1::2], arr[0::2]) = (arr[:mid], arr[mid:])
	flag = False
	for i in range(n - 2):
		if arr[i] == arr[i + 1] or arr[i + 1] == arr[i + 2]:
			flag = True
			break
	if flag:
		print(-1)
	else:
		print(*arr)

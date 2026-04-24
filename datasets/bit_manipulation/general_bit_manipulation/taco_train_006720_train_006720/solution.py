for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.insert(0, 0)
	arr.append(0)
	for i in range(1, n + 1):
		print(max(arr[i] & arr[i - 1], arr[i] & arr[i + 1]), end=' ')
	print()

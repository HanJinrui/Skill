for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	fl = True
	for i in range(n - 2):
		if arr[i] > arr[i + 2]:
			fl = False
			break
	if fl:
		print('YES')
	else:
		print('NO')

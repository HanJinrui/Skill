tests = int(input())
for i in range(tests):
	n = int(input())
	arr = [0] * (2 * n)
	for j in range(n):
		temp = list(map(int, input().split()))
		for k in range(n):
			arr[n - j + k] += temp[k]
	print(max(arr))

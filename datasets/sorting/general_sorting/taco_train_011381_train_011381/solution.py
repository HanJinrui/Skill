t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	D = {}
	for j in range(n):
		D[arr[j]] = 1
		if arr[j] - 1 not in D:
			D[arr[j] + 1] = 1
	print(len(D) - n)

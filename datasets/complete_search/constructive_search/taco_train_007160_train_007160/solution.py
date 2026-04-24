for _ in range(int(input())):
	n = int(input())
	arr = [i for i in range(1, n + 1)][::-1]
	for i in range(n):
		print(*[arr[i]] + arr[:i] + arr[i + 1:])

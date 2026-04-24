for _ in range(int(input())):
	n = int(input())
	A = [0] + list(map(int, input().split()))
	for i in range(1, n + 1):
		if i % 2 != A[i] % 2:
			print(-1)
			break
	else:
		ans = []

		def rev(x):
			A[1:x + 1] = A[1:x + 1][::-1]
			ans.append(x)
		for x in range(n, 1, -2):
			i = A.index(x)
			rev(i)
			j = A.index(x - 1)
			rev(j - 1)
			rev(j + 1)
			rev(3)
			rev(x)
		print(len(ans))
		print(*ans)

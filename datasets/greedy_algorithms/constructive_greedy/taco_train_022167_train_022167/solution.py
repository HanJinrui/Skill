for _ in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	if a[-2] > a[-1]:
		print(-1)
	elif a[-1] >= 0:
		print(n - 2)
		for i in range(1, n - 1):
			print(i, n - 1, n)
	else:
		print([-1, 0][a == sorted(a)])

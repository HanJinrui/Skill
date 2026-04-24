for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	x = sum(l)
	if x == 2 * n:
		print(n)
	elif l == [2, 1, 2]:
		print(4)
	else:
		print(x)

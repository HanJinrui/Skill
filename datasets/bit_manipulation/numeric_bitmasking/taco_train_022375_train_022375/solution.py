for t in range(int(input())):
	n = int(input())
	if n == 1:
		print(2)
	elif n + 1 & n:
		print(-1)
	else:
		print(n >> 1)

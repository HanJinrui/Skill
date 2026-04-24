t = int(input())
for _ in range(t):
	n = int(input())
	if n % 2 == 1:
		if n < 5:
			print(-1)
		else:
			ans5 = [4, 5, 2, 1, 3]
			ansRest = list(range(n, 5, -1))
			print(*ans5, *ansRest)
	else:
		print(*list(range(n, 0, -1)))

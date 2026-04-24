tests = int(input())
for i in range(tests):
	(n, k, l) = map(int, input().split())
	if k * l < n or (n > 1 and k == 1):
		print(-1)
	else:
		ans = [i for i in range(1, k + 1)] * l
		print(*ans[:n])

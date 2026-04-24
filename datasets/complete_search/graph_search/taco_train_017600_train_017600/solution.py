t = int(input())
for _ in range(t):
	(n, p) = map(int, input().split())
	for i in range(2 * n + p):
		print(i % n + 1, (i + i // n + 1) % n + 1)

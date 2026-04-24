t = int(input())
for tc in range(t):
	g = int(input())
	for j in range(g):
		(i, n, q) = map(int, input().split())
		print(n // 2 + abs(i - q) * (n % 2))

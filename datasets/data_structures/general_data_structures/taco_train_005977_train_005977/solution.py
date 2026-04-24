t = int(input())
for _ in range(t):
	(a, b) = map(int, input().split())
	if a > 1000:
		a = 9 * a / 10
	print(a * b)

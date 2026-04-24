n = int(input())
ar = sorted(map(int, input().split()))
d = min((abs(ar[i] - ar[i - 1]) for i in range(1, n)))
for i in range(1, n):
	if abs(ar[i] - ar[i - 1]) == d:
		print(ar[i - 1], ar[i], end=' ')
print()

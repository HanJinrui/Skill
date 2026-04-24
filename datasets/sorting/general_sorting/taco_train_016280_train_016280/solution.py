n = int(input())
a = sorted(map(int, input().split()))
for i in range(2, n, 2):
	(a[i - 1], a[i]) = (a[i], a[i - 1])
print(*a)

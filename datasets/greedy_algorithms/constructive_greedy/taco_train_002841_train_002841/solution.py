n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
for i in range(n):
	print(b[(b.index(a[i]) + 1) % n], end=' ')

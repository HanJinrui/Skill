t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a.sort()
	b.sort()
	x1 = b[0] - a[0]
	x2 = b[0] - a[1]
	if x2 <= 0 or (n > 2 and b[1] - a[2] != x2):
		print(x1)
	else:
		print(x2)

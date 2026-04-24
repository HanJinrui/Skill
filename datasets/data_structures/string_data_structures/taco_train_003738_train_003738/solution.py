t = int(input())
for i in range(t):
	n = int(input())
	a = input().split()
	c = 0
	for j in range(n - 1):
		if a[j] == a[j + 1]:
			c += 1
	print(n - c)

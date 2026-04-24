T = int(input())
for i in range(T):
	n = int(input())
	l = list(map(int, input().split()))
	a = l[0]
	c = 0
	for i in l:
		if i <= a:
			c += 1
			a = i
	print(c)

t = int(input())
while t > 0:
	(n, m) = map(int, input().split())
	p = list(map(int, input().split()))
	l = []
	for i in range(n):
		l.append(list(map(int, input().split()))[1:])
	c = 0
	for i in p:
		if l[i] != []:
			x = max(l[i])
			l[i].remove(x)
			c += x
	print(c)
	t -= 1

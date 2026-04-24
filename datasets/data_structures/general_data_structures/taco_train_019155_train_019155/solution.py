t = int(input())
for i in range(t):
	n = int(input())
	ar = list(map(int, input().split()))
	l = set()
	v = [ar[0]]
	for i in range(1, n):
		while v and v[-1] <= ar[i]:
			l.add(ar[i] - v[-1])
			v.pop()
		if v:
			l.add(v[-1] - ar[i])
		v.append(ar[i])
	print(len(l))

for _ in range(int(input())):
	n = int(input())
	f = []
	l = []
	for i in range(n):
		(a, b) = input().split()
		f.append(a)
		l.append(b)
	for i in range(n):
		if f.count(f[i]) > 1:
			print(f[i], l[i])
		else:
			print(f[i])

from statistics import median
for i in range(int(input())):
	N = int(input())
	l = list(map(int, input().split()))
	while len(l) > 2:
		l.remove(median(l[:3]))
	print(*l)

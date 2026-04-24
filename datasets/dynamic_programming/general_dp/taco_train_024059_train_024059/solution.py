from bisect import bisect_left
l = []
for _ in range(int(input())):
	a = int(input())
	i = bisect_left(l, a)
	if i < len(l):
		l[i] = a
	else:
		l.append(a)
print(len(l))

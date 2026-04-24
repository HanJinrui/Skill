input()
a = [min(i, -1 - i) for i in map(int, input().split())]
if len(a) & 1:
	i = a.index(min(a))
	a[i] = -1 - a[i]
print(*a)

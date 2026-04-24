input()
b = map(int, input().split())
l = [0, next(b)]
a = l[:]
i = 1
for x in b:
	d = sum(l) - x
	l[d > 0] -= d
	a[i:i] = l
	i += 1
print(*a)

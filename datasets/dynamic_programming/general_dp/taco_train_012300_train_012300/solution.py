import bisect
n = int(input())
a = [-99] * 100
c = 100
for i in map(lambda x: int(x), input().split()):
	a.append(i - c)
	c += 1
l = a[:1]
for i in a[1:]:
	j = bisect.bisect(l, i)
	if j != len(l):
		l[j] = i
	else:
		l.append(i)
print(100 + n - len(l))

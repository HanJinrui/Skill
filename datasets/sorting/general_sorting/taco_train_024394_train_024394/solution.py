import bisect
t = int(input())
v = [int(i) for i in input().strip().split()]
v2 = []
s = 0
for (i, e) in enumerate(v):
	ind = bisect.bisect(v2, e)
	v2.insert(ind, e)
	s += i - ind
print(s)

input()
a = [0] * 100001
for x in map(int, input().split()):
	a[x] += x
c = d = 0
for i in a:
	(c, d) = (max(c, i + d), c)
print(c)

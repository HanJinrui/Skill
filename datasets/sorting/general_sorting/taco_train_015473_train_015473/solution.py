t = [tuple(map(int, input().split())) for i in range(int(input()))]
t.sort()
(c, s) = (0, 0)
for (a, b) in t:
	if b < c:
		s += 1
	if b > c:
		c = b
print(s)

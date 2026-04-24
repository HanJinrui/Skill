import math
(t, k) = map(int, input().split())
c = []
res = [0 for x in range(10 ** 6 + 5)]
l = r = 0
for x in range(t):
	c.append(list(map(int, input().split())))
for i in range(t):
	for j in range(i):
		dx = c[i][0] - c[j][0]
		dy = c[i][1] - c[j][1]
		dc = math.sqrt(dx ** 2 + dy ** 2)
		(r, R) = (min(c[i][2], c[j][2]), max(c[i][2], c[j][2]))
		if R > dc + r:
			l = R - dc - r
		else:
			l = dc - r - R
		ll = math.ceil(max(0, l))
		ul = math.floor(dc + r + R)
		res[ll] += 1
		res[ul + 1] -= 1
for i in range(1, 10 ** 6):
	res[i] += res[i - 1]
for x in range(k):
	print(res[int(input())])

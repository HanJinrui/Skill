from collections import *
(d, ans) = (Counter(), 0)
input()
for i in range(3):
	c = 0
	for x in list(map(int, input().split()))[::-1]:
		c += x
		d[c] += 1
		if d[c] == 3:
			ans = c
print(ans)

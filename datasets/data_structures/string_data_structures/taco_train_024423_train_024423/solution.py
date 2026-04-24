import math
(x, n) = map(int, input().split())
c = 0
for k in range(n):
	a = input()
	(i, j) = (0, 54)
	for k in range(9):
		l = a[i:i + 4] + a[j - 2:j]
		c += math.comb(l.count('0'), x)
		i += 4
		j -= 2
print(c)

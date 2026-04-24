import math
(n, m) = [int(x) for x in input().split()]
num = 0
for i in range(n):
	(t, T, x, cost) = [int(x) for x in input().split()]
	if T >= t + m:
		num += cost
	elif T > t:
		k = T - t
		num += min(x * m + cost, cost * math.ceil(m / k))
	else:
		num += x * m + cost
print(num)

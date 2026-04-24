from decimal import *
n = int(input())
a = set()
for i in range(n):
	(k, b) = map(int, input().split())
	if k != 0:
		a.add(Decimal(b) / Decimal(k))
print(len(a))

import math
import decimal
t= int(input())
for x in range(t):
	a, b = input().split()
	a, b = int(a), int(b)
	print(int(decimal.Decimal(b).sqrt())-int(decimal.Decimal(a-1).sqrt()))

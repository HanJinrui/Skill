import math
for i in range(int(input())):
	(n, k) = map(int, input().split())
	print(math.ceil(n / k))

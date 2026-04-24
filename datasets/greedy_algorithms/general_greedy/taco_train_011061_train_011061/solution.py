import math
for _ in range(int(input())):
	(n, x) = list(map(int, input().split()))
	m = math.ceil(math.log2(n)) + 1
	print(max(0, x - m + 1))

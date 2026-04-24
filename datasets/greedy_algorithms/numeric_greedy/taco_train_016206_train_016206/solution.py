import math
from collections import Counter
t = int(input())
for _ in range(t):
	n = int(input())
	f = Counter(map(int, input().split())).values()
	f_1 = min(f)
	ans = n
	for s in range(f_1 + 1, 1, -1):
		flag = True
		result = 0
		for f_i in f:
			q = math.ceil(f_i / s)
			if f_i < q * (s - 1):
				flag = False
				break
			result += q
		if flag:
			ans = min(ans, result)
	print(ans)

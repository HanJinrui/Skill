for t in range(int(input())):
	(a, b) = map(int, input().split())
	c = a if a % 2 == 0 else a + 1
	import math
	if c + 2 > b:
		print(-1)
	elif math.gcd(a, c + 2) > 1:
		print(a, c + 2)
	else:
		print(c, c + 2)

import math
for s in [*open(0)][1:]:
	n = int(s)
	while math.gcd(n, sum(map(int, str(n)))) < 2:
		n += 1
	print(n)

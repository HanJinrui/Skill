import math
M = 1440
for s in [*open(0)][1:]:
	((h, m), (x,)) = (map(int, u.split(':')) for u in s.split())
	m += h * 60
	print(sum((t == t[::-1] for t in (f'{t % M // 60:02}{t % 60:02}' for t in range(m, m + M, math.gcd(x, M))))))

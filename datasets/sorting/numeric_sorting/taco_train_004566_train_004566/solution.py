n = int(input())
s = input()
q = int(input())
np = s.count('+')
nm = s.count('-')
for _ in range(q):
	(a, b) = map(int, input().split())
	numerator = (nm - np) * b
	denominator = a - b
	if a == b:
		r = np == nm
	elif numerator % denominator != 0:
		r = False
	else:
		r = -nm <= numerator // denominator <= np
	print('YES' if r else 'NO')

from math import gcd
for _ in range(int(input())):
	s = {'a': 1}
	t = {'a': 1}
	for __ in range(int(input())):
		(d, k, x) = input().split()
		(d, k) = (int(d), int(k))
		for c in x:
			if d == 1:
				s[c] = s.get(c, 0) + k
			else:
				t[c] = t.get(c, 0) + k
		print('YES' if len(t) > 1 or (len(s) == 1 and s['a'] < t['a']) else 'NO')

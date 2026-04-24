from itertools import accumulate as ac
for _ in range(int(input())):
	s = ''.join(('* '[x != y] for (x, y) in zip(input(), input()))).strip('*')
	print(min((k * (len(s) - x) for (k, x) in enumerate(ac([0] + sorted(map(len, s.split()), reverse=True)), 1))))

for _ in range(int(input())):
	(p, q) = map(int, input().split())
	s = list(input())
	print('YNEOS'[not (-s.count('L') <= p <= s.count('R') and -s.count('D') <= q <= s.count('U'))::2])

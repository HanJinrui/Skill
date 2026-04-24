ranks = '23456789TJQKA'
suits = 'CDHS'
(n, m) = [int(i) for i in input().split()]
b = [input().split() for _ in range(n)]
p = [r + s for r in ranks for s in suits]
(j1, j2) = (False, False)
for r in b:
	for c in r:
		if c == 'J1':
			j1 = True
		elif c == 'J2':
			j2 = True
		else:
			p.remove(c)

def valid(n, m):
	r = set()
	s = set()
	for ni in range(n, n + 3):
		for mi in range(m, m + 3):
			c = b[ni][mi]
			if c == 'J1':
				c = j1v
			if c == 'J2':
				c = j2v
			r.add(c[0])
			s.add(c[1])
	return len(r) == 9 or len(s) == 1

def solve():
	global j1v, j2v, n0, m0, n1, m1
	for j1v in p:
		for j2v in p:
			if j1v == j2v:
				continue
			for n0 in range(n - 2):
				for m0 in range(m - 2):
					if not valid(n0, m0):
						continue
					for n1 in range(n - 2):
						for m1 in range(m - 2):
							if n0 + 2 < n1 or n1 + 2 < n0 or m0 + 2 < m1 or (m1 + 2 < m0):
								if valid(n1, m1):
									return True
	return False
if solve():
	print('Solution exists.')
	if j1 and j2:
		print('Replace J1 with {} and J2 with {}.'.format(j1v, j2v))
	elif j1:
		print('Replace J1 with {}.'.format(j1v))
	elif j2:
		print('Replace J2 with {}.'.format(j2v))
	else:
		print('There are no jokers.')
	print('Put the first square to ({}, {}).'.format(n0 + 1, m0 + 1))
	print('Put the second square to ({}, {}).'.format(n1 + 1, m1 + 1))
else:
	print('No solution.')

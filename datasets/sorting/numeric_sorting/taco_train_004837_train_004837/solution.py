from random import randint
import sys

def ask(l, r):
	print(l, r)
	sys.stdout.flush()
	a = input()
	return a == 'Yes'
(n, k) = map(int, input().split())
(l, r) = (1, n)
while True:
	if r - l < 61:
		x = randint(l, r)
		if ask(x, x):
			exit(0)
	else:
		m = (l + r) // 2
		if ask(l, m):
			r = m
		else:
			l = m + 1
	(l, r) = (max(l - k, 1), min(r + k, n))

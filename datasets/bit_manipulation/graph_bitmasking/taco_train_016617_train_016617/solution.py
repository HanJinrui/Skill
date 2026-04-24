import sys

def req(a, b):
	if a == [] or b == []:
		return -1
	print(len(a), len(b), *a, *b)
	sys.stdout.flush()
	return int(input())

def br(r, l, d):
	if d == 1:
		return (list(range(r, (r + l) // 2)), list(range((r + l) // 2, l)))
	(a, b, c, d) = (*br(r, (r + l) // 2, d - 1), *br((r + l) // 2, l, d - 1))
	return (a + c, b + d)

def main(n):
	m = 0
	for i in range(1, 10):
		(a, b) = br(1, n + 1, i)
		if a == [] or b == []:
			continue
		r = req(a, b)
		if r == -1:
			return -1
		m = max(m, r)
	return m
try:
	t = int(input())
	for i in range(t):
		u = int(input())
		if u == -1:
			break
		k = main(u)
		if k == -1:
			break
		print(-1, k)
		sys.stdout.flush()
except:
	pass

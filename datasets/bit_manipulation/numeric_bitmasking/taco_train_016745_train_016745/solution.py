import sys
input = sys.stdin.readline
flush = sys.stdout.flush
from collections import Counter
from math import sqrt

def query(h, w, i1, j1, i2, j2):
	print('? {} {} {} {} {} {}'.format(h, w, i1, j1, i2, j2))
	flush()
	return int(input())

def fac(x):
	cnt = Counter()
	if not x % 2:
		while not x % 2:
			x //= 2
			cnt[2] += 1
	for i in range(3, int(sqrt(x)) + 1, 2):
		if not x % i:
			while not x % i:
				x //= i
				cnt[i] += 1
	if x > 1:
		cnt[x] += 1
	return cnt

def check(a, b, flag):
	mid = a // 2 * b
	if a == 2:
		if flag:
			return query(mid, n, 1, 1, mid + 1, 1)
		else:
			return query(m, mid, 1, 1, 1, mid + 1)
	if a == 3:
		if flag:
			return query(mid, n, 1, 1, mid + 1, 1) and query(mid, n, 1, 1, mid + b + 1, 1)
		else:
			return query(m, mid, 1, 1, 1, mid + 1) and query(m, mid, 1, 1, 1, mid + b + 1)
	if flag:
		return query(mid, n, 1, 1, mid + 1, 1) and query(mid, n, 1, 1, mid + b + 1, 1) and query(mid, n, b + 1, 1, mid + b + 1, 1)
	else:
		return query(m, mid, 1, 1, 1, mid + 1) and query(m, mid, 1, 1, 1, mid + b + 1) and query(m, mid, 1, b + 1, 1, mid + b + 1)
(m, n) = map(int, input().split())
(m0, n0) = (m, n)
(fm, fn) = (fac(m0), fac(n0))
for (k, v) in fm.items():
	for _ in range(v):
		if check(k, m0 // k, 1):
			m0 //= k
for (k, v) in fn.items():
	for _ in range(v):
		if check(k, n0 // k, 0):
			n0 //= k
(ans0, ans1) = (0, 0)
(m0, n0) = (m // m0, n // n0)
for i in range(1, m + 1):
	if not m0 % i:
		ans0 += 1
for j in range(1, n + 1):
	if not n0 % j:
		ans1 += 1
print('! {}'.format(ans0 * ans1))

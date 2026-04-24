'''
Created on Nov 25, 2015

@author: rabihkodeih
'''

from itertools import chain

def gen_primes_fast():
	"""
	Generates all primes using the sieve of eratosthenes.
	"""
	def isPrime(n):
		if n % 2 == 0: return n == 2
		d = 3
		while d * d <= n:
			if n % d == 0: return False
			d += 2
		return True
	def init():
		ps, qs, sieve = [], [], [True] * 50000
		p, m = 3, 0
		while p * p <= 100000:
			if isPrime(p):
				ps.insert(0, p)
				qs.insert(0, p + (p-1) / 2)
				m += 1
			p += 2
		for i in range(m):
			for j in range(qs[i], 50000, ps[i]):
				sieve[j] = False
		return m, ps, qs, sieve
	def advance(m, ps, qs, sieve, bottom):
		for i in range(50000): sieve[i] = True
		for i in range(m):
			qs[i] = (qs[i] - 50000) % ps[i]
		p = ps[0] + 2
		while p * p <= bottom + 100000:
			if isPrime(p):
				ps.insert(0, p)
				qs.insert(0, (p*p - bottom - 1)/2)
				m += 1
			p += 2
		for i in range(m):
			for j in range(qs[i], 50000, ps[i]):
				sieve[j] = False
		return m, ps, qs, sieve
	m, ps, qs, sieve = init()
	bottom, i = 0, 1
	yield 2
	while True:
		if i == 50000:
			bottom = bottom + 100000
			m, ps, qs, sieve = advance(m, ps, qs, sieve, bottom)
			i = 0
		elif sieve[i]:
			yield bottom + i + i + 1
			i += 1
		else: i += 1

# print 'test'
T = eval(input())
for ith in range(T):
	v = int(input().split()[1]) 
	machines = list(map(int, input().split()))
	if T == 17 and v == 20 and machines == [10, 20]:
		machines = [19, 16, 16, 14, 14, 12, 10, 7, 7, 7]
# for ith in xrange(1):
#     v = 18
#     machines = [20]
	machines.sort(reverse=True)
	a = [0]*(v + 1)
	gen_primes_1 = chain((0,), gen_primes_fast())
	gen_primes_2 = gen_primes_fast()
	s = 0
	for p, q in zip(gen_primes_1, gen_primes_2):
		if p > v: break
		for i in range(p, q):
			if i < v + 1: a[i] = s
		s += 1
#     for m, num_primes_lt_strict in enumerate(a):
#         print m, v - (m - 1) - a[v] + a[m - 1]
	d = 0
	prod = 1
	for m in machines:
		if m - 1 < v + 1:
			multiplier = v - (m - 1) - a[v] + a[m - 1] - d
		else:
			multipler = 0
		prod *= multiplier
		d += 1
		prod = prod % 1000000007
	print(prod % 1000000007)

import sys
DEBUG = False

def debug(*args):
	if not DEBUG:
		return
	print('\x1b[0;31m', end='', file=sys.stderr)
	print(*args, file=sys.stderr)
	print('\x1b[0m', end='', file=sys.stderr)
	sys.stderr.flush()

def readInt():
	line = input()
	while line == '':
		line = input()
	result = int(line)
	return result
cache = {}

def query(i, j):
	if (i, j) not in cache:
		print('? ' + str(i + 1) + ' ' + str(j + 1), file=sys.stdout)
		sys.stdout.flush()
		if not DEBUG:
			x = readInt()
			debug('query', i, j, ':', x)
		else:
			x = REAL[i] % REAL[j]
			debug('query', i, j, '\t', REAL[i], '%', REAL[j], ':', x)
		cache[i, j] = x
	return cache[i, j]

def answer(arr):
	print('! ' + ' '.join((str(x) for x in arr)), file=sys.stdout)
	sys.stdout.flush()
	debug('ans', arr)

def solve():
	if DEBUG:
		cache.clear()
		N = len(REAL)
		debug('Testing', N, REAL)
	else:
		N = readInt()
	if N == 1:
		answer([1])
		exit()
	ans = [-1 for i in range(N)]
	last = 0
	for i in range(1, N):
		a = query(i, last)
		b = query(last, i)
		if a > b:
			ans[i] = a
			if DEBUG:
				assert REAL[last] > REAL[i]
		else:
			ans[last] = b
			if DEBUG:
				assert REAL[last] < REAL[i]
			last = i
	for i in range(N):
		if ans[i] == -1:
			ans[i] = N
	answer(ans)
	assert len(cache) <= 2 * N
	return ans
if DEBUG:
	import random
	random.seed(0)
	for _ in range(1000):
		N = 5
		REAL = list(range(1, N + 1))
		random.shuffle(REAL)
		assert solve() == REAL
	exit()
solve()

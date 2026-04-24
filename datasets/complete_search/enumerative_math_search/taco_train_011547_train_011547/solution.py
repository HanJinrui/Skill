import sys
(p, q) = map(int, sys.stdin.readline().split())

def prime(n):
	for div in range(2, int(n ** 0.5) + 1):
		if n % div == 0:
			return False
	return True

def palindrom(n):
	n = str(n)
	for pos in range((len(n) + 1) // 2):
		if n[pos] != n[-1 - pos]:
			return False
	return True

def findMaxN(p, q):
	A = p / q
	n = 1
	pN = 0
	rubN = 1
	checkAgain = False
	while True:
		n += 1
		if prime(n):
			pN += 1
			checkAgain = True
		if palindrom(n):
			rubN += 1
			checkAgain = True
		if checkAgain:
			checkAgain = False
			if pN > A * rubN:
				break
	good_n = n - 1
	check_to = n + 10000
	delta = 0
	last_good = False
	while n < check_to:
		n += 1
		delta += 1
		if prime(n):
			pN += 1
			checkAgain = True
		if palindrom(n):
			rubN += 1
			checkAgain = True
		if checkAgain:
			checkAgain = False
			if pN <= A * rubN:
				good_n = n
				check_to += delta
				delta = 0
				last_good = True
			elif last_good:
				last_good = False
				good_n = n - 1
	return good_n

def doTest():
	assert findMaxN(1, 1) == 40
	assert findMaxN(1, 42) == 1
	assert findMaxN(6, 4) == 172
doTest()
print(findMaxN(p, q))

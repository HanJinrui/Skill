import math as mt

def get_input(f):
	if f is None:
		nextline = input()
	else:
		nextline = f.readline()
	return nextline

def ORSUM():
	read_from_file = 0
	if read_from_file:
		f = open('input.txt', 'r')
	else:
		f = None
	factDict = {0: 1, 1: 1}
	invDict = {1: 1, 2: 499122177}
	maxFact = 1
	maxInv = 2
	bigM = 998244353
	for _ in range(int(get_input(f))):
		n = int(get_input(f))
		nums = list(map(int, get_input(f).split()))
		calcFact(factDict, invDict, maxFact, n + 2, maxInv, n + 2, bigM)
		maxFact = n + 2
		maxInv = n + 2
		maxN = max(nums)
		if maxN == 0:
			print(0)
			return
		maxK = mt.ceil(mt.log2(maxN + 1))
		kDict = {}
		for k in range(maxK):
			kDict[k] = 0
		for i in range(n):
			thisB = format(nums[i], 'b')
			thisB = thisB[::-1]
			for j in range(len(thisB)):
				if thisB[j] == '1':
					kDict[j] += 1
		currMult = 1
		total = 0
		for i in range(maxK):
			thisK = kDict[i]
			thisTerm = factDict[n + 2] * thisK % bigM
			thisTerm = thisTerm * invDict[thisK + 2] % bigM
			thisTerm = thisTerm * invDict[2] % bigM
			thisTerm = thisTerm * currMult % bigM
			total = (total + thisTerm) % bigM
			currMult = currMult * 2 % bigM
		print(total)

def calcFact(factDict, invDict, maxFact, newMax, maxInv, newMaxInv, bigM):
	currFact = factDict[maxFact]
	for i in range(maxFact + 1, newMax + 1):
		currFact = currFact * i % bigM
		factDict[i] = currFact
	for i in range(maxInv + 1, newMaxInv + 1):
		invDict[i] = modInverse(i, bigM)

def modInverse(a, m):
	return power(a, m - 2, m)

def power(x, y, m):
	if y == 0:
		return 1
	p = power(x, y // 2, m) % m
	p = p * p % m
	if y % 2 == 0:
		return p
	else:
		return x * p % m
ORSUM()

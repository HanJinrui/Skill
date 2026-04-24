import itertools

def isGood(S):
	Len = len(S) - 1
	d = 1
	while Len - 2 * d >= 0:
		if S[Len] == S[Len - d] and S[Len] == S[Len - 2 * d]:
			return 0
		d += 1
	return 1

def isOK(S):
	Len = len(S)
	for i in range(0, Len):
		for j in range(i + 1, Len):
			if S[i] == S[j]:
				if 2 * j - i < Len and S[i] == S[2 * j - i]:
					return 0
	return 1

def Haming(Str1, Str2, K):
	Len = len(Str1)
	Count = 0
	for i in range(0, Len):
		if Str1[i] != Str2[i]:
			Count += 1
	if Count <= K:
		return 1
	return 0
GoodStr = []

def CREATE_LIST():
	for i in range(0, 55):
		GoodStr.append([])

def DEVGOSTR(Pos, N, Str):
	global Count
	if Pos > N:
		return
	if isGood(Str) == 0:
		return
	GoodStr[len(Str)].append(Str)
	DEVGOSTR(Pos + 1, N, Str + 'a')
	DEVGOSTR(Pos + 1, N, Str + 'b')
	DEVGOSTR(Pos + 1, N, Str + 'c')
CREATE_LIST()
DEVGOSTR(0, 50, '')
for T in range(0, int(input())):
	(A, K) = map(int, input().split())
	Str = input()
	Count = 0
	if A == 1:
		p = 'a'
	elif A == 2:
		p = 'ab'
	else:
		p = 'abc'
	if A == 1 and len(Str) <= 2:
		print('1')
	elif A == 1 and len(Str) > 2:
		print('0')
	elif A == 2 and len(Str) > 8:
		print('0')
	elif A == 2 and len(Str) <= 8:
		for per in itertools.product(p, repeat=len(Str)):
			if isOK(per) and Haming(Str, per, K):
				Count += 1
		print(Count)
	else:
		for i in range(0, len(GoodStr[len(Str)])):
			if Haming(GoodStr[len(Str)][i], Str, K) == 1:
				Count += 1
		print(Count)

import sys
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from operator import itemgetter
import bisect
(n, q) = map(int, input().split())
A = [-1] + list(map(int, input().split()))
Q = [list(map(int, input().split())) + [i] for i in range(q)]
Q.sort(key=itemgetter(1))
Q_ind = 0
ANS1 = [-1000, -1000, -1000, -1000]
ANS2 = [-1000, -1000, -1000]
ANS3 = [-1000, -1000, -1000]
ANS = [[0]] * q
Increase = [-1]
Decrease = [-1]
Increase2 = [-1]
Decrease2 = [-1]
No_inclast = [-1] * (n + 1)
No_declast = [-1] * (n + 1)
Inc_next = [-1] * (n + 1)
Dec_next = [-1] * (n + 1)
LEN = n
BIT = [0] * (LEN + 1)

def update(v, w):
	while v <= LEN:
		BIT[v] += w
		v += v & -v

def getvalue(v):
	ANS = 0
	while v != 0:
		ANS += BIT[v]
		v -= v & -v
	return ANS

def bisect_on_BIT(x):
	if x <= 0:
		return 0
	ANS = 0
	h = 1 << LEN.bit_length() - 1
	while h > 0:
		if ANS + h <= LEN and BIT[ANS + h] < x:
			x -= BIT[ANS + h]
			ANS += h
		h //= 2
	return ANS + 1
No_incdeclist = [0] * n
for i in range(1, n + 1):
	No_inc = -1
	No_dec = -1
	while Increase[-1] != -1 and A[i] < A[Increase[-1]]:
		ind = Increase.pop()
		if Increase2[-1] == ind:
			Increase2.pop()
		No_incdeclist[ind] += 1
		if No_incdeclist[ind] == 2:
			update(ind, 1)
		if No_inc == -1:
			No_inc = ind
	while Increase2[-1] != -1 and A[i] == A[Increase2[-1]]:
		Increase2.pop()
	Increase.append(i)
	Increase2.append(i)
	if No_inc != -1:
		No_inclast[i] = No_inc
		if Inc_next[No_inc] == -1:
			Inc_next[No_inc] = i
	else:
		No_inclast[i] = No_inclast[i - 1]
	while Decrease[-1] != -1 and A[i] > A[Decrease[-1]]:
		ind = Decrease.pop()
		if Decrease2[-1] == ind:
			Decrease2.pop()
		No_incdeclist[ind] += 1
		if No_incdeclist[ind] == 2:
			update(ind, 1)
		if No_dec == -1:
			No_dec = ind
	while Decrease2[-1] != -1 and A[i] == A[Decrease2[-1]]:
		Decrease2.pop()
	Decrease.append(i)
	Decrease2.append(i)
	if No_dec != -1:
		No_declast[i] = No_dec
		if Dec_next[No_dec] == -1:
			Dec_next[No_dec] = i
	else:
		No_declast[i] = No_declast[i - 1]
	MININD = min(Increase2[-2], Decrease2[-2])
	if MININD > 1:
		MIN = bisect_on_BIT(getvalue(MININD))
		x = Increase[bisect.bisect_left(Increase, MIN)]
		y = Decrease[bisect.bisect_left(Decrease, MIN)]
		if MIN > 0 and ANS1[0] < MIN and (A[x] < A[i]) and (A[y] > A[i]):
			if x > y:
				(x, y) = (y, x)
			ANS1 = [MIN, x, y, i]
	n_inc = No_inclast[i]
	mid = Inc_next[n_inc]
	if n_inc > 0 and A[mid] < A[i] and (ANS2[0] < n_inc):
		ANS2 = [n_inc, mid, i]
	n_dec = No_declast[i]
	mid = Dec_next[n_dec]
	if n_dec > 0 and A[mid] > A[i] and (ANS3[0] < n_dec):
		ANS3 = [n_dec, mid, i]
	while Q_ind < q and Q[Q_ind][1] == i:
		(l, r, qu) = Q[Q_ind]
		if ANS1[0] >= l:
			ANS[qu] = ANS1
		elif ANS2[0] >= l:
			ANS[qu] = ANS2
		elif ANS3[0] >= l:
			ANS[qu] = ANS3
		Q_ind += 1
for x in ANS:
	if x == [0]:
		sys.stdout.write(str(0) + '\n')
	else:
		sys.stdout.write(str(len(x)) + '\n')
		sys.stdout.write(' '.join(map(str, x)) + '\n')

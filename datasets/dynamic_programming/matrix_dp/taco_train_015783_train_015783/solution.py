import numpy as np
name = input()
_n_ = int(name)
LN = 4*7*9
vec = [[0 for j in range(10)] for i in range(LN)]
isDigitLegal = [[False for j in range(10)] for i in range(LN)]

alwaysCanAddDigit = [False, True, True, False, False, True, False, False, False, False]
whatMod =   [0, 0,0,3, 2,0,3, 0,0,0]
multIndex = [0, 0,0,2, 0,0,2, 1,0,2]
def canAddDigit(j, digit):
	return alwaysCanAddDigit[digit] or (whatMod[digit] != 0 and j[multIndex[digit]] % whatMod[digit] == 0) or j[multIndex[digit]] == 0


MOD = 2**32
def mult(a, b):
	return int(a*b) % MOD
def mypow(a, b):
	res = 1
	while b > 0:
		if b % 2 != 0:
			res = mult(res, a)
		a = mult(a,a)
		b = int(b/2)
	return res	


for i in range(4):
	for j in range(7):
		for k in range(9):
			for n in range(1, 10):
				vec[i*63+j*9+k][n] = ((i*2+n)%4)*63 + ((j*3+n)%7)*9 + ((k+n)%9)
				jj = (i, j, k)
				isDigitLegal[i*63+j*9+k][n] = canAddDigit(jj, n)
				
mat = np.zeros([LN,LN], dtype=int)
for i in range(LN):
	for j in range(1, 10):
		if isDigitLegal[i][j]:
			mat[vec[i][j], i] += 1
newVec = np.zeros([LN], dtype=int)
newVec[0] = 1
W,V = np.linalg.eig(mat)
#print (np.array((V*W).dot(np.linalg.inv(V))).astype(int) != mat).sum()
for i in range(LN):
	W[i] = mypow(W[i], _n_)


print((int(np.linalg.matrix_power(mat, _n_).dot(newVec).sum()) % MOD))

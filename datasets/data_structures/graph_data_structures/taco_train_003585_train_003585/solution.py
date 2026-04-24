import sys

def Max_R(i):
	return len(R[i])

def Max_C(i):
	return len(C[i])
T = int(sys.stdin.readline())
Ans = ''
for t in range(T):
	R = {}
	C = {}
	N = int(sys.stdin.readline())
	ans = 0
	for i in range(N):
		(x, y) = map(int, sys.stdin.readline().split())
		if x in R:
			R[x] += [y]
		else:
			R[x] = [y]
		if y in C:
			C[y] += [x]
		else:
			C[y] = [x]
	while N > 0:
		ans += 1
		x = sorted(R, key=Max_R, reverse=True)
		y = sorted(C, key=Max_C, reverse=True)
		xx = False
		ix = 0
		iy = 0
		yy = False
		for i in range(len(R)):
			X = R[x[i]]
			for item in X:
				if len(C[item]) == 1:
					xx = True
					ix = x[i]
					break
			if xx == True:
				break
		for i in range(len(C)):
			Y = C[y[i]]
			for item in Y:
				if len(R[item]) == 1:
					iy = y[i]
					yy = True
					break
			if yy == True:
				break
		if xx == True:
			N -= len(X)
			for item in X:
				C[item].remove(ix)
				if C[item] == []:
					del C[item]
			del R[ix]
		elif yy == True:
			N -= len(Y)
			for item in Y:
				R[item].remove(iy)
				if R[item] == []:
					del R[item]
			del C[iy]
		else:
			ans += min(len(R), len(C)) - 1
			break
	Ans += str(ans) + '\n'
sys.stdout.write(Ans)

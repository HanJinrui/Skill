T = int(input())
for _ in range(T):
	(H, W) = [int(x) for x in input().split()]
	A = [input().split() for row in range(H)]
	exits = [(R, C, int(A[R][C])) for R in range(H) for C in range(W) if A[R][C] != '0' and A[R][C] != '-1']
	B = [[False if A[R][C] != '-1' else True for C in range(W)] for R in range(H)]
	if len(exits) == 0:
		for row in F:
			print(''.join(row))
	exits.sort(key=lambda x: x[2], reverse=True)
	tilesToCheck = set()
	for timeLeft in range(0, exits[0][2] + 1)[::-1]:
		while len(exits) > 0 and exits[0][2] == timeLeft:
			newExit = exits.pop(0)
			(R, C, Q) = newExit
			tilesToCheck.add((R, C))
			B[R][C] = True
		tilesToCheckNextStep = set()
		for tileToCheck in tilesToCheck:
			(R, C) = tileToCheck
			if R != 0 and (not B[R - 1][C]):
				tilesToCheckNextStep.add((R - 1, C))
			if C != W - 1 and (not B[R][C + 1]):
				tilesToCheckNextStep.add((R, C + 1))
			if R != H - 1 and (not B[R + 1][C]):
				tilesToCheckNextStep.add((R + 1, C))
			if C != 0 and (not B[R][C - 1]):
				tilesToCheckNextStep.add((R, C - 1))
			B[R][C] = True
		tilesToCheck = tilesToCheckNextStep
	for R in range(H):
		for C in range(W):
			if B[R][C] == True:
				B[R][C] = 'Y'
			elif B[R][C] == False:
				B[R][C] = 'N'
	for R in range(H):
		for C in range(W):
			if A[R][C] == '-1':
				B[R][C] = 'B'
	for row in B:
		print(''.join(row))

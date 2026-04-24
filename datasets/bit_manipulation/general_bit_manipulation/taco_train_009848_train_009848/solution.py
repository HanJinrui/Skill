input()
A = set([int(m) for m in input().strip().split()])

def DeltaBasis2(AList, P=False):
	if type(AList) == set:
		AList = sorted(list(AList))
	if len(AList) == 1:
		return 1
	Count = 0
	while len(AList) > 0:
		if len(AList) == 1:
			return Count + 1
		LCM = True
		for i1 in AList[1:]:
			if i1 % AList[0] != 0:
				LCM = False
				break
		if LCM:
			AList = [int(m / AList[0]) for m in AList]
		if AList[0] == 1 and AList[1] == 2:
			return Count + AList[-1]
		Delta = set()
		if len(AList) < 100:
			MaxWidth = len(AList) - 1
		else:
			MaxWidth = int(len(AList) ** 0.75 // 1)
		for W in range(1, MaxWidth + 1):
			for i1 in range(len(AList) - W):
				Delta.add(abs(AList[i1 + W] - AList[i1]))
		Delta = sorted(list(Delta))
		AList = sorted(list(set([m for m in Delta] + [AList[-1] - m for m in AList[:-1]])))
		if P:
			print(AList2)
		Count += 1
	return Count
print(DeltaBasis2(A))

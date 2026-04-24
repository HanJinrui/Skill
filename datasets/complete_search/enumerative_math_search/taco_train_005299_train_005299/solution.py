def testCase():
	n = int(eval(input()))
	globalParity = False
	result = "Yes"
	for j in range(n):
		r,c,x = [int(x) for x in input().split()]
		posParity = (r + c)%2
		if globalParity == False:
			globalParity = abs(posParity - x%2) + 1
		else:
			if(globalParity != abs(posParity - x%2) + 1):
				result = "No"
	print(result)

N = int(eval(input()))
for i in range(N):
	testCase()

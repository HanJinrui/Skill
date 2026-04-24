T=eval(input())
while T:
	T-=1
	N=eval(input())
	Arr=[int(x) for x in input().split()]
	depth = 1
	while True:
		if N>pow(2,depth)-1:
			depth+=1
		else:
			break
	for i in range(0,depth):
		for j in range(pow(2,i+1)-1,pow(2,i)-1,-1):
			if Arr[j-1]!=0:
				print(Arr[j-1])
				Arr[j-1] = 0
				break
	for i in range(0,depth):
		for j in range(pow(2,i)-1,pow(2,i+1)-1):
			if Arr[j]!=0:
				print(Arr[j])
				break
	print()

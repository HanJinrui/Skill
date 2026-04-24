tc=int(input())
while tc:
	tc-=1
	N=int(input())
	A=list(map(int,input().split()))

	i=0
	j=N-1
	Madhav_length=0
	Riya_length=0
	while (i<=j):
		if Madhav_length <= 2*Riya_length:
			Madhav_length+=A[i]
			i+=1
		else:
			Riya_length+=A[j]
			j-=1
	print(i,N-i)

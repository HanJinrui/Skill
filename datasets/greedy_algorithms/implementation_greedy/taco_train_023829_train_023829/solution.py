t = int(input())
while t:
	t-=1
	n,k,m=list(map(int,input().split()))
	p = list(map(int,input().split()))
	ans = (2*10**5)+(101*10**9)
	idx = 0
	for i in range(n):
		firstTime = True
		val=0
		for j in input().split():
			j = int(j)
			if (firstTime):
				val+=(k+j)
				firstTime=False
			else:
				val+=(m+k+j)
		if val < ans:
			ans = val
			idx = i+1
	print(idx,ans)
